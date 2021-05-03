import streamlit as st
import pandas as pd

st.title("Fight CoVID - Resources!")

choice = st.radio("Select the resource you need:", ("List of available beds", "Oxygen resources", "Remdevisir"))

if choice == "List of available beds":
    df = pd.read_excel(r"Resources/beds.xlsx", index=False)
    
    df = df.fillna("[Not Verified]")
    
    st.table(df)
    
elif choice == "Oxygen resources":
    st.write("Oxygen")

elif choice == "Remdevisir":
    st.write("rem")

else: pass
