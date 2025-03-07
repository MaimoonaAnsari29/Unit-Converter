import streamlit as st
from pint import UnitRegistry

# Initialize UnitRegistry for unit conversions
ureg = UnitRegistry()

# Set the title and description
st.set_page_config(page_title="Unit Converter", page_icon="🔄", layout="wide")
st.title("📏 Unit Converter")

# Custom CSS for styling with a nice background color and gradient
st.markdown("""
    <style>
        body {
            background: linear-gradient(135deg, #ff7e5f, #feb47b);  /* Gradient background from pink to orange */
            color: #333;
            font-family: 'Arial', sans-serif;
            margin: 0;
            padding: 0;
        }

        .main-box {
            background-color: #ffffff;  /* White background for the conversion box */
            border-radius: 15px;
            padding: 30px;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
            margin-top: 30px;
            width: 60%;  /* Set width to a fixed percentage */
            margin-left: auto;
            margin-right: auto;
        }

        h1 {
            text-align: center;
            font-size: 2.5rem;
            font-weight: bold;
            color: #ffffff;  /* White color for the title */
            margin-bottom: 20px;
        }

        .input-container {
            display: flex;
            flex-direction: column;
            gap: 15px;
        }

        .input-container select, .input-container input {
            padding: 12px;
            font-size: 16px;
            border-radius: 8px;
            border: 2px solid #ddd;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
            transition: border 0.3s ease;
        }

        .input-container select:focus, .input-container input:focus {
            border-color: #ff7e5f;  /* Color change on focus */
            outline: none;
        }

        .btn {
            background-color: #4CAF50;
            color: white;
            border: none;
            padding: 15px 30px;
            font-size: 16px;
            border-radius: 8px;
            cursor: pointer;
            transition: background-color 0.3s ease, transform 0.2s ease, box-shadow 0.3s ease;
            width: 100%;
            margin-top: 20px;
        }

        .btn:hover {
            background-color: #45a049;
            transform: scale(1.05);
            box-shadow: 0 6px 12px rgba(0, 0, 0, 0.1);
        }

        .btn:active {
            transform: scale(0.98);
            background-color: #3e8e41;
        }

        .footer {
            text-align: center;
            margin-top: 50px;
            font-size: 14px;
            color: #ddd;
        }
    </style>
""", unsafe_allow_html=True)

# Description with style
st.markdown("""
    **Welcome to the Unit Converter app!** 🌐✨  
    Convert between various units of measurement in an easy-to-use interface.  
    Enter the value, choose the units, and click **Convert** to see the result. 😎
""")

# Main content area inside a box
with st.container():
    st.markdown('<div class="main-box">', unsafe_allow_html=True)

    # Input fields for amount, from-unit, and to-unit
    st.subheader("🔄 Conversion Options")

    # Input for amount, unit selection
    amount = st.number_input("Amount", min_value=0.0, value=1.0, step=0.1, label_visibility="collapsed")
    from_unit = st.selectbox("From Unit", ["meter", "kilometer", "mile", "yard", "centimeter"])
    to_unit = st.selectbox("To Unit", ["meter", "kilometer", "mile", "yard", "centimeter"])

    # Conversion Result Display
    st.subheader("🔄 Conversion Result")

    # Convert button
    if st.button("Convert", key="convert"):
        try:
            # Convert the input value with selected units
            from_value = amount * ureg(from_unit)
            result = from_value.to(ureg(to_unit))

            # Display result
            st.success(f"✅ {amount} **{from_unit}** is equal to **{result.magnitude:.2f} {to_unit}**", icon="✅")
        
        except Exception as e:
            st.error(f"❌ Error: {e}", icon="🚨")
    
    st.markdown('</div>', unsafe_allow_html=True)

# Footer section
st.markdown("""
    <div class="footer">
        <p>Made with ❤️ by MAIMOONA ANSARI</p>
    </div>
""", unsafe_allow_html=True)








