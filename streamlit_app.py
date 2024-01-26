import streamlit

streamlit.title('My first Project')


import streamlit as st
import pandas as pd

# Sample data
data = {
    'SOIL_TYPE_ID': [1, 2, 3, 4, 5, 6, 7, 8],
    'SOIL_TYPE': ['Any', 'Loam', 'Clay', 'Sand', 'Silt', 'Loamy Sand', 'Clay Loam', 'Sandy Clay'],
    'SOIL_DESCRIPTION': [
        'Any of the other types.',
        'Sticky and gritty. Combination of sand, silt, and clay.',
        'Easily rolls into a ball and becomes shiny but not gritty.',
        "Doesn’t roll into a ball well, and feels gritty.",
        'Feels slippery and silky.',
        'Easily rolls into a ball but it falls apart easily.',
        'Easily rolls into a ball, but feels rough.',
        'Easily rolls into a ball, shiny when rubbed, but still gritty.'
    ]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Streamlit app
def main():
    st.title("Soil Types Table")
    st.table(df)

if __name__ == "__main__":
    main()

