import streamlit as st
import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, '..', 'data')
REPORTS_DIR = os.path.join(BASE_DIR, 'reports')

# Load RFM data
rfm = pd.read_csv(os.path.join(DATA_DIR, 'rfm_segments.csv'))

st.title("Customer Segmentation")
st.write("RFM-based customer segments using K-Means clustering")

# KPI metrics
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Customers", len(rfm))
col2.metric("Loyal", len(rfm[rfm['Segment']=='Loyal']))
col3.metric("At Risk", len(rfm[rfm['Segment']=='At Risk']))
col4.metric("Lost", len(rfm[rfm['Segment']=='Lost']))

# Segment chart
st.header("Customer Segments")
st.image(os.path.join(REPORTS_DIR, 'chart6_elbow.png'))

# Churn rate
churn_rate = (rfm['Recency'] > 90).mean() * 100
st.metric("Churn Rate", f"{churn_rate:.1f}%")

# Show RFM table
st.header("RFM Table")
st.dataframe(rfm[['Customer ID','Recency',
                   'Frequency','Monetary',
                   'Segment']].head(20))