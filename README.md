# 📊 Customer Churn Prediction

This project aims to predict customer churn using machine learning techniques. By analyzing historical customer data, the model identifies patterns that indicate whether a customer is likely to leave. This can help businesses take proactive measures to retain customers and reduce churn rates.

## 🚀 Live Demo

Experience the model in action:

[👉 Customer Churn Prediction App](https://customerchurnprediction-s4yrhysnpaxbfkuwztsip9.streamlit.app/)

## 🧠 Features

Machine Learning Model: Trained on customer data to classify churn likelihood.

User Interface: Built with Streamlit for easy interaction.

Real-time Predictions: Input customer data and get instant churn predictions.

## 📂 Project Structure
```
📁 Customer_Churn_Prediction
 ┣ 📄 app.py              # Streamlit application script
 ┣ 📄 requirements.txt    # Python dependencies
 ┣ 📄 WA_Fn-UseC_-Telco-Customer-Churn.csv  # Dataset of customer information
 ┣ 📄 customer_churn_model.pkl  # Trained machine learning model
 ┣ 📄 encoders.pkl         # Encoders for categorical features
 ┗ 📄 README.md           # Project documentation
```

## ⚙️ Installation & Setup
```
# Clone the repository
git clone https://github.com/abhinav744/Customer_Churn_Prediction.git
cd Customer_Churn_Prediction

# Create a virtual environment
python -m venv venv
source venv/bin/activate   # On macOS/Linux
venv\Scripts\activate      # On Windows

# Install dependencies
pip install -r requirements.txt

# Run the application
streamlit run app.py
```

## 📊 Dataset

The project utilizes the Telco Customer Churn dataset, which contains information on customers of a telecommunications company. The dataset includes features such as:

Customer demographics

Account information

Services subscribed to

Customer tenure

Churn label (1 = churned, 0 = stayed)

## 🧪 Model Details

Preprocessing: Data cleaning, feature engineering, and encoding of categorical variables.

Model Type: Machine learning model (Random Forest).

Evaluation: Model performance metrics (e.g., accuracy, precision, recall).

## 🌐 Usage

Launch the app with:
```
streamlit run app.py
```

Or use the live app directly:

[👉 Customer Churn Prediction App](https://customerchurnprediction-s4yrhysnpaxbfkuwztsip9.streamlit.app/)

Input customer data and get a Churn Prediction.
