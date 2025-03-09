import streamlit as st

def convert_length(value, from_unit, to_unit):
    length_units = {
        "Meters": 1,
        "Kilometers": 0.001,
        "Centimeters": 100,
        "Millimeters": 1000,
        "Inches": 39.3701,
        "Feet": 3.28084,
        "Yards": 1.09361,
        "Miles": 0.000621371
    }
    return value * (length_units[to_unit] / length_units[from_unit])

def convert_temperature(value, from_unit, to_unit):
    if from_unit == "Celsius" and to_unit == "Fahrenheit":
        return (value * 9/5) + 32
    elif from_unit == "Fahrenheit" and to_unit == "Celsius":
        return (value - 32) * 5/9
    elif from_unit == "Celsius" and to_unit == "Kelvin":
        return value + 273.15
    elif from_unit == "Kelvin" and to_unit == "Celsius":
        return value - 273.15
    elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
        return (value - 32) * 5/9 + 273.15
    elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
        return (value - 273.15) * 9/5 + 32
    return value  # If same unit is selected

st.title("Unit Converter App")

category = st.selectbox("Select Category", ["Length", "Temperature"])

if category == "Length":
    value = st.number_input("Enter value:", min_value=0.0, format="%.4f")
    from_unit = st.selectbox("From Unit", ["Meters", "Kilometers", "Centimeters", "Millimeters", "Inches", "Feet", "Yards", "Miles"])
    to_unit = st.selectbox("To Unit", ["Meters", "Kilometers", "Centimeters", "Millimeters", "Inches", "Feet", "Yards", "Miles"])
    
    if st.button("Convert"):
        result = convert_length(value, from_unit, to_unit)
        st.success(f"{value} {from_unit} is equal to {result:.4f} {to_unit}")

elif category == "Temperature":
    value = st.number_input("Enter value:", format="%.2f")
    from_unit = st.selectbox("From Unit", ["Celsius", "Fahrenheit", "Kelvin"])
    to_unit = st.selectbox("To Unit", ["Celsius", "Fahrenheit", "Kelvin"])
    
    if st.button("Convert"):
        result = convert_temperature(value, from_unit, to_unit)
        st.success(f"{value} {from_unit} is equal to {result:.2f} {to_unit}")
