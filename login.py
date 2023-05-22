import streamlit as st
import pandas as pd
from callender import main

# Load Excel data
df_data = pd.read_excel('student.xlsx')

# Define app pages
def login_page():
    st.title('Login')

    # Load Excel data
    df = pd.read_excel('users.xlsx')
    
    # Get user credentials
    Username = st.text_input('Username',key='log_name')
    Email = st.text_input('Email',key='log_email')
    Password = st.text_input('Password', type='password',key='log_password')

    # Check if login is valid
    if st.button('Login'):
        if (Email in df["Email"].values) and (Password in df[df["Email"] == Email]["Password"].values):
            st.success('Login successful!')
            st.experimental_set_query_params(login='success')
        else:
            st.error('Invalid login!')

def landing_page():
    st.markdown("##search")
    st.title('Student Data Search')
    name = st.text_input('Enter a student name')

    # Search for rows that contain the entered name
    results = df_data[df_data['name'].str.contains(name)]

    st.dataframe(results)

    # Display the results
    for i, row in results.iterrows():
        st.write(row['id'])
        st.write(row['name'])
        st.image(row['images'], width=300, caption=row['name'])
        st.write(row['skills'])

def payment_page():
    st.title('Payment Page')
    # Add payment page content here

def contact_page():
    st.title('Contact Page')
    # Add contact page content here

def redirect_page():
    if 'login' not in st.experimental_get_query_params():
        login_page()
    else:
        if st.sidebar.button('Logout'):
            # Redirect to the login page
            st.experimental_set_query_params()
            st.stop()
        else:
            option = st.sidebar.selectbox('Select an option', ['Search', 'Payment','slots_booking', 'Contact'])
            if option == 'Search':
                landing_page()
            elif option == 'Payment':
                payment_page()
            elif option == 'slots_booking':
                main()
            elif option == 'Contact':
                contact_page()

if __name__ == "__main__":
    redirect_page()