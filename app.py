import streamlit as st
import preprocessor , helper  # Import preprocessor.py and helper.py

st.sidebar.title("WhatsApp Chat Analyzer")  # Sidebar title
uploaded_file = st.sidebar.file_uploader("Choose a file", type=["txt"])  # File uploader

# Ensure df is only created when a file is uploaded
df = None

if uploaded_file is not None:
    bytes_data = uploaded_file.getvalue()
    data = bytes_data.decode("utf-8")  # Convert bytes to text
    df = preprocessor.preprocess(data)  # Process the chat file

    st.dataframe(df)  # convert the data into dataframe 

# Prevent errors if no file is uploaded
user_list = []
if df is not None:
    user_list = df['user'].unique().tolist()
    if 'group_notification' in user_list:
        user_list.remove('group_notification')
    user_list.sort()
    user_list.insert(0, "Overall")  # Add "Overall" to user list

# Dropdown to select user for analysis
selected_user = st.sidebar.selectbox("Show analysis with respect to", user_list)

# Only run analysis if the button is clicked and a file is uploaded
if st.sidebar.button('Show Analysis') and df is not None:

    num_messages = helper.fetch_stats(selected_user, df)  # Fetch statistics for the selected user that is the number of messages 

    col1, col2, col3, col4 = st.columns(4)  

    with col1:
        col1.header("Total Messages")



