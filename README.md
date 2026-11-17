# 🧠 Mental Health Risk & Prevalence Analytics Platform

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.25%2B-FF4B4B.svg)](https://streamlit.io/)
[![Plotly](https://img.shields.io/badge/Plotly-Interactive-3F4F75.svg)](https://plotly.com/)
[![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458.svg)](https://pandas.pydata.org/)
[![Scikit-Learn](https://img.shields.io/badge/scikit--learn-ML-F7931E.svg)](https://scikit-learn.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

> An end-to-end data analytics and interactive intelligence platform designed to analyze global mental illness prevalence, primary data coverage disparities, depressive symptom distributions, and disorder risk correlations across countries and demographics.

---

## 📑 Table of Contents
- [Project Overview](#-project-overview)
- [Key Features](#-key-features)
- [Datasets & Sources](#-datasets--sources)
- [Exploratory Data Analysis (EDA) Highlights](#-exploratory-data-analysis-eda-highlights)
- [Interactive Streamlit Dashboard](#-interactive-streamlit-dashboard)
- [Repository Structure](#-repository-structure)
- [Getting Started](#-getting-started)
- [Running the Applications](#-running-the-applications)
- [Tech Stack](#-tech-stack)
- [Project Documentation (PDF Report)](#-project-documentation-pdf-report)
- [License & Acknowledgments](#-license--acknowledgments)

---

## 🔍 Project Overview

Mental health disorders represent one of the leading global burdens of disease, yet epidemiologic coverage and clinical surveillance vary drastically across countries and socioeconomic groups.

This repository provides:
1. **In-depth Exploratory Data Analysis (EDA)** using Jupyter Notebook ([`mental-health-eda-prediction.ipynb`](mental-health-eda-prediction.ipynb)) covering 1990–2019 longitudinal trends, disorder comorbidity correlations, and outlier distributions.
2. **Interactive Streamlit Web Dashboard** ([`dashboard.py`](dashboard.py)) providing dynamic filtering, KPI summaries, global choropleths/bar charts, population coverage audits, and US symptom breakdowns.
3. **Comprehensive Technical Documentation** ([`Mental_Health_Risk_Prediction_Project_Report.pdf`](Mental_Health_Risk_Prediction_Project_Report.pdf)) detailing the mathematical definitions, methodology, statistical observations, and risk prediction frameworks.

---

## ⚡ Key Features

- **Multi-Disorder Prevalence Modeling**: Evaluates age-standardized prevalence rates for Schizophrenia, Major Depressive Disorder, Anxiety Disorders, Bipolar Disorder, and Eating Disorders across 200+ countries and territories.
- **Surveillance & Data Coverage Auditing**: Highlights the empirical research gap between high-income and low-to-middle-income countries in primary mental health surveillance.
- **Symptom Frequency Analysis**: Breaks down the temporal distribution of depressive symptoms (daily vs. intermittent) across demographics using US survey data.
- **Dynamic Interactive Dashboard**: Features country multi-selection, year slider/selector, real-time KPI metrics, Plotly interactive visualizations, and filtered CSV export capabilities.
- **Statistical Correlation Analysis**: Cross-analyzes co-occurrence patterns between severe disorders (e.g., strong mutual correlations between Anxiety and Depressive disorders).

---

## 📊 Datasets & Sources

The underlying datasets originate from the **Global Burden of Disease (GBD) Study** conducted by the Institute for Health Metrics and Evaluation (IHME) and curated by **Our World in Data (OWID)**.

| File Name | Description | Key Indicators / Columns |
|:---|:---|:---|
| `1- mental-illnesses-prevalence.csv` | Country-by-year standardized prevalence | Schizophrenia, Depression, Anxiety, Bipolar, Eating disorders (% of pop) |
| `2- burden-disease-from-each-mental-illness(1).csv` | Global disease burden & regional distribution | Regional aggregate prevalence for 22 global geographic divisions |
| `3- adult-population-covered-in-primary-data-on-the-prevalence-of-major-depression.csv` | Empirical primary research coverage | Share of adult population covered in direct observational studies |
| `4- adult-population-covered-in-primary-data-on-the-prevalence-of-mental-illnesses.csv` | Primary data coverage for all major disorders | Population coverage by disorder and country |
| `5- anxiety-disorders-treatment-gap.csv` | Clinical treatment & intervention gap | Proportion of diagnosed individuals receiving adequate medical care |
| `6- depressive-symptoms-across-us-population.csv` | Granular depressive symptoms frequency | Symptom categories (sleep, mood, self-esteem, appetite) by day frequency |
| `7- number-of-countries-with-primary-data-on-prevalence-of-mental-illnesses-in-the-global-burden-of-disease-study.csv` | Global surveillance completeness | Number of countries with primary epidemiological data by illness type |

---

## 📈 Exploratory Data Analysis (EDA) Highlights

### 1. Disorder Comorbidities & Heatmap Analysis
- **Depression & Anxiety**: Exhibit a high positive Pearson correlation ($r > 0.70$), demonstrating significant comorbidity across populations.
- **Eating & Bipolar Disorders**: Show distinct regional clusters, with higher documented rates in urbanized and high-income regions, reflecting both diagnostic infrastructure and demographic susceptibility.

### 2. Surveillance Disparity Findings
- Primary empirical data for severe conditions like Schizophrenia and Major Depression cover over 80% of populations in North America and Australasia, but drop to under 15% in parts of Central Sub-Saharan Africa and Andean Latin America.
- Machine learning risk models must adjust for surveillance bias when generalizing across regions.

### 3. Depressive Symptom Profiles
- Cognitive and affective symptoms ("depressed mood", "low energy", "loss of interest") dominate the "Nearly every day" bracket, serving as primary risk triggers for predictive screening.

---

## 🖥️ Interactive Streamlit Dashboard

The repository includes a ready-to-deploy Streamlit application:

```
┌────────────────────────────────────────────────────────┐
│ 🧠 Mental Health Analytics Dashboard                   │
├───────────────┬────────────────────────────────────────┤
│ 📂 Datasets   │ 📊 Overview KPIs                       │
│ • Prevalence  │ [Records: 6,468]  [Countries: 204]     │
│ • Coverage    │ [Year: 2019]      [Disorders: 5]       │
│ • Symptoms    ├────────────────────────────────────────┤
│               │ 📈 Highest Prevalence Comparisons      │
│ 🔎 Filters    │ [Horizontal Bar Charts - Plotly]       │
│ • Year Slider ├────────────────────────────────────────┤
│ • Country     │ 🌍 Global Trends Over Time (1990-2019) │
│   Multiselect │ [Multi-Line Chart with Hover Tooltips] │
└───────────────┴────────────────────────────────────────┘
```

- **Sidebar Controls**: Upload custom CSVs or automatically leverage pre-bundled datasets; filter by individual or multiple nations and historical years.
- **Real-Time KPIs**: Metrics tracking total sample size, geographical entity count, active time slice, and disorder dimensions.
- **Export Capabilities**: Clean, filtered data can be downloaded directly from the UI with one click.

---

## 📁 Repository Structure

```plaintext
mental-health-risk-prediction-/
│
├── archive/                                              # Dedicated dataset directory
│   ├── 1- mental-illnesses-prevalence.csv
│   ├── 2- burden-disease-from-each-mental-illness(1).csv
│   ├── 3- adult-population-covered-in-primary-data-on-the-prevalence-of-major-depression.csv
│   ├── 4- adult-population-covered-in-primary-data-on-the-prevalence-of-mental-illnesses.csv
│   ├── 5- anxiety-disorders-treatment-gap.csv
│   ├── 6- depressive-symptoms-across-us-population.csv
│   └── 7- number-of-countries-with-primary-data-on-prevalence-of-mental-illnesses-in-the-global-burden-of-disease-study.csv
│
├── dashboard.py                                         # Primary Streamlit web application
├── dashboard1.py                                        # Alternative Streamlit layout configuration
├── dashboard2.py                                        # Staged dashboard iteration
├── mental-health-eda-prediction.ipynb                   # Complete Jupyter EDA & modeling notebook
├── Mental_Health_Risk_Prediction_Project_Report.pdf     # Full technical documentation report (PDF)
├── requirements.txt                                     # Python dependencies
├── .gitignore                                           # Git exclusion rules
└── README.md                                            # Project documentation (this file)
```

---

## 🚀 Getting Started

### Prerequisites
- Python 3.9, 3.10, 3.11, 3.12, 3.13, or 3.14
- Git

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/vishesh-i-tech/mental-health-risk-prediction-.git
   cd mental-health-risk-prediction-
   ```

2. **Create and activate a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   # On Windows:
   .\venv\Scripts\activate
   # On Linux/macOS:
   source venv/bin/activate
   ```

3. **Install required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

---

## 💻 Running the Applications

### Launch the Streamlit Dashboard
To run the interactive web application:
```bash
python -m streamlit run dashboard.py
```
Then open your browser and navigate to `http://localhost:8501`.

### Run the Jupyter Notebook
To run the complete data exploration and statistical analysis:
```bash
jupyter notebook mental-health-eda-prediction.ipynb
```
*(Or open the `.ipynb` directly in VS Code with the Jupyter extension and select "Run All".)*

---

## 🛠️ Tech Stack

- **Core Analysis**: Python, NumPy, Pandas
- **Visualization**: Plotly Express & Graph Objects, Matplotlib, Seaborn
- **Machine Learning & Modeling**: Scikit-Learn
- **Web Dashboard**: Streamlit
- **Report Generation**: ReportLab, PyMuPDF

---

## 📄 Project Documentation (PDF Report)

A publication-grade technical report is included directly in the repository:
- 📖 **[`Mental_Health_Risk_Prediction_Project_Report.pdf`](Mental_Health_Risk_Prediction_Project_Report.pdf)**

It includes:
- Detailed statistical formulations and data dictionary
- High-resolution visual analysis breakdowns
- Surveillance coverage and bias assessment
- Predictive risk modeling framework and future clinical integration pathways

---

## 📜 License & Acknowledgments

- **License**: Released under the [MIT License](LICENSE).
- **Data Source**: Institute for Health Metrics and Evaluation (IHME), Global Burden of Disease (GBD) Study, and Our World in Data (OWID).
- **Author**: [vishesh-i-tech](https://github.com/vishesh-i-tech)
