import streamlit as st
import pandas as pd
from datetime import datetime
from engine_util import engine
from crud import (
    add_provider, update_provider, delete_provider,
    add_receiver, update_receiver, delete_receiver,
    add_food, add_claim, update_claim_status
)

st.set_page_config(page_title="Add Entries", layout="wide")
st.title("➕ Add / Manage Entries")

# Provider Section
with st.expander("🏪 Manage Providers", expanded=False):
    st.subheader("➕ Add New Provider")
    with st.form("add_provider_form"):
        name = st.text_input("Name")
        type_ = st.selectbox("Type", ["Restaurant", "Grocery Store", "Supermarket", "Catering Service"])
        address = st.text_input("Address")
        city = st.text_input("City")
        contact = st.text_input("Contact")
        submitted = st.form_submit_button("Add Provider")
        if submitted:
            new_id = add_provider(name, type_, address, city, contact)
            st.success(f"✅ Added! Provider ID: {new_id}")

    st.divider()

    st.subheader("🔁 Update Provider")
    df = pd.read_sql("SELECT provider_id, name FROM providers ORDER BY provider_id", engine)
    pid = st.selectbox("Select Provider to Update", df["provider_id"])
    new_name = st.text_input("New Name", key="pname")
    new_contact = st.text_input("New Contact", key="pcontact")
    if st.button("Update Provider"):
        update_provider(pid, name=new_name or None, contact=new_contact or None)
        st.success(f"✅ Provider {pid} updated.")

    st.divider()

    st.subheader("🗑️ Delete Provider")
    del_pid = st.selectbox("Select Provider to Delete", df["provider_id"], key="pdel")
    if st.button("Delete Provider"):
        delete_provider(del_pid)
        st.warning(f"🗑️ Deleted Provider ID: {del_pid}")

# Receiver Section 
with st.expander("🎯 Manage Receivers", expanded=False):
    st.subheader("➕ Add New Receiver")
    with st.form("add_receiver_form"):
        name = st.text_input("Receiver Name")
        type_ = st.selectbox("Type", ["NGO", "Charity", "Individual", "Orphanage"])
        city = st.text_input("City")
        contact = st.text_input("Contact")
        submitted = st.form_submit_button("Add Receiver")
        if submitted:
            new_id = add_receiver(name, type_, city, contact)
            st.success(f"✅ Added! Receiver ID: {new_id}")

    st.divider()

    st.subheader("🔁 Update Receiver")
    df_r = pd.read_sql("SELECT receiver_id, name FROM receivers ORDER BY receiver_id", engine)
    rid = st.selectbox("Select Receiver to Update", df_r["receiver_id"])
    new_name = st.text_input("New Name", key="rname")
    new_contact = st.text_input("New Contact", key="rcontact")
    if st.button("Update Receiver"):
        update_receiver(rid, name=new_name or None, contact=new_contact or None)
        st.success(f"✅ Receiver {rid} updated.")

    st.divider()

    st.subheader("🗑️ Delete Receiver")
    del_rid = st.selectbox("Select Receiver to Delete", df_r["receiver_id"], key="rdel")
    if st.button("Delete Receiver"):
        delete_receiver(del_rid)
        st.warning(f"🗑️ Deleted Receiver ID: {del_rid}")

# Food Listing 
with st.expander("🍱 Add Food Listing", expanded=False):
    with st.form("add_food_form"):
        food_name = st.text_input("Food Name")
        quantity = st.number_input("Quantity", min_value=1)
        expiry_date = st.date_input("Expiry Date")
        provider_id = st.number_input("Provider ID (must exist)", min_value=1)
        provider_type = st.text_input("Provider Type")
        location = st.text_input("Location")
        food_type = st.selectbox("Food Type", ["Packaged", "Fresh", "Cooked"])
        meal_type = st.selectbox("Meal Type", ["Breakfast", "Lunch", "Dinner", "Snacks"])
        submitted = st.form_submit_button("Add Food")
        if submitted:
            add_food(food_name, quantity, expiry_date, provider_id, provider_type, location, food_type, meal_type)
            st.success("✅ Food listing added successfully!")

# Claim 
with st.expander("📥 Manage Claims", expanded=False):
    st.subheader("➕ Add Claim")
    with st.form("add_claim_form"):
        food_id = st.number_input("Food ID", min_value=1)
        receiver_id = st.number_input("Receiver ID", min_value=1)
        status = st.selectbox("Status", ["Pending", "Completed", "Cancelled"])
        timestamp = datetime.now()
        submitted = st.form_submit_button("Add Claim")
        if submitted:
            add_claim(food_id, receiver_id, status, timestamp)
            st.success("✅ Claim added successfully!")

    st.divider()

    st.subheader("🔁 Update Claim Status")
    df_claims = pd.read_sql("SELECT claim_id, food_id, status FROM claims ORDER BY claim_id", engine)
    claim_id = st.selectbox("Select Claim to Update", df_claims["claim_id"])
    new_status = st.selectbox("New Status", ["Pending", "Completed", "Cancelled"], key="status_update")
    if st.button("Update Claim Status"):
        update_claim_status(claim_id, new_status)
        st.success(f"✅ Claim {claim_id} status updated to {new_status}")
