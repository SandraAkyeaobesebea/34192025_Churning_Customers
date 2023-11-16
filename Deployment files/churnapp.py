# Streamlit App (app.py)
import streamlit as st
import joblib 
from keras.models import load_model
import pandas as pd

# Load the trained model and scaler
model = load_model('best_model.h5') 
scaler = joblib.load('scaler.pkl')  

# Streamlit App
def main():
    st.title("Customer Churn Prediction App")

    # Collect user input
    st.header("User Input Features")

    # Collect user input for each feature
    senior_citizen = st.selectbox("Senior Citizen", [0, 1])
    partner = 1 if st.selectbox("Partner", ["No", "Yes"]) == "Yes" else 0
    dependents = 1 if st.selectbox("Dependents", ["No", "Yes"]) == "Yes" else 0
    tenure = st.slider("Tenure", 0, 72, 0)

    # Handling MultipleLines as a categorical variable
    multiple_lines_map = {'No phone service': 0, 'No': 1, 'Yes': 2}
    multiple_lines = multiple_lines_map[st.selectbox("Multiple Lines", ["No phone service", "No", "Yes"])]

    internet_service = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
    online_security = 1 if st.selectbox("Online Security", ["No", "Yes"]) == "Yes" else 0
    online_backup = 1 if st.selectbox("Online Backup", ["No", "Yes"]) == "Yes" else 0
    device_protection = 1 if st.selectbox("Device Protection", ["No", "Yes"]) == "Yes" else 0
    tech_support = 1 if st.selectbox("Tech Support", ["No", "Yes"]) == "Yes" else 0
    streaming_tv = 1 if st.selectbox("Streaming TV", ["No", "Yes"]) == "Yes" else 0
    streaming_movies = 1 if st.selectbox("Streaming Movies", ["No", "Yes"]) == "Yes" else 0
    contract_map = {'Month-to-month': 0, 'One year': 1, 'Two year': 2}
    contract = contract_map[st.selectbox("Contract", ["Month-to-month", "One year", "Two year"])]
    paperless_billing = 1 if st.selectbox("Paperless Billing", ["No", "Yes"]) == "Yes" else 0
    payment_method_map = {'Electronic check': 0, 'Mailed check': 1, 'Bank transfer (automatic)': 2, 'Credit card (automatic)': 3}
    payment_method = payment_method_map[st.selectbox("Payment Method", ["Electronic check", "Mailed check", "Bank transfer (automatic)", "Credit card (automatic)"])]
    monthly_charges = st.slider("Monthly Charges", 0.0, 300.0, 0.0)
    total_charges = st.slider("Total Charges", 0.0, 10000.0, 0.0)

    # Convert categorical values to numerical values
    internet_service_map = {'DSL': 0, 'Fiber optic': 1, 'No': 2}
    internet_service = internet_service_map[internet_service]

    # Combine user input into a DataFrame
    user_input = pd.DataFrame({
        'SeniorCitizen': [senior_citizen],
        'Partner': [partner],
        'Dependents': [dependents],
        'tenure': [tenure],
        'MultipleLines': [multiple_lines],
        'InternetService': [internet_service],
        'OnlineSecurity': [online_security],
        'OnlineBackup': [online_backup],
        'DeviceProtection': [device_protection],
        'TechSupport': [tech_support],
        'StreamingTV': [streaming_tv],
        'StreamingMovies': [streaming_movies],
        'Contract': [contract],
        'PaperlessBilling': [paperless_billing],
        'PaymentMethod': [payment_method],
        'MonthlyCharges': [monthly_charges],
        'TotalCharges': [total_charges]
    })

      # "Predict" button
    if st.button("Predict"):
        # Preprocess the input data
        processed_input = scaler.transform(user_input)

        # Make predictions
        prediction = model.predict(processed_input)

        # Print the confidence factor
        confidence_factor = prediction[0][0]  # Assuming the prediction is a probability

        st.subheader("Prediction and Confidence Factor")
        st.write("Churn: {}".format("Customer is likely to churn" if confidence_factor >= 0.5 else "Customer is not likely to churn"))
        st.write("Confidence Factor: {:.2%}".format(confidence_factor))

if __name__ == '__main__':
    main()
