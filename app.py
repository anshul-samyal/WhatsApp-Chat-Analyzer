import streamlit as st
import preprocessor # this is to import the preprocessor.py file 

st.sidebar.title("WhatsApp Chat Analyzer") # sidebar.s title
uploaded_file = st.sidebar.file_uploader("Choose a file")
if uploaded_file is not None:
    bytes_data = uploaded_file.getvalue()
    data = bytes_data.decode("utf-8")# till here this the code for uploading the chat file in our sidebar 
    df = preprocessor.preprocess(data) #to convert the data from preprocessor 

    st.dataframe(df) # to convert the the data into dataframe 
   
# to create the dropdown for different users or for the analysis between them 
user_list = df['user'].unique().tolist()
user_list.remove('group_notification')
user_list.sort()
user_list.insert(0 , "overall") #ye saari user name ke liye bakchidub thi
st.sidebar.selectbox("Show analysis with respect to" , user_list)

if st.sidebar.button('Show Analysis'):
    pass


