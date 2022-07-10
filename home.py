# Show complete dataset and summary in 'census_home.py'
# Import necessary modules.
import numpy as np
import pandas as pd
import streamlit as st
# Define a function 'app()' which accepts 'census_df' as an input.
def app(census_df):
    st.header("View Data")
    # Display dataset within beta_expander.
    with st.beta_expander("View Dataset"):
        st.table(census_df)    
    # Show dataset summary on click of a checkbox.
    st.subheader("Columns Description:")
    if st.checkbox("Show summary"):
        st.table(census_df.describe())