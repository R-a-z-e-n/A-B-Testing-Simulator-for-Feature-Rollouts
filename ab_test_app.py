!pip install streamlit
!streamlit run ab_test_app.py --server.port 8501 --server.headless true
# ============================================
# A/B Testing Simulator with Streamlit
# ============================================

# Install dependencies in Colab if needed
# !pip install streamlit statsmodels matplotlib seaborn

import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.stats.proportion import proportions_ztest, proportion_confint

# -----------------------------
# Helper Functions
# -----------------------------
def simulate_ab_test(n_users=10000, cr_control=0.10, cr_treatment=0.12):
    control = np.random.binomial(1, cr_control, n_users)
    treatment = np.random.binomial(1, cr_treatment, n_users)
    
    df = pd.DataFrame({
        "group": ["control"]*n_users + ["treatment"]*n_users,
        "converted": np.concatenate([control, treatment])
    })
    return df

def analyze_ab_test(df, n_users=10000):
    success = [
        df[df.group=="control"].converted.sum(),
        df[df.group=="treatment"].converted.sum()
    ]
    nobs = [n_users, n_users]
    
    # Z-test for proportions
    stat, pval = proportions_ztest(success, nobs)
    
    # Confidence intervals
    confint = [proportion_confint(s, n, method='normal') for s, n in zip(success, nobs)]
    
    # Conversion rates
    cr_control = success[0]/nobs[0]
    cr_treatment = success[1]/nobs[1]
    lift = (cr_treatment - cr_control) / cr_control
    
    return {
        "control_rate": cr_control,
        "treatment_rate": cr_treatment,
        "lift": lift,
        "p_value": pval,
        "confint": confint
    }

def summary_report(results):
    report = f"""
    === A/B Test Summary Report ===
    Control Conversion Rate: {results['control_rate']:.4f}
    Treatment Conversion Rate: {results['treatment_rate']:.4f}
    Lift: {results['lift']*100:.2f}%
    p-value: {results['p_value']:.4f}
    Confidence Intervals: {results['confint']}
    
    Recommendation: {"Roll out new feature" if results['p_value']<0.05 and results['lift']>0 else "Hold / Retest"}
    """
    return report

# -----------------------------
# Streamlit Interface
# -----------------------------
st.title("📊 A/B Testing Simulator for Feature Rollouts")
st.write("Simulate and analyze A/B tests for new product features.")

# User Inputs
n_users = st.slider("Number of users per group", 1000, 50000, 10000)
cr_control = st.number_input("Control conversion rate", 0.0, 1.0, 0.10)
cr_treatment = st.number_input("Treatment conversion rate", 0.0, 1.0, 0.12)

# Run Simulation
df = simulate_ab_test(n_users, cr_control, cr_treatment)
results = analyze_ab_test(df, n_users)

# Display Results
st.subheader("Results")
st.write("Control Conversion Rate:", round(results["control_rate"],4))
st.write("Treatment Conversion Rate:", round(results["treatment_rate"],4))
st.write("Lift:", f"{results['lift']*100:.2f}%")
st.write("p-value:", round(results["p_value"],4))
st.write("Confidence Intervals:", results["confint"])

# Visualization
st.subheader("Conversion Rate Comparison")
fig, ax = plt.subplots()
sns.barplot(x=["Control","Treatment"], 
            y=[results["control_rate"], results["treatment_rate"]], ax=ax)
ax.set_ylabel("Conversion Rate")
ax.set_title("Conversion Rates")
st.pyplot(fig)

# Case Study
st.subheader("Case Study: Checkout Flow")
if results["p_value"] < 0.05:
    if results["lift"] > 0:
        st.success("✅ Statistically significant improvement. Recommendation: Roll out new checkout flow.")
    else:
        st.error("❌ Statistically significant decline. Recommendation: Do NOT roll out.")
else:
    st.warning("⚠️ No statistically significant difference. Keep testing.")

# Summary Report
st.subheader("Summary Report")
st.text(summary_report(results))
