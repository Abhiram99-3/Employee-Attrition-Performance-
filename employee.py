# Employee Attrition Prediction - Streamlined Demo
import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import base64
import warnings
warnings.filterwarnings("ignore", message="missing ScriptRunContext")


st.title("📊 Employee Attrition Prediction")
st.write("Upload employee dataset to check attrition risk")

# File uploader
uploaded_file = st.file_uploader("Upload Employee Dataset (CSV)", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write("### Dataset Preview", df.head())

    # Preprocessing
    df_encoded = pd.get_dummies(df, drop_first=True)

    if "Attrition_Yes" in df_encoded.columns:
        X = df_encoded.drop("Attrition_Yes", axis=1)
        y = df_encoded["Attrition_Yes"]

        # Train-test split
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

        # Train model
        model = RandomForestClassifier(random_state=42)
        model.fit(X_train, y_train)

        # Predictions
        y_pred = model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)

        st.success(f"✅ Model Accuracy: {accuracy*100:.2f}%")

        # Find risky employees
        risky = df.loc[df_encoded["Attrition_Yes"] == 1, ["EmployeeNumber", "EmployeeName"]] \
                  if "EmployeeName" in df.columns else df.loc[df_encoded["Attrition_Yes"] == 1]

        st.write("### 🚨 Employees at Risk of Leaving")
        st.dataframe(risky)

        # Allow export to CSV
        risky_csv = risky.to_csv(index=False).encode()
        st.download_button("📥 Download Risky Employees List", risky_csv, "risky_employees.csv", "text/csv")

else:
    st.info("Please upload a CSV file to continue.")
