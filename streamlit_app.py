import pandas as pd
import streamlit as st

st.set_page_config(page_icon="😷", initial_sidebar_state='collapsed')
st.sidebar.write("Hell-o!")

st.title("Fight CoVID - Resources!")
st.markdown("For any updates/corrections/suggestions, please reach out [here](mailto://fightcovid.resources@gmail.com   )")
st.markdown("To volunteer with us connect [here](mailto://fightcovid.resources@gmail.com   )")
st.markdown("***")

choice = st.radio("Select the resource you need:", ("List of available beds", "Oxygen resources", "Remdevisir", "Home-cooked meals", "Medicines"))

if choice == "List of available beds":
    df = pd.read_excel(r"Resources/beds.xlsx")
    df = df.fillna("[Not Verified]")
    st.table(df)
    
elif choice == "Oxygen resources":
    df = pd.read_excel(r"Resources/oxygen.xlsx")
    df = df.fillna("[Not Verified]")
    st.table(df)

elif choice == "Remdevisir":
    st.write("Please give us some time we are gathering Remdevisir resources for this section")

elif choice == "Home-cooked meals":
    st.write("Please give us some time we are gathering resources for this section")

elif choice == "Medicines":
    st.write("Please give us some time we are gathering medicine resources for this section")
    

else: pass