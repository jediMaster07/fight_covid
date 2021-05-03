import pandas as pd
import streamlit as st

st.title("Fight CoVID - Resources!")
st.write("For any updates/corrections/suggestions, please reach out to: ")
st.markdown("***")

choice = st.radio("Select the resource you need:", ("List of available beds", "Oxygen resources", "Remdevisir"))

if choice == "List of available beds":
    df = pd.read_excel(r"Resources/beds.xlsx")
    df = df.fillna("[Not Verified]")
    st.table(df)
    
elif choice == "Oxygen resources":
    st.write("Oxygen")

elif choice == "Remdevisir":
    st.write("rem")

else: pass