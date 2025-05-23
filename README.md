# Economic Policy Optimization for Regional Plant Disease Management: A Hop Powdery Mildew Case Study

This repository contains code and analysis for optimizing economic control strategies for aerially-dispersed plant pathogens at the regional scale, using hop powdery mildew as a case study.

## Overview

This project develops and implements a coupled epidemiological-economic model to simulate the impact of epidemic conditions and coordinated management interventions on profitability in agricultural systems. It aims to provide insights for agricultural stakeholders by modeling the economic impacts of plant disease and optimizing management strategies at a regional level. The findings can be interactively explored using the accompanying Streamlit application (`app.py`).

## Key Features

- **Network-based epidemiological modeling:** Simulates realistic disease spread dynamics.
- **Integrated economic analysis:** Assesses impacts on yield, quality, and overall profitability.
- **Flexible simulation framework:** Enables testing of diverse management interventions.
- **Scenario-based optimization:** Identifies optimal control strategies under various conditions (e.g., inoculum levels, pathogen diversity, market demand).

## Project Structure

- `app.py`: Interactive Streamlit application for visualizing simulation results.
- `data/`: Contains raw, processed, and simulation output data.
  - `data/raw/`: Original unprocessed data.
  - `data/processed/`: Cleaned and transformed data ready for analysis.
  - `data/processed/simulations/`: Output from simulation runs.
- `src/`: Python source code for models, simulation functions, and utility scripts.
- `notebooks/`: Jupyter notebooks detailing the analysis workflow:
  - `1-data-preprocessing.ipynb`: Data cleaning and preparation.
  - `2-mle.ipynb`: Maximum likelihood estimation of epidemiological model parameters.
  - `7-simulations.ipynb`: Core simulation experiments.
  - `13-visualization.ipynb`: Generation of static plots and result summaries.
- `reports/`: Research papers, figures, and other documentation.
  - `paper/`: Drafts and materials for the research manuscript.
- `requirements.txt`: Lists project dependencies.

## Key Findings

The project's analysis yields several key insights into optimal disease management strategies, considering factors like initial inoculum dose, pathogen diversity (e.g., V6-virulent strains), dispersal centrality within the grower network, and varying market conditions. Detailed findings and visualizations are available in the research paper and can be interactively explored using the Streamlit application.

## Requirements

- Python 3.x
- Project dependencies are listed in `requirements.txt`. Install them using:
  ```bash
  pip install -r requirements.txt
  ```
- Key dependencies include NumPy, SciPy, Pandas, Statsmodels, Plotly, and Streamlit.

## Usage

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/your-repository-name.git # TODO: Replace with actual URL
   cd your-repository-name
   ```
2. **Install dependencies:**
   Ensure you have Python 3.x installed. Then, install the project dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. **Explore the analysis via Jupyter Notebooks:**
   The `notebooks/` directory contains the detailed analysis workflow. It's recommended to run them in numerical order to follow the data processing and modeling steps. Start with `notebooks/1-data-preprocessing.ipynb`.
4. **Run the interactive Streamlit application:**
   To explore the simulation results interactively, run the Streamlit app:
   ```bash
   streamlit run app.py
   ```
5. **Consult the research paper:**
   For a detailed understanding of the methodology, model specifics, and in-depth discussion of results, please refer to the manuscript in `reports/paper/` (e.g., `paper.md` or `main.tex`).

## Citation

If you use this code or findings in your research, please cite:
TODO: Add appropriate citation details for the research paper once published or available as a preprint.
e.g., Pedro, J. F., et al. (Year). Title of Paper. *Journal/Conference*. Link/DOI

## License

This project is licensed under the terms of the TODO: Specify License Type (e.g., MIT License, Apache License 2.0).
See the `LICENSE` file for more details (TODO: Ensure a LICENSE file exists and is correctly referenced, or add the full license text here if a separate file is not used).

## Contact

For questions or collaboration, please contact:
Joshua F. Pedro ([joshfpedro@gmail.com](mailto:joshfpedro@gmail.com))
