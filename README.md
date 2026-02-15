# A-B-Testing-Simulator-for-Feature-Rollouts
Simulate and analyze A/B tests for new product features (e.g., UI changes, pricing models)
# 📊 A/B Testing Simulator for Feature Rollouts

## Overview
This project provides a hands-on simulator for running and analyzing **A/B tests** on product features such as UI changes, pricing models, or checkout flows.  
It helps product teams and analysts understand whether new features improve conversion rates using statistical rigor.

Built with **Python** and **Streamlit**, the tool allows interactive experimentation, statistical testing, and report generation.

---

## ✨ Features
- Simulate A/B test data for control vs. treatment groups.
- Statistical analysis:
  - Conversion rates
  - Lift calculations
  - p-values (two-proportion z-test)
  - Confidence intervals
- Interactive **Streamlit dashboard** with sliders and inputs.
- Visual comparison of conversion rates.
- Case study: *“Did the new checkout flow improve conversion?”*
- Automated summary report with recommendations.

---

## 🛠️ Tech Stack
- **Python 3.9+**
- **Streamlit** – interactive UI
- **Statsmodels** – statistical tests
- **NumPy / Pandas** – data simulation & manipulation
- **Matplotlib / Seaborn** – visualization

---

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/ab-testing-simulator.git
cd ab-testing-simulator
pip install -r requirements.txt
streamlit run ab_test_app.py
