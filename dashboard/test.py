import streamlit as st
import pandas as pd

st.title('Inflation Calculator')

form = st.form('calculator_form')
initial_amount = form.number_input('Enter initial amount', value=10000)
inflation_rate = form.number_input('Annual inflation rate (%)', value=7.0)
years = form.number_input('Number of years', value=10)
submit = form.form_submit_button('Calculate')

def calculate_inflation(initial_amount, inflation_rate, years):
    return initial_amount * (1 + inflation_rate / 100) ** years

if submit:
    future_value = calculate_inflation(initial_amount, inflation_rate, years)
    st.write("Future value: ", future_value)
    
    years_range = range(0, years + 1)
    future_values = [calculate_inflation(initial_amount, inflation_rate, year) for year in years_range]
    
    dataset = pd.DataFrame({
        'Year': years_range,
        'Future Value': future_values
    })
    
    st.line_chart(dataset.set_index('Year'))
