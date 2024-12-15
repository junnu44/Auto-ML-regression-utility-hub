import streamlit as st
import pandas as pd
import pandas_profiling
from streamlit_pandas_profiling import st_profile_report
from pycaret.regression import setup, compare_models, pull, save_model

# Title and header
st.title("AutoML Regression Utility Hub")
st.header("Automated Regression Analysis Made Easy")

# Step 1: Upload Dataset
st.subheader("1. Upload Your Dataset")
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file:
    try:
        df = pd.read_csv(uploaded_file)
        st.write("Preview of the Dataset", df.head())
    except Exception as e:
        st.error(f"Error reading the file: {e}")

    # Step 2: Exploratory Data Analysis (EDA)
    st.subheader("2. Exploratory Data Analysis (EDA)")
    if st.button("Generate EDA Report"):
        profile = pandas_profiling.ProfileReport(df)
        st_profile_report(profile)

    # Step 3: Run AutoML
    st.subheader("3. Run AutoML")
    target = st.selectbox("Select Target Column", df.columns)

    if st.button("Start AutoML"):
        try:
            # Setup the PyCaret environment
            setup(data=df, target=target, silent=True, session_id=123)
            best_model = compare_models()
            st.write("Best Model:", best_model)

            # Display evaluation metrics
            metrics = pull()
            st.write("Model Evaluation Metrics:")
            st.dataframe(metrics)

            # Save the best model
            if st.button("Save Best Model"):
                save_model(best_model, "best_regression_model")
                st.success("Model saved as 'best_regression_model.pkl'!")
        except Exception as e:
            st.error(f"Error during AutoML process: {e}")