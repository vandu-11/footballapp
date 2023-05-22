import streamlit as st
import streamlit.components.v1 as stc 
import pandas as pd
from signup import sign_up
from login import redirect_page
from streamlit_option_menu import option_menu # assuming this is a custom function defined in a separate file


st.set_page_config(page_title="Football Club", page_icon=":soccer:")

# Read the user data from the Excel file
df = pd.read_excel('users.xlsx')

# Read the student data from the Excel file
df_data = pd.read_excel('student.xlsx')


custom_title = """
<div style="font-size:40px;font-weight:bolder;background-color:#fff;padding:10px;
border-radius:10px;border:5px solid #464e5f;text-align:center;">
		<span style='color:blue'>F</span>
		<span style='color:orange'>o</span>
		<span style='color:red'>o</span>
		<span style='color:black'>t</span>
		<span style='color:green'>i</span>
		<span style='color:black'>e</span>
		<span style='color:yellow'>s</span>
		<span style='color:blue'>-</span>
		<span style='color:blue'>S</span>
		<span style='color:#464e5f'>p</span>
		<span style='color:red'>o</span>
		<span style='color:green'>r</span>
		<span style='color:yellow'>t</span>
		<span style='color:black'>s</span>
		<span style='color:blue'>-</span>
		<span style='color:blue'>A</span>
		<span style='color:yellow'>c</span>
		<span style='color:black'>a</span>
        <span style='color:orange'>d</span>
        <span style='color:red'>e</span>
        <span style='color:green'>m</span>
        <span style='color:black'>y</span>
        
        
		
</div>
"""

# Define function for the home page
def home():
    st.title('Home Page')
    st.write("Welcome to the home page!")
stc.html(custom_title)

# Define function for the signup page
def signup():
    sign_up()

# Define function for the login page
def login():
     redirect_page()



# Define the options for the navigation bar
options = ["Home", "Sign Up", "Login"]
icons=['house', 'cloud-upload', "list-task"]

# Create a vertical navigation bar with the options
selection = option_menu(options=options,icons=icons, orientation='horizontal', menu_title='Navigation')


          

# Display the content based on the selected option
if selection == "Home":
    home()
elif selection == "Sign Up":
    signup()
else:
    login()
