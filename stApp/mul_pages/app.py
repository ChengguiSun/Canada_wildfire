import streamlit as st
import pandas as pd
from home import home
from fire_counts import fire_counts
from burned_area import burned_area
from property_losses import property_losses

st.set_page_config(page_title='Fires', layout = 'wide', initial_sidebar_state = 'auto')

def load_data():
    # LOADING DATA
    @st.cache_data
    def load_data(fname):
        return pd.read_pickle(fname)

    fireNumber = load_data('./data/NFD_Number_of_fires_by_month.pkl')
    print(fireNumber.columns)
    fireArea = load_data('./data/NFD_Area_burned_by_month.pkl')
    print(fireArea.columns)
    fireLoss = load_data('./data/NFD_Property_losses.pkl')
    print(fireLoss.columns)
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