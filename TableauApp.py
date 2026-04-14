import streamlit as st
import pandas as pd

# 1. Page Configuration
st.set_page_config(page_title="Mini-Tableau", layout="wide")

st.title("Mini-Tableau: Data Visualization and Analysis")
st.write("Upload a CSV, pick your axes, and generate interactive chart on the fly!")

# 2. Sidebar - File Uploader
st.sidebar.header("1. Upload Data")
uploaded_file = st.sidebar.file_uploader("Choose a CSV file", type="csv")
 # 3. Main Logic
if uploaded_file is not None:
     # Read the data
    df = pd.read_csv(uploaded_file)
    
    # Show a priview of the data
    st.subheader("Data Preview")
    st.dataframe(df.head(5))
    
    st.markdown("---")
    
    # 4. Side Bar - Chart build controls
    st.sidebar.header("2. Build Your Chart")
    
    # Get all cokumn names from uploaded fila
    columns = df.columns.tolist()
    
    # Let the user choose the chart Type, X- Axis, and Y-Axis
    chart_type = st.sidebar.selectbox("Select Chart Type",["Bar Chart", "Line Chart", "Scatter Plot"])
    x_axis = st.sidebar.selectbox("Choose X-Axis", columns)
    # Only allow numeric columns for Y-Axis
    numeric_columns = df.select_dtypes(include ="number").columns.tolist()
    y_axis = st.sidebar.selectbox("Choose Y-Axis", numeric_columns)
    
    st.subheader(f"{chart_type}: {y_axis} vs {x_axis}")
    
    # 5. Draw the Chart dynamically using a try/except block
    # (Just in case the user tries to do math on text columns!)
    try:
        if chart_type == "Scatter Plot":
            st.scatter_chart(data=df, x=x_axis, y=y_axis)
            
        elif chart_type == "Bar Chart":
            st.bar_chart(data=df, x=x_axis, y=y_axis)
            
        elif chart_type == "Line Chart":
            st.line_chart(data=df, x=x_axis, y=y_axis)
            
    except Exception as e:
        st.error(f"Error: {e}")
        
else:
    st.info("Please upload a csv file in the sidebar to begin.")
    
         
