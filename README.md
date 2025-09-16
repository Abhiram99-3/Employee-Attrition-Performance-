# Employee-Attrition-Performance
📌 Project Overview

This project predicts employee attrition — identifying employees at high risk of leaving the company. It is built using Python, Pandas, Scikit-learn, and Streamlit for an interactive web interface. The goal is to help HR departments proactively manage employee retention.

🔍 Features

The dataset contains 100+ employee records with the following features:

Feature	Description
EmployeeID	Unique identifier for each employee
Age	Age of the employee
Gender	Male/Female
Department	Employee department (IT, HR, Sales, Finance, R&D)
JobRole	Job title (Developer, Manager, Analyst, etc.)
Education	Education level (1–5)
YearsAtCompany	Years of experience in the company
MonthlyIncome	Monthly salary of the employee
JobSatisfaction	Job satisfaction level (1–4)
WorkLifeBalance	Work-life balance rating (1–4)
Overtime	Whether the employee works overtime (Yes/No)
NumCompaniesWorked	Number of previous companies
PerformanceRating	Performance rating (1–5)
Attrition	Target variable: Yes/No (whether employee left)
🛠 Tools and Technologies

Programming Language: Python

Libraries: Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn

Web App: Streamlit for interactive predictions

Modeling: Logistic Regression / Random Forest (or your model)

🚀 How to Run the Project
1. Clone the repository
git clone <your-repo-link>
cd <repo-folder>

2. Install dependencies
pip install -r requirements.txt

3. Run the Streamlit app
streamlit run employee.py

4. View the app

Open the URL provided in the terminal (usually http://localhost:8501)

Upload a CSV file or input employee details to get attrition predictions.

📈 Model Performance

Accuracy: 82%

Model predicts the likelihood of employee leaving based on their features.

Features like JobSatisfaction, Overtime, and YearsAtCompany are highly influential.

📂 Dataset

The sample dataset employee_attrition_sample.csv is included in the repository.

For real-world projects, you can use the IBM HR Analytics Employee Attrition dataset from Kaggle
.

📝 Future Improvements

Increase dataset size for better model accuracy.

Add more employee-related features (training, promotion history, feedback scores).

Implement advanced models like XGBoost or LightGBM.

Deploy the app on Heroku or Streamlit Cloud for public access.
