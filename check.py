import streamlit as st
import yfinance as yf
import pandas as pd

# App title
st.title("📈 Interactive Stock Price Dashboard")

# Sidebar for user input
st.sidebar.header("Select Stock & Date Range")

# User selects stock symbol
ticker_symbol = st.sidebar.text_input("Enter Stock Symbol", "GOOGL")

# User selects date range
start_date = st.sidebar.date_input("Start Date", pd.to_datetime("2010-01-01"))
end_date = st.sidebar.date_input("End Date", pd.to_datetime("2023-12-31"))

# Fetch stock data
if ticker_symbol:
    try:
        ticker_data = yf.Ticker(ticker_symbol)
        stock_df = ticker_data.history(period="1d", start=start_date, end=end_date)

        # Display stock data
        st.subheader(f"Stock Data for {ticker_symbol}")
        st.line_chart(stock_df["Close"])
        st.line_chart(stock_df["Volume"])

        # Show raw data (optional)
        st.subheader("Raw Data")
        st.write(stock_df)

    except Exception as e:
        st.error(f"Error fetching data: {e}")

