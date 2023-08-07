import streamlit as st


def home():
    st.title("Canada Forest Fires Statistics")

    st.header("Project Objectives")
    st.markdown("""
    The objectives of this visualizatoin project are:
    <ul style='list-style-type:circle; margin-left: 20px; line-height:1.6'>
        <li>To offer an interactive tool that allows users to explore and understand the impact of forest fires in Canada.</li>
        <li>To highlight the significant threats posed by forest fires to both the environment and properties.</li>
        <li>To present detailed data on fire counts, the areas burned, and the property losses due to these fires.</li>
    </ul>
    """, unsafe_allow_html=True)
    
    
    st.header("Visualization Contents")
    st.markdown("""
    This visualzation project include the demonstration of fire counts, burned area, and proprerty losses. The contents of each section are:
    """, unsafe_allow_html=True)

    st.subheader("Fire Counts")
    st.markdown("""
    <ul style='list-style-type:circle; margin-left: 20px; line-height:1.6'>
        <li>Focuses on the number of fires that have occurred each month since 1990 in different jurisdictions in Canada.</li>
        <li>An interactive graph shows the number of fires over the years.</li>
        <li>Users can filter the data by Year, Month, and Jurisdiction in the table.</li>

    </ul>
    """, unsafe_allow_html=True)

    st.subheader("Burned Area")
    st.markdown("""
    <ul style='list-style-type:circle; margin-left: 20px; line-height:1.6'>
        <li>Delves into the impact of these fires, more specifically, the area these fires have burned each month.</li>
        <li>Similar to the Fire Counts section, there is an interactive graph and a table. Users can apply filters to the table for Year, Month, and Jurisdiction.</li>
        <li>Analysis of this data helps to understand the scale of forest fires and to anticipate potential environmental consequences.</li>
    </ul>
    """, unsafe_allow_html=True)

    st.subheader("Property Losses")
    st.markdown("""
    <ul style='list-style-type:circle; margin-left: 20px; line-height:1.6'>
        <li>Provides data on the property losses resulting from these fires.</li>
        <li>Similar to previous two sections, there is an interactive graph and a table. Users can apply filters to the table for Year and Jurisdiction.</li>
        <li>By examining these losses, we can better comprehend the human and economic costs of these fires and can guide efforts towards more effective protective\
            measures and mitigation strategies.</li>
    </ul>
    """, unsafe_allow_html=True)
   
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image("./img/wildfire_stable_diffusion.jpg", width=None, use_column_width="auto", output_format="auto")
    with col2:
        st.image("./img/wildfire_stable_diffusion2.jpg", width=None, use_column_width="auto", output_format="auto")
    with col3:
        st.image("./img/wildfire_stable_diffusion3.jpg", width=None, use_column_width="auto", output_format="auto")
    
    st.header("Attribution")
    st.markdown("""
    - **DATA SOURCES**: Canadian Council of Forest Ministers - Conseil canadien des ministres des forêts. (2020). 
    The data used in this application is derived from the _National Forestry Database. This dataset is a product of Natural Resources Canada\
        – Ressources naturelles Canada. [DOI](http://doi.org/10.5281/zenodo.3690046)
    The _National Forestry Database_ is archived on Zenodo.org. All releases can be accessed [here](https://zenodo.org/record/3690045).
    - **CANADA FLAG ICON**: [Flags icons created by Freepik - Flaticon](https://www.flaticon.com/free-icons/flags)
    """)
    