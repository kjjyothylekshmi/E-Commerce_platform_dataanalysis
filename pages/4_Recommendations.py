import streamlit as st
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, '..', 'data')

st.title("Product Recommendations")
st.write("Collaborative filtering — based on similar customer purchases")

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv(os.path.join(DATA_DIR, 'cleaned_data.csv'),
                     parse_dates=['InvoiceDate'])
    return df

@st.cache_data
def build_matrix(df):
    matrix = df.pivot_table(
        index='Customer ID',
        columns='StockCode',
        values='Quantity',
        aggfunc='sum',
        fill_value=0
    )
    similarity = cosine_similarity(matrix)
    return matrix, similarity

df = load_data()
matrix, similarity = build_matrix(df)

def get_recommendations(customer_id, n=5):
    if customer_id not in matrix.index:
        return []
    idx = matrix.index.get_loc(customer_id)
    sim_scores = similarity[idx]
    similar = np.argsort(sim_scores)[::-1][1:11]
    recommended = set()
    for i in similar:
        bought = matrix.iloc[i]
        products = bought[bought > 0].index.tolist()
        recommended.update(products)
    already = matrix.loc[customer_id]
    already = already[already > 0].index.tolist()
    recs = [p for p in recommended if p not in already]
    return recs[:n]

def get_name(code):
    names = df[df['StockCode'] == code]['Description']
    return names.iloc[0] if len(names) > 0 else 'Unknown'

# ── Interactive input ─────────────────────────────
st.header("Get Recommendations")
customer_id = st.number_input("Enter Customer ID",
                               min_value=1,
                               value=12347,
                               step=1)
if st.button("Get Recommendations"):
    recs = get_recommendations(int(customer_id))
    if recs:
        st.success(f"Top {len(recs)} recommendations:")
        for i, code in enumerate(recs, 1):
            st.write(f"**{i}.** {code} — {get_name(code)}")
    else:
        st.warning("Customer not found or no recommendations available")
