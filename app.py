import pickle
# Load the model from the saved file
with open('model.pkl', 'rb') as file:
    loaded_model = pickle.load(file)

import streamlit as st
import pandas as pd

# Create the make_prediction function
def make_prediction(Title, NewlyBuilt, Furnished, Bedrooms, Toilets, City):
    data = {
        "Title": Title,
        "Newly Built": NewlyBuilt,
        "Furnished": Furnished,
        "Bedrooms": Bedrooms,
        "Toilets": Toilets,
        "City": City
    }
    df = pd.DataFrame(data, index=[0])
    prediction = loaded_model.predict(df).round(2)[0]
    return f"Predicted apartment price: ₦{prediction}"

# Streamlit app
def main():
  st.title("Apartment Price Prediction")
  # Input fields for user
  Title = st.selectbox("Title", X_train["Title"].unique())
  NewlyBuilt = st.checkbox("Newly Built")
  Furnished = st.checkbox("Furnished")
  Bedrooms = st.number_input("Bedrooms", min_value=1, max_value=10)
  Toilets = st.number_input("Toilets", min_value=1, max_value=10)
  City = st.selectbox("City", X_train["City"].unique())

  # Make prediction
  if st.button("Predict"):
      prediction = make_prediction(Title, NewlyBuilt, Furnished, Bedrooms, Toilets, City)
      st.write(prediction)

if __name__ == "__main__":
    main()
