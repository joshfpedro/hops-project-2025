import pandas as pd
import numpy as np

df = pd.read_parquet('data/processed/simulations/simulations_2_21_2026.parquet')

# Severe conditions: p0=0.01, 100% V6, high demand, 2014
sub = df[(df['Initial Probability']==0.01) & (df['V6 Percent']==1.0) & (df['Market Demand']=='high') & (df['Year']==2014)]

print("Rows:", len(sub))
print("Quantiles:", sorted(sub['Quantile'].unique()))
print("Sprays in May values:", sorted(sub['Sprays in May'].unique()))
print()

# For each centrality quantile, find the optimal number of May sprays
for q in sorted(sub['Quantile'].unique()):
    q_data = sub[sub['Quantile']==q]
    by_spray = q_data.groupby('Sprays in May')['Mean Profit Percent Change'].mean()
    optimal = by_spray.idxmax()
    optimal_profit = by_spray.max()
    print(f"Q{q}: optimal May sprays = {int(optimal)}, best profit = {optimal_profit:.2f}%")

print()

q1_data = sub[sub['Quantile']==0.2]
q5_data = sub[sub['Quantile']==1.0]
by_spray_q1 = q1_data.groupby('Sprays in May')['Mean Profit Percent Change'].mean()
by_spray_q5 = q5_data.groupby('Sprays in May')['Mean Profit Percent Change'].mean()

q1_opt = by_spray_q1.idxmax()
q5_opt = by_spray_q5.idxmax()
print(f"Q1 optimal: {int(q1_opt)} sprays -> {by_spray_q1.max():.2f}%")
print(f"Q5 optimal: {int(q5_opt)} sprays -> {by_spray_q5.max():.2f}%")
print(f"Difference in optimal sprays: {int(q5_opt - q1_opt)}")
print()

print("Q1 spray profile:")
for s in sorted(by_spray_q1.index):
    print(f"  {int(s)} sprays: {by_spray_q1[s]:.3f}%")
print()
print("Q5 spray profile:")
for s in sorted(by_spray_q5.index):
    print(f"  {int(s)} sprays: {by_spray_q5[s]:.3f}%")

# Also check: what spray count at Q5 achieves a profit similar to Q1 optimal?
q1_best = by_spray_q1.max()
print(f"\nQ1 best profit: {q1_best:.3f}%")
print("Q5 sprays needed to match Q1 best profit:")
for s in sorted(by_spray_q5.index):
    if by_spray_q5[s] >= q1_best:
        print(f"  {int(s)} sprays: {by_spray_q5[s]:.3f}% (matches or exceeds Q1 best)")
        break
else:
    print("  Q5 never reaches Q1 best profit")
    closest = (by_spray_q5 - q1_best).abs().idxmin()
    print(f"  Closest: {int(closest)} sprays -> {by_spray_q5[closest]:.3f}%")
