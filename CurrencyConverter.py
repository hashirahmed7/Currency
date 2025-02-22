import streamlit as st

# Currency conversion rates (using hypothetical static values for now)
conversion_rates = {
    'INR': 24.20,  # Pakistani Rupees (PKR) to Indian Rupees (INR)
    'GBP': 0.0044,  # Pakistani Rupees (PKR) to British Pounds (GBP)
    'USD': 0.0067,  # Pakistani Rupees (PKR) to US Dollars (USD)
    'CNY': 0.046,   # Pakistani Rupees (PKR) to Chinese Yuan (CNY)
    'RUB': 0.506,   # Pakistani Rupees (PKR) to Russian Rubles (RUB)
}

# Function to convert PKR to selected currency
def convert_currency(amount, currency):
    return amount * conversion_rates[currency]

# Streamlit interface setup
st.title("Currency Converter")
st.markdown("""
    Welcome to the **Currency Converter** app! Convert Pakistani Rupees (PKR) into UK Pounds (GBP), Indian Rupees (INR), 
    US Dollars (USD), Chinese Yuan (CNY), and Russian Rubles (RUB). 
    Simply enter the amount of PKR you want to convert, and select the target currency.
""")

# User input for amount in PKR
amount_pkr = st.number_input("Enter amount in Pakistani Rupees (PKR):", min_value=1.0, step=1.0)

# Dropdown to select target currency
currency = st.selectbox("Select target currency:", ["INR", "GBP", "USD", "CNY", "RUB"])

# Perform conversion
converted_amount = convert_currency(amount_pkr, currency)

# Display the result
st.subheader(f"{amount_pkr} PKR is equal to {converted_amount:.2f} {currency}")

# Styling and layout adjustments
st.markdown("""
    <style>
    .stApp {
        background-color: #f0f0f5;
        padding: 20px;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        font-size: 18px;
        border-radius: 5px;
    }
    .stSelectbox select {
        font-size: 16px;
    }
    .stNumberInput input {
        font-size: 16px;
    }
    </style>
""", unsafe_allow_html=True)

# Optional: Add a currency symbol for better understanding
currency_symbols = {
    'INR': '₹',
    'GBP': '£',
    'USD': '$',
    'CNY': '¥',
    'RUB': '₽'
}

# Add a small feature to display the currency symbol next to the amount
st.markdown(f"Converted amount: **{currency_symbols[currency]}{converted_amount:.2f}**")
