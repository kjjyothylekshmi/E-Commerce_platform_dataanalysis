import streamlit as st

# ── Sidebar ───────────────────────────────────────
st.sidebar.title("E-Commerce Analytics")
st.sidebar.write("By: Jyothylekshmi KJ")
st.sidebar.markdown("---")
st.sidebar.write("Navigate using the pages below")

# ── Main page ─────────────────────────────────────
st.title("E-Commerce Analytics Platform")
st.write("Built from 1M+ real transactions — UCI Online Retail II Dataset")

# ── KPI cards ─────────────────────────────────────
col1, col2, col3 = st.columns(3)

col1.metric("Total Customers", "5,878")
col2.metric("Clean Transactions", "779,425")
col3.metric("Countries", "43")