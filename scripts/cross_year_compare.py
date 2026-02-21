import pandas as pd
df = pd.read_parquet('data/processed/simulations/simulations_2_21_2026.parquet')

for yr in [2014,2015,2016,2017]:
    agg = df[df['Year']==yr].groupby(['Market Demand','V6 Percent','Initial Probability','Sprays in May','Quantile'])['Mean Profit Percent Change'].mean().reset_index()
    agg.rename(columns={'Mean Profit Percent Change':'MPC'}, inplace=True)
    worst = agg[(agg['Initial Probability']==0.01)&(agg['Sprays in May']==0)&(agg['V6 Percent']==1.0)&(agg['Quantile']==1.0)&(agg['Market Demand']=='high')]
    best_row = agg[(agg['Initial Probability']==0.01)&(agg['V6 Percent']==1.0)&(agg['Quantile']==1.0)&(agg['Market Demand']=='high')]
    best = best_row.loc[best_row.MPC.idxmax()]
    gmin = agg.MPC.min()
    gmax = agg.MPC.max()
    wval = worst.MPC.values[0]
    bspr = int(best['Sprays in May'])
    bval = best.MPC
    print(f'{yr}: global=[{gmin:.2f}%, {gmax:.2f}%], worst(high,V6=1,Q=1,0spr)={wval:.2f}%, optimal={bspr}spr ({bval:.2f}%)')

# Also show the diminishing returns pattern for p0=0.01 high demand
print()
print('=== Spray response curve: p0=0.01, V6=1.0, Q=1.0, HIGH demand ===')
for yr in [2014,2015,2016,2017]:
    agg = df[df['Year']==yr].groupby(['Market Demand','V6 Percent','Initial Probability','Sprays in May','Quantile'])['Mean Profit Percent Change'].mean().reset_index()
    agg.rename(columns={'Mean Profit Percent Change':'MPC'}, inplace=True)
    sub = agg[(agg['Initial Probability']==0.01)&(agg['V6 Percent']==1.0)&(agg['Quantile']==1.0)&(agg['Market Demand']=='high')].sort_values('Sprays in May')
    print(f'{yr}: ', end='')
    vals = []
    for _, r in sub.iterrows():
        vals.append(f'{int(r["Sprays in May"])}:{r.MPC:.2f}')
    print(', '.join(vals))

# Check if any cell is positive
print()
for yr in [2014,2015,2016,2017]:
    agg = df[df['Year']==yr].groupby(['Market Demand','V6 Percent','Initial Probability','Sprays in May','Quantile'])['Mean Profit Percent Change'].mean().reset_index()
    pos = (agg['Mean Profit Percent Change'] > 0).sum()
    print(f'{yr}: positive cells = {pos}')
