import pandas as pd
import streamlit as st


st.set_page_config(page_icon="😷", initial_sidebar_state='expanded', layout="wide")
st.set_option('deprecation.showPyplotGlobalUse', False)

def drop_col_from_df(df, state):
    colList = df.columns.values.tolist()
    saveList = ['Date', state]
    removeList = [i for i in colList if i not in saveList]
    print("\nTotal column(s): ", colList)
    print("\nSaving column(s): ", saveList)
    print("\nRemoving column(s): ", removeList)
    df = df.drop(removeList, axis = 1)
    return df

@st.cache
def fetch():
    return pd.read_csv("https://api.covid19india.org/csv/latest/states.csv")



# st.sidebar.write("Our contributors:")

st.title("Fight CoVID - Resources!")
st.markdown("For any updates/corrections/suggestions, please reach out [here](mailto://fightcovid.resources@gmail.com   )")
st.markdown("To volunteer with us connect [here](mailto://fightcovid.resources@gmail.com   )")

st.markdown("***")

choice = st.radio("Select the resource you need:", ("Oxygen resources", "Home-cooked meals", "Medicines", "Available beds"))

col1, col2 = st.beta_columns([5, 3])
with col1:
    if choice == "Available beds":
        st.write("Please give us some time we are gathering resources for this section")
        
    elif choice == "Oxygen resources":
        sheet_id = "1Oj64QgJYqvY65JYF_2pqnSXRQBlixGN8eyae-6lxjdU"
        sheet_name = "Oxygen"
        url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"
        
        df = pd.read_csv(url, index_col=False)
        df = df.fillna("")
        df = df.set_index("Unnamed: 0") 
        st.table(df)

    elif choice == "Remdevisir":
        st.write("Please give us some time we are gathering Remdevisir resources for this section")

    elif choice == "Home-cooked meals":    
        sheet_id = "1sgHGi1ns0dmVtmRdWVYb9Ax9LChurlkJJlLf1YeH_bE"
        sheet_name = "Meals"
        url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"
        
        df = pd.read_csv(url)
        df = df.fillna("")
        df = df.set_index("Sl. No.") 
        st.table(df)

    elif choice == "Medicines":
        st.write("Please give us some time we are gathering medicine resources for this section")
    else: pass


# Code for graphs
raw_df = fetch()
raw_df = raw_df.loc[raw_df['State'] == 'West Bengal']
raw_df = raw_df.set_index("Date")
raw_df.index = pd.to_datetime(raw_df.index)
raw_df.drop(["Other", "Tested", "State"], axis=1, inplace=True)

with col2:
    st.write("Latest West Bengal Trends")
    st.line_chart(raw_df)
