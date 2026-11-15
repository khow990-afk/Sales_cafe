import streamlit as st
import pandas as pd

st.title("Qahwa Corner - Sales Dashboard")
st.markdown("Cloud Computing for Data Science - Assignment 1")

@st.cache_data
def load_data():
    df = pd.read_csv('cafe_sales.csv')
    df['total_sar'] = df['unit_price'] * df['quantity']
    return df

try:
    df = load_data()
except Exception as e:
    st.error(f"Error loading cafe_sales.csv: {e}")
    st.stop()

# Branch selector
branch_list = ['All'] + sorted(df['branch'].unique().tolist())
selected_branch = st.selectbox('Select Branch', branch_list)

if selected_branch != 'All':
    filtered_df = df[df['branch'] == selected_branch]
else:
    filtered_df = df

# Total-revenue metric
total_rev = filtered_df['total_sar'].sum()
st.metric(label="Total Revenue (SAR)", value=f"{total_rev:,.2f} SAR")

# Bar chart of revenue by product
st.subheader("Revenue by Product")
product_revenue = filtered_df.groupby('product')['total_sar'].sum()
st.bar_chart(product_revenue)

if st.checkbox("Show Filtered Dataset"):
    st.dataframe(filtered_df)
