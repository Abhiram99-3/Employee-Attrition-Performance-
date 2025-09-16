# Employee-Attrition-Performance
📌 Overview

Predict which employees are at high risk of leaving the company using Python, Pandas, Scikit-learn, and Streamlit.
This tool helps HR teams make data-driven decisions to improve employee retention. ✨

#🔍 Features

Dataset includes 100+ employee records with:

Feature	Description
EmployeeID	Unique ID for each employee
Age	Employee age
Gender	Male/Female
Department	IT, HR, Sales, Finance, R&D
JobRole	Developer, Manager, Analyst, etc.
Education	Level (1–5)
YearsAtCompany	Experience in company
MonthlyIncome	Salary
JobSatisfaction	1–4 scale
WorkLifeBalance	1–4 scale
Overtime	Yes/No
NumCompaniesWorked	Previous companies
PerformanceRating	1–5 scale
Attrition	Target: Yes/No ✅
🛠 Tech Stack

Python 🐍

Libraries: Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn

Web App: Streamlit 🌐

Model: Logistic Regression / Random Forest 🌲

🚀 How to Run
# Clone repo
git clone <repo-link>
cd <repo-folder>

# Install dependencies
pip install -r requirements.txt

# Run Streamlit app
streamlit run employee.py


Open the URL in your terminal (http://localhost:8501)

Upload CSV or input employee details to get attrition predictions 📊

📈 Model Performance

Accuracy: 82% ✅

Key features influencing attrition: JobSatisfaction, Overtime, YearsAtCompany

📂 Dataset

Sample CSV: employee_attrition_sample.csv included

For real-world data: IBM HR Analytics Dataset (Kaggle)

📝 Future Improvements

Increase dataset size 📊

Add more features: training, promotions, feedback scores ✨

Use advanced models: XGBoost, LightGBM 💡

Deploy app online: Heroku / Streamlit Cloud 🌐



GitHub
