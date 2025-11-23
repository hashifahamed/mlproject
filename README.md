🎓 Student Math Score Prediction – End-to-End Machine Learning Project

This project is an end-to-end Machine Learning pipeline designed to predict the math score of students based on demographic and academic features. It includes data preprocessing, model training, model selection, evaluation, and deployment through a Flask web application.

📊 Project Overview

This ML system predicts a student's math score using the following features:

Gender

Race/Ethnicity

Parental Level of Education

Lunch Type

Test Preparation Course

Reading Score

Writing Score

The project follows a modular and production-ready architecture, making it easy to maintain, extend, and deploy.

🧠 Features of the Project
✔️ 1. Data Preprocessing

Handled missing values

Encoded categorical features

Scaled numerical columns

Built a reusable preprocessing pipeline using ColumnTransformer

✔️ 2. Model Training & Selection

Trained multiple ML models:

Linear Regression

Lasso/Ridge

Random Forest

Decision Tree

Gradient Boosting

XGBoost (if installed)

Compared models using performance metrics

Selected the best-performing model and saved it using pickle

✔️ 3. Modular ML Pipeline

Project contains fully modular components:

Data ingestion

Data transformation

Model trainer

Prediction pipeline

Logging & custom exception handling

Model persistence system

✔️ 4. Flask Web Application

User-friendly input form

Sends data to the backend pipeline

Returns math score prediction in real time

Simple UI for demonstration and testing

🏗️ Project Structure
├── artifacts/
│   ├── model.pkl
│   ├── preprocessor.pkl
├── notebook/
│   ├── EDA.ipynb
│   ├── Model_Training.ipynb
├── src/
│   ├── components/
│   │   ├── data_ingestion.py
│   │   ├── data_transformation.py
│   │   ├── model_trainer.py
│   ├── pipeline/
│   │   ├── predict_pipeline.py
│   ├── utils.py
│   ├── logger.py
│   ├── exception.py
├── templates/
│   ├── index.html
│   ├── home.html
├── app.py
├── requirements.txt
├── README.md

🛠️ Tech Stack

Python

Pandas, NumPy

Scikit-learn

Matplotlib/Seaborn (for EDA)

Flask

Pickle/Joblib

Git/GitHub

🚀 How to Run the Project
1. Clone the repository
git clone <your_repo_link>
cd <project_folder>

2. Create a virtual environment
python -m venv venv
venv\Scripts\activate  # Windows

3. Install dependencies
pip install -r requirements.txt

4. Run the Flask app
python app.py

5. Open in browser

Visit:

http://127.0.0.1:5000/

📈 Results

The selected ML model achieved strong performance on evaluation metrics.

Demonstrates how reading and writing scores significantly influence math performance.

Flask interface allows easy real-time prediction.

🌟 Key Learnings

Building end-to-end ML systems

Setting up a modular ML architecture

Hands-on experience with model deployment basics

Understanding data preprocessing and model evaluation techniques

Practical use of Flask for ML deployment

🤝 Contributions

Feel free to open issues or submit pull requests to enhance the project.  
