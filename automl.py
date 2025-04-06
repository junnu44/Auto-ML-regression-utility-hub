import streamlit as st
import pandas as pd
from ydata_profiling import ProfileReport
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from h2o.automl import H2OAutoML
import h2o


h2o.init()

st.title("AutoML Regression Utility Hub 🚀")


uploaded_file = st.file_uploader("Upload your dataset (CSV format)", type=["csv"])
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("### 🔍 Data Preview:")
    st.dataframe(df.head())

    
    profile = ProfileReport(df, explorative=True)
    st.write("### 📊 Data Profiling Report:")
    st.components.v1.html(profile.to_html(), height=1000, scrolling=True)

    
    target_column = st.selectbox("🎯 Select Target Variable", df.columns)

    if target_column:
        X = df.drop(columns=[target_column])
        y = df[target_column]

        
        df_h2o = h2o.H2OFrame(pd.concat([X, y], axis=1))
        predictors = X.columns.tolist()
        response = target_column

        
        splits = df_h2o.split_frame(ratios=[0.8], seed=42)
        train = splits[0]
        test = splits[1]

        if test.nrows == 0:
            st.error("🚫 Test set is empty. Please upload a larger dataset or reduce the split ratio.")
        else:
            st.write("### 🧠 Training AutoML Model...")
            model = H2OAutoML(max_models=20, seed=42)
            model.train(x=predictors, y=response, training_frame=train)

           
            preds = model.leader.predict(test)
            y_pred = preds.as_data_frame(use_pandas=True).values.flatten()
            y_test = test[response].as_data_frame(use_pandas=True).values.flatten()

            
            mae = mean_absolute_error(y_test, y_pred)
            mse = mean_squared_error(y_test, y_pred)
            r2 = r2_score(y_test, y_pred)

            st.write("### 📈 Model Performance:")
            st.write(f"**Mean Absolute Error:** {mae:.2f}")
            st.write(f"**Mean Squared Error:** {mse:.2f}")
            st.write(f"**R-squared Score:** {r2:.2f}")

            
            if st.button("💾 Download Trained Model"):
                model_path = h2o.save_model(model=model.leader, path="./", force=True)
                st.success(f"✅ Model saved to: {model_path}")
 s