import streamlit as st
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
REPORTS_DIR = os.path.join(BASE_DIR, 'reports')

st.title("Sales Forecasting")
st.write("LSTM deep learning model trained on 2 years of daily sales")

# Model metrics
col1, col2 = st.columns(2)
col1.metric("Test RMSE", "£18,682")
col2.metric("Test MAE", "£10,729")

st.header("Actual vs Predicted Sales")
st.image(os.path.join(REPORTS_DIR, 'chart8_lstm_predictions.png'))

st.header("Training Loss Over Epochs")
st.image(os.path.join(REPORTS_DIR, 'chart_loss_history.png'))

st.write("""
**How the model works:**
- Looks back 30 days to predict the next day
- Trained on 80% of data, tested on 20%
- Architecture: LSTM(50) → Dropout(0.2) → Dense(1)
- Trained for 150 epochs
""")