# Code for 'census_plots.py' file.
# Import necessary modules.
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
# Define a function 'app()' which accepts 'census_df' as an input.
def app(census_new):
    st.header("Visualise Data")
    st.set_option("deprecation.showPyplotGlobalUse", False)
    # Add a multiselect in the sidebar with label 'Select the Charts/Plots:'
    # Store the current value of this widget in a variable 'plot_list'.
    plot_list = st.sidebar.multiselect("Select the Charts/Plots:", ("Pie Chart", "Box Plot", "Count Plot"))
    # Display count plot using seaborn module and 'st.pyplot()' 
    if "Count Plot" in plot_list:
      st.subheader("Count Plot")
      plt.title(f"Count plot for unique workclass group")
      plt.figure(figsize = (12, 6))
      sns.countplot(x = df["workclass"], hue = df["income-group"])
      st.pyplot()
    # Display pie plot using matplotlib module and 'st.pyplot()'
    if "Pie Chart" in plot_list:
      st.subheader("Pie Chart")
      pie_feature = st.selectbox("Select a feature for your pie chart:", ("income","gender"))
      group_slices = df[pie_feature].value_counts()*100/df.shape[0]
      plt.figure(figsize=(20,10))
      plt.title(f"Distribution of records for different {pie_feature}s")
      plt.pie(census_df[pie_feature].value_counts())
      st.pyplot()
    # Display box plot using matplotlib module and 'st.pyplot()'
    if "Box Plot" in plot_list:
      st.subheader("Box Plot")
      box_plot_feature = st.selectbox("income-group", "gender")
      plt.title(f"Distribution of hours worked for different {box_plot_feature}s")
      plt.figure(figsize = (12, 6))
      sns.boxplot(x = census_df["hours-per-week"], y = census_df[box_plot_feature])
      st.pyplot()