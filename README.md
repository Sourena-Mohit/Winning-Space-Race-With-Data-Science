# Winning the Space Race With Data Science 
**IBM Data Science Capstone (SpaceX Falcon 9 Landing Prediction)**

This repository contains my completed work for the IBM Data Science Professional Certificate capstone project.  
The goal is to analyze SpaceX Falcon 9 launch records and build a classification model to predict whether the **first stage will land successfully**.

---

## Project Objectives
- Collect SpaceX launch data using **SpaceX REST API** and **web scraping**
- Clean and wrangle the dataset into a modeling-ready format
- Perform **EDA** using **visualization** and **SQL**
- Build interactive analytics with **Folium** and a **Plotly Dash** dashboard
- Train and evaluate multiple **classification models** to predict landing success
- Create a technical presentation in **PDF** format for peer review

---

## Repository Structure
```
Winning-Space-Race-With-Data-Science/
├── Module_1/
│   ├── jupyter-labs-spacex-data-collection-api.ipynb
│   ├── jupyter-labs-webscraping.ipynb
│   ├── labs-jupyter-spacex-Data wrangling.ipynb
│   ├── dataset_part_1.csv
│   ├── dataset_part_2.csv
│   └── spacex_web_scraped.csv
├── Module_2/
│   ├── edadataviz.ipynb
│   └── jupyter-labs-eda-sql-coursera_sqllite.ipynb
├── Module_3/
│   ├── lab_jupyter_launch_site_location.ipynb
│   └── Build an Interactive Dashboard with Plotly Dash.py
├── Module_4/
│   └── SpaceX_Machine Learning Prediction_Part_5.ipynb
└── README.md
```

> Folder/module names may vary slightly depending on Coursera lab exports, but all required notebooks and scripts are included.

---

## Datasets
Data was collected and prepared from:
- **SpaceX REST API** (launches, payloads, rockets, launchpads)
- **Wikipedia** tables (Falcon 9 launch records) via web scraping  
- IBM Skills Network course dataset: `spacex_launch_geo.csv` (used for the Folium lab)

Generated datasets (examples):
- `dataset_part_1.csv`, `dataset_part_2.csv`, `spacex_web_scraped.csv`

---

## Key Results (High Level)
- Success rate improves over time (experience / flight number effect).
- Success patterns vary by **orbit type**, **payload mass**, and **launch site**.
- Multiple classifiers (Logistic Regression, SVM, Decision Tree, KNN) achieved ~**0.83** test accuracy in the provided split.

---

## How to Run
### 1) Install dependencies
```bash
pip install pandas numpy matplotlib seaborn scikit-learn sqlalchemy folium dash plotly
```

### 2) Run notebooks
Open notebooks in JupyterLab / Jupyter Notebook and execute cells in order.

### 3) Run Plotly Dash app
From the repository folder:
```bash
python "Module_3/Build an Interactive Dashboard with Plotly Dash.py"
```
Then open the local Dash URL shown in the terminal (usually `http://127.0.0.1:8050/`).

---

## Notebooks / Deliverables
### Data Collection
- SpaceX API: `Module_1/jupyter-labs-spacex-data-collection-api.ipynb`
- Web Scraping: `Module_1/jupyter-labs-webscraping.ipynb`

### Data Wrangling
- Wrangling: `Module_1/labs-jupyter-spacex-Data wrangling.ipynb`

### EDA
- Visualization: `Module_2/edadataviz.ipynb`
- SQL: `Module_2/jupyter-labs-eda-sql-coursera_sqllite.ipynb`

### Interactive Analytics
- Folium map: `Module_3/lab_jupyter_launch_site_location.ipynb`
- Dash dashboard: `Module_3/Build an Interactive Dashboard with Plotly Dash.py`

### Predictive Analysis
- ML Classification: `Module_4/SpaceX_Machine Learning Prediction_Part_5.ipynb`

---

## Presentation
A final technical presentation was created and exported to **PDF** for peer review.

---

## Author
**Sourena Mohit Tabatabaie**  
GitHub: https://github.com/Sourena-Mohit

---
