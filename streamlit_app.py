import pandas as pd
import streamlit as st

st.title("Fight CoVID - Resources!")
st.markdown("For any updates/corrections/suggestions, please reach out to: www.subhroneel_moitra@outlook.com")
st.markdown("***")

choice = st.radio("Select the resource you need:", ("List of available beds", "Oxygen resources", "Remdevisir"))

if choice == "List of available beds":
    df = pd.read_excel(r"Resources/beds.xlsx")
    df = df.fillna("[Not Verified]")
    st.table(df)
    
elif choice == "Oxygen resources":
    df = pd.read_excel(r"Resources/oxygen.xlsx")
    df = df.fillna("[Not Verified]")
    st.table(df)

elif choice == "Remdevisir":
    st.write("Please give us some time we are gathering resources for this section")

else: pass