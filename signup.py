import streamlit as st
import pandas as pd

def sign_up():
    # Load existing user data from Excel file
    df = pd.read_excel("users.xlsx")

    # Create a Streamlit form for user input
    with st.form("signup_form"):
        Username = st.text_input("Username")
        Email = st.text_input("Email")
        Password = st.text_input("Password", type="password")

        # Submit button
        submit_button = st.form_submit_button(label="Sign up")

        # Handle form submission
        if submit_button:
            # Check if email already exists
            if Email in df["Email"].values:
                st.error("Email already exists. Please use a different email.")
            else:
                # Add user data to DataFrame and save to Excel file
                new_data = {"Username": Username, "Email": Email, "Password": Password}
                df = df.append(new_data, ignore_index=True)
                df.to_excel("users.xlsx", index=False)
                st.success("You have successfully signed up!")
    return df

if __name__ == "__main__":
    df = sign_up()
