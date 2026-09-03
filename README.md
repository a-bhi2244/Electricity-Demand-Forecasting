# Electricity Demand Forecasting Using Machine Learning
Electricity demand forecasting is an important application of machine learning that helps predict future electricity consumption based on historical patterns and external factors. Accurate demand forecasting can help electricity providers and organizations plan power generation, manage resources efficiently, reduce operational costs, and avoid electricity shortages.

This project uses historical electricity demand data along with features such as Temperature, Humidity, Hour, Day of Week, Month, Year, Day of Year, Week of Year, Quarter, Weekend information, previous demand values, and rolling statistics.

The project performs data preprocessing by handling missing values and converting timestamps into a proper datetime format. Feature engineering is then applied to extract useful time-based features and historical demand patterns. Important lag features, including demand from the previous 24 hours and previous 168 hours (one week), are created. Rolling mean and rolling standard deviation features are also generated to capture recent electricity demand trends.

The dataset is divided into training and testing data based on time. Data up to December 31, 2023 is used for training, while data from January 1, 2024 onwards is used for testing.

The project uses the XGBoost Regressor machine learning algorithm to forecast electricity demand. The model is evaluated using Root Mean Squared Error (RMSE) and Mean Absolute Error (MAE). Finally, actual and predicted electricity demand values are visualized using graphs, and the trained model is saved using Joblib for future predictions.

# Main Objective
To develop a machine learning model that can accurately predict future electricity demand using historical electricity consumption, weather conditions, time-based features, and previous demand patterns.

# Key Features
Historical electricity demand analysis
Missing value handling
Timestamp preprocessing
Temperature and humidity analysis
Time-based feature engineering
Weekend detection
Lag features for previous demand
24-hour rolling mean
24-hour rolling standard deviation
Exploratory Data Analysis (EDA)
Correlation analysis
XGBoost machine learning model
RMSE and MAE evaluation
Actual vs Predicted visualization
Saved trained model for future predictions

# Recommended Folder Structure
Electricity-Demand-Forecasting/
│
├── data/
│   ├── raw/
│   │   └── Electricity_Demand_Dataset.csv
│   │
│   └── processed/
│       └── processed_electricity_data.csv
│
├── notebooks/
│   └── Electricity_Demand_Forecasting.ipynb
│
├── src/
│   ├── __init__.py
│   │
│   ├── data_preprocessing.py
│   │
│   ├── feature_engineering.py
│   │
│   ├── train_model.py
│   │
│   ├── evaluate_model.py
│   │
│   └── predict.py
│
├── models/
│   └── electricity_demand_xgb_model.pkl
│
├── outputs/
│   ├── plots/
│   │   ├── electricity_demand_over_time.png
│   │   ├── demand_by_hour.png
│   │   ├── demand_by_month.png
│   │   ├── temperature_vs_demand.png
│   │   ├── correlation_heatmap.png
│   │   └── actual_vs_predicted.png
│   │
│   └── metrics/
│       └── model_performance.txt
│
├── app/
│   └── app.py
│
├── requirements.txt
│
├── README.md
│
└── main.py

# Recommended Project Architecture
Raw Dataset
     │
     ▼
Data Preprocessing
     │
     ├── Missing Value Handling
     ├── Timestamp Conversion
     └── Data Cleaning
     │
     ▼
Feature Engineering
     │
     ├── Hour
     ├── Day of Week
     ├── Month
     ├── Quarter
     ├── Weekend
     ├── Lag 24 Hours
     ├── Lag 168 Hours
     ├── Rolling Mean
     └── Rolling Standard Deviation
     │
     ▼
Exploratory Data Analysis
     │
     ▼
Train/Test Split
     │
     ▼
XGBoost Model Training
     │
     ▼
Model Evaluation
     │
     ├── RMSE
     └── MAE
     │
     ▼
Actual vs Predicted Visualization
     │
     ▼
Save Trained Model
     │
     ▼
Future Electricity Demand Prediction
