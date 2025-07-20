import streamlit as st
from api_wrapper import APIWrapper
import os
from custom_logger import logger
from dotenv import load_dotenv
load_dotenv()

api_wrapper = APIWrapper(
    api_address=os.getenv('API_ADDRESS'),
    api_port=os.getenv('API_PORT')
)

countries = api_wrapper.list_countries()


st.title("Country Getter GUI")
with st.form("my_form"):
    st.write("Select Countries to Pull data from")
    selected_countries = st.multiselect("Countries", countries, default=countries[:2], accept_new_options=True)
    format_data = st.checkbox("Format Data", value=True)
    submit_button = st.form_submit_button("Submit")

if submit_button:
    st.header("Data for Countries:")
    logger.info(f"User submitted countries: {selected_countries}")
    data = api_wrapper.country_data(selected_countries)
    st.dataframe(data)

logger.info("Streamlit Page Loaded")
    