import argparse
import hashlib
import os
from pathlib import Path
from typing import List, Optional

import pandas as pd


def stable_token(value: str, salt: str, prefix: str = "GRW_", length: int = 12) -> str:
    """
    Create a deterministic anonymized token using SHA-256 with a provided salt.
    - value: original string value (e.g., grower name)
    - salt: secret salt string (kept private, not committed)
    - prefix: token prefix for easier auditing
    - length: number of hex characters to keep from the hash
    Returns: prefix + hex[:length]
    """
    norm = (value or "").strip().lower()
    digest = hashlib.sha256(f"{salt}|{norm}".encode("utf-8")).hexdigest()
    return f"{prefix}{digest[:length]}"


def anonymize_column(df: pd.DataFrame, column: str, salt: str, prefix: str = "GRW_") -> pd.DataFrame:
    if column not in df.columns:
        raise ValueError(f"Column '{column}' not found in dataframe: {list(df.columns)}")
    df = df.copy()
    unique_vals = df[column].astype(str).fillna("").unique()
    mapping = {val: stable_token(val, salt=salt, prefix=prefix) for val in unique_vals}
    df[column] = df[column].astype(str).map(mapping)
    return df


def try_read_csv(path: Path) -> pd.DataFrame:
    # Try utf-8 first, then fall back to cp1252 commonly used in Windows CSVs
    try:
        return pd.read_csv(path, encoding="utf-8")
    except UnicodeDecodeError:
        return pd.read_csv(path, encoding="cp1252")


def write_csv(df: pd.DataFrame, out_path: Path) -> None:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(out_path, index=False)


def anonymize_files(
    inputs: List[Path],
    column: str,
    salt: str,
    suffix: str = "_anonymized",
    prefix: str = "GRW_",
    mapping_out: Optional[Path] = None,
) -> None:
    mapping_rows = []
    for in_path in inputs:
        df = try_read_csv(in_path)
        original_values = df[column].astype(str).fillna("") if column in df.columns else None
        df_anon = anonymize_column(df, column=column, salt=salt, prefix=prefix)
        out_path = in_path.with_name(in_path.stem + suffix + in_path.suffix)
        write_csv(df_anon, out_path)
        if mapping_out is not None and original_values is not None:
            # Collect unique mapping for this file
            uniq = pd.DataFrame({
                "file": str(in_path),
                "original": original_values.unique(),
            })
            uniq["anonymized"] = uniq["original"].map(lambda v: stable_token(v, salt=salt, prefix=prefix))
            mapping_rows.append(uniq)
        print(f"Wrote anonymized file: {out_path}")

    if mapping_out is not None and mapping_rows:
        mapping_df = pd.concat(mapping_rows, ignore_index=True).drop_duplicates()
        mapping_out.parent.mkdir(parents=True, exist_ok=True)
        mapping_df.to_csv(mapping_out, index=False)
        print(f"Wrote mapping file (keep private!): {mapping_out}")


def main():
    parser = argparse.ArgumentParser(description="Anonymize sensitive string columns in CSV files deterministically.")
    parser.add_argument(
        "--inputs",
        nargs="+",
        required=True,
        help="One or more CSV file paths to anonymize (space-separated)",
    )
    parser.add_argument(
        "--column",
        default="Grower",
        help="Column name to anonymize (default: Grower)",
    )
    parser.add_argument(
        "--salt",
        default=os.getenv("GROWER_ANON_SALT", ""),
        help="Secret salt for hashing. If omitted, reads GROWER_ANON_SALT env var; if still empty, will error.",
    )
    parser.add_argument(
        "--suffix",
        default="_anonymized",
        help="Suffix to append to filenames before extension (default: _anonymized)",
    )
    parser.add_argument(
        "--prefix",
        default="GRW_",
        help="Prefix to add to anonymized tokens (default: GRW_)",
    )
    parser.add_argument(
        "--mapping-out",
        default=None,
        help="Optional path to save original->anonymized mapping CSV (keep private, do not publish)",
    )

    args = parser.parse_args()

    if not args.salt:
        raise SystemExit(
            "Error: No salt provided. Pass --salt 'your-secret-salt' or set env var GROWER_ANON_SALT."
        )

    input_paths = [Path(p) for p in args.inputs]
    mapping_out = Path(args.mapping_out) if args.mapping_out else None

    anonymize_files(
        inputs=input_paths,
        column=args.column,
        salt=args.salt,
        suffix=args.suffix,
        prefix=args.prefix,
        mapping_out=mapping_out,
    )


if __name__ == "__main__":
    main()
