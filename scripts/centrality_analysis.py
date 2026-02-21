import pandas as pd
import numpy as np

df = pd.read_parquet('data/processed/simulations/simulations_2_21_2026.parquet')

# Focus on 2014, p0=0.01, V6=1.0, 0 sprays - the worst-case scenario
print("="*80)
print("1. PROFIT LOSS BY QUANTILE: p0=0.01, V6=1.0, 0 sprays, high demand, 2014")
print("="*80)
sub = df[(df['Year']==2014) & (df['Initial Probability']==0.01) & 
         (df['V6 Percent']==1.0) & (df['Sprays in May']==0) & 
         (df['Market Demand']=='high')]
for q in sorted(sub['Quantile'].unique()):
    vals = sub[sub['Quantile']==q]['Mean Profit Percent Change']
    print(f"  Q={q:.1f}: mean={vals.mean():.2f}%, std={vals.std():.2f}%, median={vals.median():.2f}%")

print()
print("="*80)
print("2. PROFIT LOSS BY QUANTILE: p0=0.01, V6=1.0, 0 sprays, ALL demands, 2014")
print("="*80)
for demand in ['high', 'moderate', 'low']:
    print(f"\n  --- {demand.upper()} demand ---")
    sub = df[(df['Year']==2014) & (df['Initial Probability']==0.01) & 
             (df['V6 Percent']==1.0) & (df['Sprays in May']==0) & 
             (df['Market Demand']==demand)]
    for q in sorted(sub['Quantile'].unique()):
        vals = sub[sub['Quantile']==q]['Mean Profit Percent Change']
        print(f"    Q={q:.1f}: mean={vals.mean():.2f}%")

print()
print("="*80)
print("3. DISEASE INCIDENCE BY QUANTILE: p0=0.01, V6=1.0, 0 sprays, 2014")
print("="*80)
sub = df[(df['Year']==2014) & (df['Initial Probability']==0.01) & 
         (df['V6 Percent']==1.0) & (df['Sprays in May']==0) & 
         (df['Market Demand']=='high')]
for q in sorted(sub['Quantile'].unique()):
    vals = sub[sub['Quantile']==q]
    print(f"  Q={q:.1f}: May incid={vals['Disease Incidence May'].mean():.6f}, "
          f"Jun incid={vals['Disease Incidence June'].mean():.4f}, "
          f"Jul incid={vals['Disease Incidence July'].mean():.4f}")

print()
print("="*80)
print("4. PROFIT LOSS BY QUANTILE WITH V6=0: p0=0.01, 0 sprays, high demand, 2014")
print("="*80)
sub = df[(df['Year']==2014) & (df['Initial Probability']==0.01) & 
         (df['V6 Percent']==0.0) & (df['Sprays in May']==0) & 
         (df['Market Demand']=='high')]
for q in sorted(sub['Quantile'].unique()):
    vals = sub[sub['Quantile']==q]['Mean Profit Percent Change']
    print(f"  Q={q:.1f}: mean={vals.mean():.2f}%")

print()
print("="*80)
print("5. CENTRALITY EFFECT WITH OPTIMAL SPRAYS (5): p0=0.01, V6=1.0, high demand, 2014")
print("="*80)
sub = df[(df['Year']==2014) & (df['Initial Probability']==0.01) & 
         (df['V6 Percent']==1.0) & (df['Sprays in May']==5) & 
         (df['Market Demand']=='high')]
for q in sorted(sub['Quantile'].unique()):
    vals = sub[sub['Quantile']==q]['Mean Profit Percent Change']
    print(f"  Q={q:.1f}: mean={vals.mean():.2f}%")

print()
print("="*80)
print("6. CENTRALITY GAP: difference between Q=1.0 and Q=0.2 across spray levels")
print("   p0=0.01, V6=1.0, high demand, 2014")
print("="*80)
for spr in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    sub = df[(df['Year']==2014) & (df['Initial Probability']==0.01) & 
             (df['V6 Percent']==1.0) & (df['Sprays in May']==spr) & 
             (df['Market Demand']=='high')]
    q_low = sub[sub['Quantile']==0.2]['Mean Profit Percent Change'].mean()
    q_high = sub[sub['Quantile']==1.0]['Mean Profit Percent Change'].mean()
    gap = q_high - q_low
    print(f"  {spr} sprays: Q=0.2={q_low:.2f}%, Q=1.0={q_high:.2f}%, gap={gap:.2f}pp")

print()
print("="*80)
print("7. CENTRALITY EFFECT AT LOW INOCULUM: p0=1e-4, V6=1.0, 0 sprays, high demand, 2014")
print("="*80)
sub = df[(df['Year']==2014) & (df['Initial Probability']==0.0001) & 
         (df['V6 Percent']==1.0) & (df['Sprays in May']==0) & 
         (df['Market Demand']=='high')]
for q in sorted(sub['Quantile'].unique()):
    vals = sub[sub['Quantile']==q]['Mean Profit Percent Change']
    print(f"  Q={q:.1f}: mean={vals.mean():.2f}%")

print()
print("="*80)
print("8. SPRAYS RESPONSE BY QUANTILE: p0=0.01, V6=1.0, high demand, 2014")
print("   (landscape-level sprays in Jun/Jul)")
print("="*80)
for spr in [0, 3, 5, 10]:
    sub = df[(df['Year']==2014) & (df['Initial Probability']==0.01) & 
             (df['V6 Percent']==1.0) & (df['Sprays in May']==spr) & 
             (df['Market Demand']=='high')]
    for q in [0.2, 1.0]:
        vals = sub[sub['Quantile']==q]
        print(f"  {spr} sprays, Q={q:.1f}: jun_sprays={vals['Mean Sprays in June'].mean():.2f}, "
              f"jul_sprays={vals['Mean Sprays in July'].mean():.2f}, "
              f"late_sprays={vals['Mean Sprays in Late Season'].mean():.2f}")
    print()

print()
print("="*80)
print("9. QUANTILE EFFECT ACROSS V6 PROPORTIONS: p0=0.01, 0 sprays, high demand, 2014")
print("="*80)
for v6 in [0.0, 0.25, 0.5, 0.75, 1.0]:
    sub = df[(df['Year']==2014) & (df['Initial Probability']==0.01) & 
             (df['V6 Percent']==v6) & (df['Sprays in May']==0) & 
             (df['Market Demand']=='high')]
    q_low = sub[sub['Quantile']==0.2]['Mean Profit Percent Change'].mean()
    q_high = sub[sub['Quantile']==1.0]['Mean Profit Percent Change'].mean()
    gap = q_high - q_low
    print(f"  V6={v6:.0%}: Q=0.2={q_low:.2f}%, Q=1.0={q_high:.2f}%, gap={gap:.2f}pp")

print()
print("="*80)
print("10. CROSS-YEAR CENTRALITY EFFECT: p0=0.01, V6=1.0, 0 sprays, high demand")
print("="*80)
for yr in [2014, 2015, 2016, 2017]:
    sub = df[(df['Year']==yr) & (df['Initial Probability']==0.01) & 
             (df['V6 Percent']==1.0) & (df['Sprays in May']==0) & 
             (df['Market Demand']=='high')]
    q_low = sub[sub['Quantile']==0.2]['Mean Profit Percent Change'].mean()
    q_high = sub[sub['Quantile']==1.0]['Mean Profit Percent Change'].mean()
    gap = q_high - q_low
    print(f"  {yr}: Q=0.2={q_low:.2f}%, Q=1.0={q_high:.2f}%, gap={gap:.2f}pp")

print()
print("="*80)
print("11. FUNGICIDE COST BY QUANTILE: p0=0.01, V6=1.0, 0 sprays, high demand, 2014")
print("="*80)
sub = df[(df['Year']==2014) & (df['Initial Probability']==0.01) & 
         (df['V6 Percent']==1.0) & (df['Sprays in May']==0) & 
         (df['Market Demand']=='high')]
for q in sorted(sub['Quantile'].unique()):
    vals = sub[sub['Quantile']==q]
    print(f"  Q={q:.1f}: total_fung_cost={vals['Mean Fungicide Cost'].mean():.2f}, "
          f"baseline_fung_cost={vals['Mean Baseline Fungicide Cost'].mean():.2f}, "
          f"cone_color={vals['Mean Cone Color'].mean():.2f}, "
          f"cone_incid={vals['Mean Cone Incidence'].mean():.4f}")
