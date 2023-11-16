# 34192025_Churning_Customers
This repository contains a machine learning model for predicting customer churn. The model is built using a neural network architecture implemented with Keras. The prediction app is developed using Streamlit, allowing users to input relevant features and obtain predictions regarding the likelihood of a customer churning.

# Customer Churn Prediction App

## Overview

This Streamlit app predicts customer churn based on a trained machine learning model. The model is built using Keras and is loaded from the 'best_model.h5' file. The app allows users to input various features related to a customer and get a prediction on whether the customer is likely to churn or not. Additionally, the app displays the confidence factor associated with the prediction.

## Functionalities

- User-friendly interface to input customer features.
- Real-time prediction of customer churn.
- Display of confidence factor for the prediction.
- Easy to use and understand.

## Usage

1. Install the necessary libraries by running:
    bash
    pip install streamlit joblib keras pandas
    

2. Run the Streamlit app using the following command:
    bash
    streamlit run app.py
    

3. Input the customer features through the user interface.

4. Click the "Predict" button to get the churn prediction and confidence factor.

## Files

- *app.py:* The main Streamlit application file.
- *best_model.h5:* Trained machine learning model for customer churn prediction.
- *scaler.pkl:* Scaler used for preprocessing input data.

## Dependencies

- Streamlit
- Joblib
- Keras
- Pandas

## Video Demo

For a quick demonstration, check out the video (insert_link_to_video).

