import streamlit as st
import pandas as pd
import os

# ── File paths ────────────────────────────────────
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, '..', 'data')
REPORTS_DIR = os.path.join(BASE_DIR, 'reports')

# ── Load data ─────────────────────────────────────
df = pd.read_csv(os.path.join(DATA_DIR, 'cleaned_data.csv'),
                 parse_dates=['InvoiceDate'])

# ── Page content ──────────────────────────────────
st.title("Business Overview")
st.write("Revenue trends and top products — 2009 to 2011")

st.header("Monthly Revenue Trend")
st.image(os.path.join(REPORTS_DIR, 'chart1_monthly_revenue.png'))

st.header("Top 10 Products by Revenue")
st.image(os.path.join(REPORTS_DIR, 'chart2_top_products.png'))

st.header("Revenue by Country")
st.image(os.path.join(REPORTS_DIR, 'chart3_country_revenue.png'))