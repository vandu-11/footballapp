import streamlit as st
import pandas as pd

# Load Excel data
df = pd.read_excel('users.xlsx')
def redirect_page():
  
  if 'login' not in st.experimental_get_query_params():
      login_page()
  else:
    landing_page()
# Define app pages
def login_page():
    st.title('Login')
    
    # Get user credentials
    Username = st.text_input('Username',key='login_name')
    Email = st.text_input('Email',key='login_email')
    Password = st.text_input('Password', type='password',key='login_password')
    
    # Check if login is valid
    if st.button('Login'):
        if (Email in df.values) and (Password in df.values):
            st.success('Login successful!')
            st.experimental_set_query_params(login='success')
        else:
            st.error('Invalid login!')

def landing_page():
    st.title('Welcome to the Landing Page!')
    st.write('This is your landing page.')

# Define app flow
if 'login' not in st.experimental_get_query_params():
      login_page()
else:
    landing_page()

if __name__ == "__main__":
    redirect_page()

