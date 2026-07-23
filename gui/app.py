import streamlit as st
import requests

API_URL = "http://payment-service:8088/payment"

st.title("💳 Payment Application")

menu = st.sidebar.selectbox(
    "Select Operation",
    ["Status", "Initiate Payment"]
)

if menu == "Status":
    if st.button("Check API"):
        try:
            r = requests.get(API_URL + "/status")
            st.success(r.text)
        except Exception as e:
            st.error(e)

elif menu == "Initiate Payment":

    card_number = st.text_input("Card Number")
    cvv = st.text_input("CVV", type="password")
    amount = st.number_input("Amount", min_value=1.0)
    card_type = st.selectbox(
        "Card Type",
        ["VISA", "MASTER", "RUPAY"]
    )

    if st.button("Pay"):

        payload = {
            "cardNumber": card_number,
            "cvv": cvv,
            "amount": amount,
            "cardType": card_type
        }

        try:
            response = requests.post(
                API_URL + "/initiate",
                json=payload
            )

            st.write(response.status_code)
            st.json(response.json())

        except Exception as e:
            st.error(e)
