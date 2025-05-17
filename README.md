# Policy Optimization for Plant Disease Management

This repository contains code and analysis for optimizing economic control strategies for aerially-dispersed plant pathogens at the regional scale, using hop powdery mildew as a case study.

## Overview

This project develops and implements a coupled epidemiological-economic model to simulate the impact of epidemic conditions and coordinated management interventions on profitability in agricultural systems. The model considers:

- Heterogeneity in pathogen transmission
- Effectiveness of control measures
- Host susceptibility and pathogen virulence
- Economic outcomes at regional scale
- Coordinated management strategies

## Key Features

- Network-based epidemiological model for disease spread
- Economic model incorporating yield and quality effects
- Simulation framework for testing management strategies
- Analysis of optimal control under varying conditions:
  - Initial inoculum dose
  - Pathogen diversity
  - Dispersal centrality
  - Market demand scenarios

## Project Structure

- `notebooks/`: Jupyter notebooks containing analysis and implementation
  - `1-data-preprocessing.ipynb`: Initial data cleaning and preparation
  - `2-mle.ipynb`: Maximum likelihood estimation of model parameters
  - `7-simulations.ipynb`: Simulation experiments
  - `8-fungicide-sprays.ipynb`: Analysis of fungicide application strategies
  - `13-visualization.ipynb`: Results visualization

- `reports/`: Documentation and research outputs
  - `paper/`: Manuscript and supplementary materials

## Key Findings

1. **Initial Inoculum Dose**
   - Low inoculum levels show minimal impact on profitability
   - Higher inoculum levels require more intensive management
   - Optimal spray strategies vary with inoculum pressure

2. **Pathogen Diversity**
   - V6-virulent strains require more intensive management
   - Strain composition affects optimal control strategies
   - Pathogen diversity influences economic outcomes

3. **Dispersal Centrality**
   - Central locations in the network have greater impact
   - Management strategies should consider network position
   - Early intervention critical in central locations

4. **Market Conditions**
   - Quality standards affect optimal management
   - Economic penalties vary with market demand
   - Control strategies adapt to market conditions

## Requirements

- Python 3.x
- Key dependencies:
  - NumPy
  - SciPy
  - Statsmodels
  - Jupyter

## Usage

1. Clone the repository
2. Install dependencies
3. Run notebooks in sequence for analysis
4. See paper.md for detailed methodology and results

## Citation

If you use this code in your research, please cite:
[Paper citation to be added]

## License

[License information to be added]

## Contact

For questions or collaboration, please contact:
Joshua F. Pedro (joshfpedro@gmail.com)
 
