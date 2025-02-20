import streamlit as st
import pandas as pd

# setup page 
st.set_page_config(page_title="Finance Tracker", layout="wide")

# Initialize session state for storing transactions
if 'transactions' not in st.session_state:
    st.session_state.transactions = pd.DataFrame(columns=['Date', 'Category', 'Amount', 'Type'])

# App Title
st.title("💰 Personal Finance Tracker")

# User Input
st.sidebar.header("Add Transaction")
date = st.sidebar.date_input("Select Date")
category = st.sidebar.selectbox("Category", ["Food", "Rent", "Shopping", "Bills", "Others"])
amount = st.sidebar.number_input("Amount", min_value=0.0, format="%.2f")
type_ = st.sidebar.radio("Type", ["Income", "Expense"])

if st.sidebar.button("Add Transaction"):
    new_data = pd.DataFrame([[date, category, amount, type_]], columns=['Date', 'Category', 'Amount', 'Type'])
    st.session_state.transactions = pd.concat([st.session_state.transactions, new_data], ignore_index=True)
    st.sidebar.success("Transaction Added!")

# Show Data
st.subheader("📊 Transactions History")
st.dataframe(st.session_state.transactions)

# Summary & Charts
st.subheader("📈 Financial Overview")
if not st.session_state.transactions.empty:
    total_income = st.session_state.transactions[st.session_state.transactions['Type'] == 'Income']['Amount'].sum()
    total_expense = st.session_state.transactions[st.session_state.transactions['Type'] == 'Expense']['Amount'].sum()
    balance = total_income - total_expense
    
    st.metric("Total Income", f"$ {total_income:.2f}")
    st.metric("Total Expense", f"$ {total_expense:.2f}")
    st.metric("Balance", f"$ {balance:.2f}")
