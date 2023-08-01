import streamlit as st
import pandas as pd
from home import home
from fire_counts import fire_counts
from burned_area import burned_area
from property_losses import property_losses

def load_data():
    # LOADING DATA
    @st.cache_data
    def load_data(fname):
        return pd.read_pickle(fname)

    fireNumber = load_data('./data/NFD_Number_of_fires_by_month.pkl')
    fireArea = load_data('./data/NFD_Area_burned_by_month.pkl')
    fireLoss = load_data('./data/NFD _Property_losses.pkl')
    return fireNumber, fireArea, fireLoss

def main():
    # Load your data
    fireNumber, fireArea, fireLoss = load_data()

    # Define your pages
    pages = {
        "Home": home,
        "Fire Counts": lambda: fire_counts(fireNumber),
        "Burned Area (hectares)": lambda: burned_area(fireArea),
        "Property Losses": lambda: property_losses(fireLoss)
    }

    # Create a selectbox for the sidebar
    st.sidebar.title('Page Navigation')
    choice = st.sidebar.radio("", list(pages.keys()))

    # Render the selected page
    pages[choice]()

if __name__ == "__main__":
    main()