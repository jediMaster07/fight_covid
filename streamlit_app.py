import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt


st.set_page_config(page_icon="😷", initial_sidebar_state='expanded', layout="wide")
st.set_option('deprecation.showPyplotGlobalUse', False)

# st.sidebar.write("Our contributors:")

st.title("Fight CoVID - Resources!")
st.markdown("For any updates/corrections/suggestions, please reach out [here](mailto://fightcovid.resources@gmail.com   )")
st.markdown("To volunteer with us connect [here](mailto://fightcovid.resources@gmail.com   )")

st.markdown("***")

col1, col2 = st.beta_columns([5,3])

choice = col1.radio("Select the resource you need:", ("Oxygen resources", "Home-cooked meals", "Medicines", "Available beds"))

if choice == "Available beds":
    col1.write("Please give us some time we are gathering resources for this section")
    
elif choice == "Oxygen resources":
    sheet_id = "1Oj64QgJYqvY65JYF_2pqnSXRQBlixGN8eyae-6lxjdU"
    sheet_name = "Oxygen"
    url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"
    
    df = pd.read_csv(url)
    df = df.fillna("")
    col1.table(df)

elif choice == "Remdevisir":
    col1.write("Please give us some time we are gathering Remdevisir resources for this section")

elif choice == "Home-cooked meals":    
    sheet_id = "1sgHGi1ns0dmVtmRdWVYb9Ax9LChurlkJJlLf1YeH_bE"
    sheet_name = "Meals"
    url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"
    
    df = pd.read_csv(url)
    df = df.fillna("")
    col1.table(df)

elif choice == "Medicines":
    col1.write("Please give us some time we are gathering medicine resources for this section")
else: pass


# Code for graphs
def drop_col_from_df(df, state):
    colList = df.columns.values.tolist()
    saveList = ['Date', state]
    removeList = [i for i in colList if i not in saveList]
    print("\nTotal column(s): ", colList)
    print("\nSaving column(s): ", saveList)
    print("\nRemoving column(s): ", removeList)
    df = df.drop(removeList, axis = 1)
    return df

col2.write("Latest West Bengal Trends")
raw_df = pd.read_csv("https://api.covid19india.org/csv/latest/states.csv")
raw_df = raw_df.loc[raw_df['State'] == 'West Bengal']
raw_df = raw_df.set_index("Date")
raw_df.index = pd.to_datetime(raw_df.index)
raw_df.drop(["Other", "Tested", "State"], axis=1, inplace=True)


# confirmed_df = raw_df.loc[raw_df['Status'] == 'Confirmed']#.reset_index()#.drop('index', axis = 1)
# wb_confirmed = drop_col_from_df(confirmed_df, 'WB')

# recovered_df = raw_df.loc[raw_df['Status'] == 'Recovered']#.reset_index()#.drop('index', axis = 1)
# wb_recovered = drop_col_from_df(recovered_df, 'WB')

# deceased_df = raw_df.loc[raw_df['Status'] == 'Deceased']#.reset_index()#.drop('index', axis = 1)
# wb_deceased = drop_col_from_df(deceased_df, 'WB')

# plt.figure(figsize=(20,10))
# plt.ylabel("Confirmed", labelpad=35)
# plt.plot(wb_confirmed, 'r:', linewidth=2) 
# col2.pyplot(transparent=True)

# plt.ylabel("Recovered", labelpad=35)
# plt.plot(wb_recovered, 'g:', linewidth=2)
# col2.pyplot(transparent=True)

# plt.ylabel("Deceased", labelpad=35)
# plt.xlabel("Date", horizontalalignment='left')
# plt.plot(wb_deceased, 'k:', linewidth=2)
# col2.pyplot(transparent=True)

# result = pd.concat([wb_confirmed, wb_recovered, wb_deceased], axis=1)
# result.columns = ["confirmed", "recovered", "deceased"]
col2.line_chart(raw_df)
