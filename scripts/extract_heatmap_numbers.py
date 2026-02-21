import pandas as pd
import numpy as np

df = pd.read_parquet('data/processed/simulations/simulations_2_21_2026.parquet')
df14 = df[df['Year'] == 2014].copy()

# The heatmap shows Mean Profit Percent Change averaged over simulations
agg = df14.groupby(['Market Demand','V6 Percent','Initial Probability','Sprays in May','Quantile'])['Mean Profit Percent Change'].mean().reset_index()
agg.rename(columns={'Mean Profit Percent Change': 'MPC'}, inplace=True)

print('=== GLOBAL RANGE 2014 ===')
print(f'Min: {agg.MPC.min():.2f}%')
print(f'Max: {agg.MPC.max():.2f}%')
print()

# 1) Low inoculum: p0 <= 1e-4
low_inoc = agg[agg['Initial Probability'] <= 1e-4]
print('=== LOW INOCULUM (p0 <= 1e-4) ===')
print(f'  Overall range: {low_inoc.MPC.min():.2f}% to {low_inoc.MPC.max():.2f}%')
for dem in ['high','moderate','low']:
    sub = low_inoc[low_inoc['Market Demand']==dem]
    print(f'  {dem}: {sub.MPC.min():.2f}% to {sub.MPC.max():.2f}%')
print()

# 2) High inoculum p0=0.01, 0 sprays
print('=== HIGH INOCULUM p0=0.01, 0 SPRAYS ===')
hi = agg[(agg['Initial Probability']==0.01) & (agg['Sprays in May']==0)]
for dem in ['high','moderate','low']:
    sub = hi[hi['Market Demand']==dem]
    print(f'  {dem}: min={sub.MPC.min():.2f}%, max={sub.MPC.max():.2f}%')
    # Show by quantile (lowest and highest) and V6
    for q in [0.2, 1.0]:
        for v6 in [0.0, 0.5, 1.0]:
            val = sub[(sub['Quantile']==q) & (sub['V6 Percent']==v6)].MPC.values
            if len(val): print(f'    Q={q}, V6={v6}: {val[0]:.2f}%')
print()

# 3) High inoculum p0=0.01, best spray level (5-6 sprays)
print('=== HIGH INOCULUM p0=0.01, 5-6 SPRAYS ===')
for sprays in [5, 6]:
    hi_s = agg[(agg['Initial Probability']==0.01) & (agg['Sprays in May']==sprays)]
    print(f'  --- {sprays} sprays ---')
    for dem in ['high','moderate','low']:
        sub = hi_s[hi_s['Market Demand']==dem]
        print(f'  {dem}: min={sub.MPC.min():.2f}%, max={sub.MPC.max():.2f}%')
        for q in [0.2, 1.0]:
            for v6 in [0.0, 0.5, 1.0]:
                val = sub[(sub['Quantile']==q) & (sub['V6 Percent']==v6)].MPC.values
                if len(val): print(f'    Q={q}, V6={v6}: {val[0]:.2f}%')
print()

# 4) Moderate inoculum p0=0.005 and p0=0.001
print('=== MODERATE INOCULUM p0=0.005, 0 SPRAYS ===')
mod = agg[(agg['Initial Probability']==0.005) & (agg['Sprays in May']==0)]
for dem in ['high','moderate','low']:
    sub = mod[mod['Market Demand']==dem]
    print(f'  {dem}: min={sub.MPC.min():.2f}%, max={sub.MPC.max():.2f}%')
print()

print('=== MODERATE INOCULUM p0=0.001, 0 SPRAYS ===')
mod2 = agg[(agg['Initial Probability']==0.001) & (agg['Sprays in May']==0)]
for dem in ['high','moderate','low']:
    sub = mod2[mod2['Market Demand']==dem]
    print(f'  {dem}: min={sub.MPC.min():.2f}%, max={sub.MPC.max():.2f}%')
print()

# 5) Effect of V6 at high inoculum - show gradient
print('=== V6 EFFECT: p0=0.01, 0 sprays, Q=1.0 (highest centrality) ===')
v6eff = agg[(agg['Initial Probability']==0.01) & (agg['Sprays in May']==0) & (agg['Quantile']==1.0)]
for dem in ['high','moderate','low']:
    sub = v6eff[v6eff['Market Demand']==dem].sort_values('V6 Percent')
    print(f'  {dem}:')
    for _, r in sub.iterrows():
        print(f'    V6={r["V6 Percent"]:.2f}: {r.MPC:.2f}%')
print()

# 6) Centrality effect: p0=0.01, 0 sprays, V6=1.0
print('=== CENTRALITY EFFECT: p0=0.01, 0 sprays, V6=1.0 ===')
cent = agg[(agg['Initial Probability']==0.01) & (agg['Sprays in May']==0) & (agg['V6 Percent']==1.0)]
for dem in ['high','moderate','low']:
    sub = cent[cent['Market Demand']==dem].sort_values('Quantile')
    print(f'  {dem}:')
    for _, r in sub.iterrows():
        print(f'    Q={r.Quantile:.1f}: {r.MPC:.2f}%')
print()

# 7) Over-spraying cost: p0=1e-5, 10 sprays vs 0 sprays
print('=== OVER-SPRAYING: p0=1e-5, 10 sprays vs 0 sprays ===')
for dem in ['high','moderate','low']:
    v0 = agg[(agg['Initial Probability']==1e-5) & (agg['Sprays in May']==0) & (agg['Market Demand']==dem)]
    v10 = agg[(agg['Initial Probability']==1e-5) & (agg['Sprays in May']==10) & (agg['Market Demand']==dem)]
    print(f'  {dem}: 0-spray range={v0.MPC.min():.2f}% to {v0.MPC.max():.2f}%, 10-spray range={v10.MPC.min():.2f}% to {v10.MPC.max():.2f}%')
print()

# 8) Where does spraying break even / become detrimental at low p0?
print('=== SPRAY EFFECT AT LOW p0=1e-5, all V6, all Q ===')
lo_p0 = agg[agg['Initial Probability']==1e-5]
for dem in ['high','moderate','low']:
    sub = lo_p0[lo_p0['Market Demand']==dem]
    pivot = sub.groupby('Sprays in May').MPC.mean()
    print(f'  {dem}:')
    for s, v in pivot.items():
        print(f'    Sprays={s}: avg MPC={v:.3f}%')
print()

# 9) Optimal spray count at high p0 across demands
print('=== OPTIMAL SPRAYS at p0=0.01, V6=1.0, Q=1.0 ===')
opt = agg[(agg['Initial Probability']==0.01) & (agg['V6 Percent']==1.0) & (agg['Quantile']==1.0)]
for dem in ['high','moderate','low']:
    sub = opt[opt['Market Demand']==dem].sort_values('Sprays in May')
    best = sub.loc[sub.MPC.idxmax()]
    worst = sub.loc[sub.MPC.idxmin()]
    print(f'  {dem}: best={best["Sprays in May"]:.0f} sprays ({best.MPC:.2f}%), worst={worst["Sprays in May"]:.0f} sprays ({worst.MPC:.2f}%)')
    for _, r in sub.iterrows():
        print(f'    Sprays={r["Sprays in May"]:.0f}: {r.MPC:.2f}%')
