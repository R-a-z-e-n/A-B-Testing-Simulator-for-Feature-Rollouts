
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
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the Streamlit App
```bash
streamlit run ab_test_app.py
```

### 4. Open in Browser
Streamlit will provide a local URL (default: `http://localhost:8501`) to interact with the app.

---

---

## 📊 Example Workflow
1. Set number of users and conversion rates for control & treatment groups.
2. Run simulation to generate synthetic experiment data.
3. View statistical results:
   - Conversion rates
   - Lift %
   - p-value
   - Confidence intervals
4. Visualize conversion comparison.
5. Read summary report with rollout recommendation.

---

## 📖 Case Study
**Question:** Did the new checkout flow improve conversion?  
- If **p-value < 0.05** and **lift > 0** → ✅ Roll out new feature.  
- If **p-value < 0.05** and **lift < 0** → ❌ Do not roll out.  
- If **p-value ≥ 0.05** → ⚠️ No statistically significant difference, keep testing.

---

## 📌 Deliverables
- Python notebook (Colab-ready).
- Streamlit app for interactive simulation.
- Statistical analysis outputs.
- Case study demonstration.
- Summary report for product team.

---

## 🧑‍💻 Contributors
- Mohammad Razeen Iqbal  
- Open-source community contributions welcome!

