import pandas as pd
import streamlit as st

st.set_page_config(page_icon="😷", initial_sidebar_state='collapsed')
# st.sidebar.write("Our contributors:")

st.title("Fight CoVID - Resources!")
st.markdown("For any updates/corrections/suggestions, please reach out [here](mailto://fightcovid.resources@gmail.com   )")
st.markdown("To volunteer with us connect [here](mailto://fightcovid.resources@gmail.com   )")
st.markdown("***")

choice = st.radio("Select the resource you need:", ("Oxygen resources", "Home-cooked meals", "Medicines"))

if choice == "List of available beds":
    pass
    
elif choice == "Oxygen resources":
    sheet_id = "1Oj64QgJYqvY65JYF_2pqnSXRQBlixGN8eyae-6lxjdU"
    sheet_name = "Oxygen"
    url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"
    
    df = pd.read_csv(url)
    df = df.fillna("")
    st.table(df)

elif choice == "Remdevisir":
    st.write("Please give us some time we are gathering Remdevisir resources for this section")

elif choice == "Home-cooked meals":    
    sheet_id = "1sgHGi1ns0dmVtmRdWVYb9Ax9LChurlkJJlLf1YeH_bE"
    sheet_name = "Meals"
    url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"
    
    df = pd.read_csv(url)
    df = df.fillna("")
    st.table(df)

elif choice == "Medicines":
    st.write("Please give us some time we are gathering medicine resources for this section")
    

else: pass