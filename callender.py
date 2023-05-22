import streamlit as st
import pandas as pd
import os
from datetime import datetime,timedelta


def main():
    # create initial excel files for data storage if they don't exist
    if not os.path.isfile("slots.xlsx"):
        pd.DataFrame(columns=["Age Group", "Location", "Date", "Start Time", "End Time"]).to_excel("slots.xlsx", index=False)
    if not os.path.isfile("registrations.xlsx"):
        pd.DataFrame(columns=["Name", "Email", "Phone", "Slot ID", "Approved"]).to_excel("registrations.xlsx", index=False)
    
    # create sidebar selection for owner and coach
    user_type = st.sidebar.radio("Select user type", ["Owner", "Coach"])
    
    if user_type == "Owner":
        owner_page()
    else:
        coach_page()

def owner_page():
    # owner page content
    selection = st.radio("Select a page", ["Create Slot", "Dataframe", "Approve Registrations", "Approved List"])
    if selection == "Create Slot":
        create_slot()
    elif selection == "Dataframe":
        dataframe()
    elif selection == "Approve Registrations":
        approve_registrations()
    else:
        approved_list()

def coach_page():
    # coach page content
    view_slots()






# function to create a new training slot
def create_slot():
    st.title("Create Slot")
    age_group = st.selectbox("Age Group", ["Junior", "Senior"],key='sel2')
    location = st.selectbox("Location", ["Whitefield", "Marthalli", "Mahadevpura"],key='sel3')
    date = st.date_input("Date")
    start_time = st.time_input("Start Time")
    end_time = (datetime.combine(date, start_time) + timedelta(minutes=90)).time()
    st.write(f"End Time: {end_time}")
    if st.button("Create"):
        slots_df = pd.read_excel("slots.xlsx")
        count = slots_df[(slots_df['Age Group']==age_group) & (slots_df['Location']==location)]['Count'].max() + 1
        new_slot = {"Age Group": age_group, "Location": location, "Date": date, "Start Time": start_time, "End Time": end_time, "Count": count}
        slots_df = slots_df.append(new_slot, ignore_index=True)
        slots_df.to_excel("slots.xlsx", index=False)
        st.success("Slot created successfully!")


def dataframe():
    st.title("View Slots")
    slots_df = pd.read_excel("slots.xlsx")

    sorted_slots = slots_df.sort_values(by=["Age Group", "Location", "Date", "Start Time"])

    # filter slots by age group and location
    age_group = st.selectbox("Filter by Age group", ["All", "Junior", "Senior"])
    location = st.selectbox("Filter by Location", ["All", "Whitefield", "Marthalli", "Mahadevpura"])
    
    if age_group == "All" and location == "All":
        filtered_slots = sorted_slots
    elif age_group == "All":
        filtered_slots = sorted_slots[slots_df["Location"] == location]
    elif location == "All":
        filtered_slots = sorted_slots[slots_df["Age Group"] == age_group]
    else:
        filtered_slots = sorted_slots[(slots_df["Age Group"] == age_group) & (slots_df["Location"] == location)]
    
    if not filtered_slots.empty:
        st.write(f"{age_group} Slots ({location})")
        st.dataframe(filtered_slots)
    else:
        st.write("No slots available")


# function to view available training slots
# function to view available training slots
def view_slots():
    st.title("View Slots")
    slots_df = pd.read_excel("slots.xlsx")

    # filter slots by age group
    age_groups = ["All", "Junior", "Senior"]
    age_group2 = st.selectbox("Age group", age_groups)
    if age_group2 == "All":
        filtered_slots = slots_df
    else:
        filtered_slots = slots_df[slots_df["Age Group"] == age_group2]

    if not filtered_slots.empty:
        st.write(f"{age_group2} Slots")
        st.dataframe(filtered_slots)

        # show registration form for available slots
        selected_slot = st.selectbox("Select a slot to register", filtered_slots.index)
        name = st.text_input("Name")
        email = st.text_input("Email")
        phone = st.text_input("Phone")

        # submit registration for approval
        if st.button("Submit Registration"):
            registration = {"Name": name, "Email": email, "Phone": phone, "Slot ID": selected_slot, "Approved": "No"}
            registrations_df = pd.read_excel("registrations.xlsx")
            registrations_df = registrations_df.append(registration, ignore_index=True)
            registrations_df.to_excel("registrations.xlsx", index=False)
            st.success("Registration submitted successfully! Waiting for owner approval.")

        # show registrations for the selected slot
        registration_df = pd.read_excel("registrations.xlsx")
        registrations = registration_df[registration_df["Slot ID"] == selected_slot]
        if not registrations.empty:
            st.write(f"Registrations for slot {selected_slot}")
            st.dataframe(registrations[["Name", "Email", "Phone", "Approved"]])
        else:
            st.write("No registrations for this slot")
    else:
         st.write("No slots available")



        
def approve_registrations():
    st.title("Approve Registrations")
    registrations_df = pd.read_excel("registrations.xlsx")

    # filter unapproved registrations
    unapproved_registrations = registrations_df[registrations_df["Approved"] == "No"]
    
    if not unapproved_registrations.empty:
        st.write("Unapproved Registrations")
        st.dataframe(unapproved_registrations)

        # approve registration
        selected_index = st.selectbox("Select a registration to approve", unapproved_registrations.index)
        if st.button("Approve"):
            registrations_df.loc[selected_index, "Approved"] = "Yes"
            registrations_df.to_excel("registrations.xlsx", index=False)
            st.success("Registration approved!")
    
    else:
        st.write("No unapproved registrations")  

def approved_list():
    st.title("Approved List")
    registrations_df = pd.read_excel("registrations.xlsx")

    # filter approved registrations
    approved_registrations = registrations_df[registrations_df["Approved"] == "Yes"]
    
    if not approved_registrations.empty:
        st.write("Approved Registrations")
        st.dataframe(approved_registrations)
    
    else:
        st.write("No approved registrations")




if __name__ == "__main__":
    main()