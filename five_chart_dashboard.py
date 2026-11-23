import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Five Chart Types Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Five Essential Chart Types")
st.subheader("Data Visualization Dashboard")

st.markdown("""
**Name:** Raghav Chaudhary  
**Roll No.:** 2501201033  
**Course:** BCA (AI & DS)  
**University:** K.R. Mangalam University
""")

st.write("Dashboard based on five charts from the IBM Cognos Analytics reference PPT.")

tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "Bar Chart", "Column Chart", "Line Chart",
    "Pie Chart", "Scatter Chart"
])

# 1. BAR CHART
with tab1:
    st.header("1. Bar Chart")
    st.write("Horizontal bars compare values across categories.")

    df = pd.DataFrame({
        "Product": ["Product A", "Product B", "Product C", "Product D"],
        "Sales ($K)": [42, 58, 35, 66]
    })

    fig = px.bar(
        df, x="Sales ($K)", y="Product",
        orientation="h", color="Product",
        title="Product Sales Comparison",
        text="Sales ($K)"
    )
    st.plotly_chart(fig, use_container_width=True)
    st.dataframe(df, hide_index=True)

    st.success("Product D has the highest sales: $66K.")

# 2. COLUMN CHART
with tab2:
    st.header("2. Column Chart")
    st.write("Vertical columns compare values across categories.")

    df = pd.DataFrame({
        "Quarter": ["Q1", "Q2", "Q3", "Q4"],
        "Revenue ($K)": [120, 150, 135, 180]
    })

    fig = px.bar(
        df, x="Quarter", y="Revenue ($K)",
        color="Quarter", text="Revenue ($K)",
        title="Quarterly Revenue"
    )
    st.plotly_chart(fig, use_container_width=True)
    st.dataframe(df, hide_index=True)

    st.success("Q4 has the highest revenue: $180K.")

# 3. LINE CHART
with tab3:
    st.header("3. Line Chart")
    st.write("A continuous line shows the direction of change over time.")

    df = pd.DataFrame({
        "Day": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
        "Stock Price ($)": [102, 105, 101, 108, 112]
    })

    fig = px.line(
        df, x="Day", y="Stock Price ($)",
        markers=True, title="Stock Price Trend"
    )
    st.plotly_chart(fig, use_container_width=True)
    st.dataframe(df, hide_index=True)

    st.success("Stock price reaches $112 on Friday.")

# 4. PIE CHART
with tab4:
    st.header("4. Pie Chart")
    st.write("A circle divided into slices shows proportions of a whole.")

    df = pd.DataFrame({
        "Brand": ["Brand A", "Brand B", "Brand C", "Brand D"],
        "Market Share (%)": [35, 25, 20, 20]
    })

    fig = px.pie(
        df, names="Brand", values="Market Share (%)",
        title="Market Share by Brand"
    )
    fig.update_traces(textinfo="label+percent")
    st.plotly_chart(fig, use_container_width=True)
    st.dataframe(df, hide_index=True)

    st.success("Brand A has the largest market share: 35%.")

# 5. SCATTER CHART
with tab5:
    st.header("5. Scatter Chart")
    st.write("Unconnected points show the relationship between two numerical variables.")

    df = pd.DataFrame({
        "Advertising Spend": [10, 20, 30, 40, 50, 60],
        "Sales ($K)": [15, 18, 22, 20, 30, 28]
    })

    fig = px.scatter(
        df, x="Advertising Spend", y="Sales ($K)",
        title="Advertising Spend vs Sales"
    )
    st.plotly_chart(fig, use_container_width=True)
    st.dataframe(df, hide_index=True)

    st.success("The overall pattern suggests higher advertising spend is associated with higher sales.")

# DASHBOARD SUMMARY
st.divider()
st.header("Dashboard Summary")

c1, c2, c3, c4, c5 = st.columns(5)
c1.metric("Total Charts", "5")
c2.metric("Chart Families", "4")
c3.metric("Top Product", "Product D")
c4.metric("Best Quarter", "Q4")
c5.metric("Largest Share", "35%")

st.caption("Reference: 25 Essential Chart Types in IBM Cognos Analytics.")