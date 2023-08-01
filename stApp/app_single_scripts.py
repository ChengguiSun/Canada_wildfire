import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# SETTING PAGE CONFIG TO WIDE MODE
st.set_page_config(page_title='Fires', layout = 'wide', initial_sidebar_state = 'auto')

# LOADING DATA
@st.cache_data
def load_data(fname):
    return pd.read_pickle(fname)

fireNumber = load_data('./data/NFD_Number_of_fires_by_month.pkl')
fireArea = load_data('./data/NFD_Area_burned_by_month.pkl')
fireLoss = load_data('./data/NFD _Property_losses.pkl')

N = 5  # Default number of rows to display

# Create a selectbox for the sidebar
options = ['Home', 'Fire Counts', 'Burned Area (hectares)', 'Property Losses']
choice = st.sidebar.selectbox('Project Page', options)

if choice == 'Home':
    st.title("Canada Forest Fires Statistics")
    st.image("./img/canada.png", width=50)
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

    st.subheader("Fire Counts")
    st.markdown("""
    Features of this section:
    <ul style='list-style-type:circle; margin-left: 20px; line-height:1.6'>
        <li>Focuses on the number of fires that have occurred each month since 1990 in different jurisdictions in Canada.</li>
        <li>Users can filter the data by Year, Month, and Jurisdiction.</li>
        <li>An interactive graph shows the number of fires over the years.</li>
    </ul>
    """, unsafe_allow_html=True)

    st.subheader("Burned Area")
    st.markdown("""
    Features of this section:
    <ul style='list-style-type:circle; margin-left: 20px; line-height:1.6'>
        <li>Delves into the impact of these fires, more specifically, the area these fires have burned each month.</li>
        <li>Similar to the Fire Counts section, users can apply filters for Year, Month, and Jurisdiction.</li>
        <li>Analysis of this data helps to understand the scale of forest fires and to anticipate potential environmental consequences.</li>
    </ul>
    """, unsafe_allow_html=True)

    st.subheader("Property Losses")
    st.markdown("""
    Features of this section:
    <ul style='list-style-type:circle; margin-left: 20px; line-height:1.6'>
        <li>Provides data on the property losses resulting from these fires.</li>
        <li>Users can filter the data by Year and Jurisdiction.</li>
        <li>By examining these losses, we can better comprehend the human and economic costs of these fires and can guide efforts towards more effective protective measures and mitigation strategies.</li>
    </ul>
    """, unsafe_allow_html=True)

    st.write("""
    Throughout the website, users can interact with visualizations and filter data to focus on areas and time periods of interest. 
    We hope that this tool aids in fostering a comprehensive understanding of forest fires in Canada, and spurs necessary action towards 
    their prevention and control.
    """)
    
    st.image("./img/wildfire_stable_diffusion.jpg", width=None, use_column_width="auto", output_format="auto")
    
    st.header("Attribution")
    st.markdown("""
    - **DATA SOURCES**: Canadian Council of Forest Ministers - Conseil canadien des ministres des forêts. (2020). 
    The data used in this application is derived from the _National Forestry Database. This dataset is a product of Natural Resources Canada – Ressources naturelles Canada. [DOI](http://doi.org/10.5281/zenodo.3690046)
    The _National Forestry Database_ is archived on Zenodo.org. All releases can be accessed [here](https://zenodo.org/record/3690045).
    - **CANADA FLAG ICON**: [Flags icons created by Freepik - Flaticon](https://www.flaticon.com/free-icons/flags)
    """)


elif choice == 'Fire Counts':
    st.title('Number of Forest Fires by Month from 1990 to 2020')

    # Load and plot data
    num = fireNumber.copy()  # using the filtered dataframe
    num['Date'] = pd.to_datetime(num['Year'].astype(str) + '-' + num['Month'].astype(str), format="%Y-%B")  # convert Date to datetime object

    # Create a new figure
    fig_num = go.Figure()
    
    # Get unique jurisdictions
    unique_jurisdictions_num = sorted(num['Jurisdiction'].unique())

    # Move 'Canada' to the end of the list
    unique_jurisdictions_num.remove('Canada')
    unique_jurisdictions_num.append('Canada')

    # Loop over each unique jurisdiction
    for jurisdiction in unique_jurisdictions_num:
        # Create a new dataframe for each jurisdiction
        jurisdiction_df = num[num['Jurisdiction'] == jurisdiction]
        # Add a line to the figure for the current jurisdiction
        fig_num.add_trace(go.Scatter(x= jurisdiction_df['Date'], y= jurisdiction_df['Number'], 
                                mode='lines', name = jurisdiction))

    # Set the title and labels
    fig_num.update_layout(title='', 
                    xaxis_title='Date', yaxis_title='Number',
                    xaxis_showgrid=False, yaxis_showgrid=False,
                    legend=dict(x=-1, y=0.5, orientation="h"))
        
    # Update y-axis to display only years
    fig_num.update_xaxes(tickformat="%Y")

    # Show the plot
    st.plotly_chart(fig_num, use_container_width=True)  # plot the figure
    
    col1_1, col1_2 = st.columns(2)

    with col1_1:
        selected_value1_year = st.multiselect('Filter by Year', fireNumber['Year'].unique(), key='year1')
        selected_value1_month = st.multiselect('Filter by Month', fireNumber['Month'].unique(), key='month1')
        selected_value1_jurisdiction = st.multiselect('Filter by Jurisdiction', unique_jurisdictions_num, key='jurisdiction1')

    # Filter data for plot
    if selected_value1_year or selected_value1_month or selected_value1_jurisdiction:
        filtered_num = fireNumber[(fireNumber['Year'].isin(selected_value1_year if selected_value1_year else fireNumber['Year'].unique())) &
                                (fireNumber['Month'].isin(selected_value1_month if selected_value1_month else fireNumber['Month'].unique())) &
                                (fireNumber['Jurisdiction'].isin(selected_value1_jurisdiction if selected_value1_jurisdiction else unique_jurisdictions_num))]
        # Show the full table
        with col1_2:
            st.write(filtered_num[['Year', 'Month', 'Jurisdiction', 'Number']].to_html(index=False, classes='table table-centered', table_id='my-table-num'), unsafe_allow_html=True)
            st.markdown('<style>#my-table-num {width: 100%;} #my-table-num th, #my-table-num td {text-align: center;}</style>', unsafe_allow_html=True)
    else:
        # If no filters applied, only display the last 5 rows
        with col1_2:
            st.write(fireNumber[['Year', 'Month', 'Jurisdiction', 'Number']].tail(N).to_html(index=False, classes='table table-centered', table_id='my-table-num'), unsafe_allow_html=True)
            st.markdown('<style>#my-table-num {width: 100%;} #my-table-num th, #my-table-num td {text-align: center;}</style>', unsafe_allow_html=True)
               
                    
elif choice == 'Burned Area (hectares)':
    st.title('Area Burned by Forest Fires by Month from 1990 to 2020')

    # Load and plot data
    area = fireArea.copy()  # using the filtered dataframe
    area['Date'] = pd.to_datetime(area['Year'].astype(str) + '-' + area['Month'].astype(str), format="%Y-%B")  # convert Date to datetime object

    # Create a new figure
    fig_area = go.Figure()
    
    # Get unique jurisdictions
    unique_jurisdictions_area = sorted(area['Jurisdiction'].unique())

    # Move 'Canada' to the end of the list
    unique_jurisdictions_area.remove('Canada')
    unique_jurisdictions_area.append('Canada')

    # Loop over each unique jurisdiction
    for jurisdiction in unique_jurisdictions_area:
        # Create a new dataframe for each jurisdiction
        jurisdiction_df_area = area[area['Jurisdiction'] == jurisdiction]
        # Add a line to the figure for the current jurisdiction
        fig_area.add_trace(go.Scatter(x= jurisdiction_df_area['Date'], y= jurisdiction_df_area['Area (hectares)'], 
                                mode='lines', name= jurisdiction))

    # Set the title and labels
    fig_area.update_layout(title='', 
                    xaxis_title='Date', yaxis_title='Area (hectares)',
                    xaxis_showgrid=False, yaxis_showgrid=False,
                    legend=dict(x=-1, y=0.5, orientation="h"))
    
    # Update y-axis to display only years
    fig_area.update_xaxes(tickformat="%Y")

    # Show the plot
    st.plotly_chart(fig_area, use_container_width=True)  # plot the figure
    
    
    col2_1, col2_2 = st.columns(2)
    
    with col2_1:
        selected_value2_year = st.multiselect('Filter by Year', fireArea['Year'].unique(), key='year2')
        selected_value2_month = st.multiselect('Filter by Month', fireArea['Month'].unique(), key='month2')
        selected_value2_jurisdiction = st.multiselect('Filter by Jurisdiction', unique_jurisdictions_area, key='jurisdiction2')
    
        # Filter data for table
        if selected_value2_year or selected_value2_month or selected_value2_jurisdiction:
            filtered_area = fireArea[(fireArea['Year'].isin(selected_value2_year if selected_value2_year else fireArea['Year'].unique())) &
                                        (fireArea['Month'].isin(selected_value2_month if selected_value2_month else fireArea['Month'].unique())) &
                                        (fireArea['Jurisdiction'].isin(selected_value2_jurisdiction if selected_value2_jurisdiction else unique_jurisdictions_area))]
            # Show the full table
            with col2_2:
                st.write(filtered_area[['Year', 'Month', 'Jurisdiction', 'Area (hectares)']].to_html(index=False, classes='table table-centered', table_id='my-table'), unsafe_allow_html=True)
                st.markdown('<style>#my-table {width: 100%;} #my-table th, #my-table td {text-align: center;}</style>', unsafe_allow_html=True)
        else:
            # If no filters applied, only display the last 5 rows
            with col2_2:
                st.write(fireArea[['Year', 'Month', 'Jurisdiction', 'Area (hectares)']].tail(N).to_html(index=False, classes='table table-centered', table_id='my-table'), unsafe_allow_html=True)
                st.markdown('<style>#my-table {width: 100%;} #my-table th, #my-table td {text-align: center;}</style>', unsafe_allow_html=True)



elif choice == 'Property Losses':
    st.title('Property Losses Caused by Forest Fires by year from 1990 to 2020')

    Loss = fireLoss.copy() 
    # Create a new figure
    fig_loss = go.Figure()

    # Get unique jurisdictions and years for multiselect options
    unique_jurisdictions = fireLoss['Jurisdiction'].unique()
    unique_years = fireLoss['Year'].unique()
    
        # Get unique jurisdictions
    unique_jurisdictions_loss = sorted(Loss['Jurisdiction'].unique())

    # Move 'Canada' to the end of the list
    unique_jurisdictions_loss.remove('Canada')
    unique_jurisdictions_loss.append('Canada')

    # Loop over each unique jurisdiction in filtered data
    for jurisdiction in unique_jurisdictions_loss:
        # Create a new dataframe for each jurisdiction
        jurisdiction_df_loss = Loss[Loss['Jurisdiction'] == jurisdiction]
        # Add a bar to the figure for the current jurisdiction
        fig_loss.add_trace(go.Bar(x=jurisdiction_df_loss['Year'], y=jurisdiction_df_loss['Dollars'], name=jurisdiction))

    # Set the title and labels
    fig_loss.update_layout(title='',
                           xaxis_title='Year', yaxis_title='Dollars',
                           xaxis_showgrid=False, yaxis_showgrid=False,
                           legend=dict(x=-1, y=0.5, orientation="h"))

    # Show the plot
    st.plotly_chart(fig_loss, use_container_width=True)
    
    col3_1, col3_2 = st.columns(2)
    
    with col3_1:
        # Multiselect widgets for filtering data
        selected_year = st.multiselect('Filter by Year', options=unique_years, key='year3')
        selected_jurisdiction = st.multiselect('Filter by Jurisdiction', options=unique_jurisdictions, key='jurisdiction3')

        # Filter data based on selected year and jurisdiction
        if selected_year or selected_jurisdiction:
            filtered_loss = fireLoss[(fireLoss['Year'].isin(selected_year if selected_year else unique_years)) &
                                    (fireLoss['Jurisdiction'].isin(selected_jurisdiction if selected_jurisdiction else unique_jurisdictions))]
            
            # Show the full table
            with col3_2:
                st.write(filtered_loss.to_html(index=False, classes='table table-centered', table_id='my-table'), unsafe_allow_html=True)
                st.markdown('<style>#my-table {width: 100%;} #my-table th, #my-table td {text-align: center;}</style>', unsafe_allow_html=True)
        else:
            # If no filters applied, only display the last 5 rows
            with col3_2:
                st.write(fireLoss.tail(N).to_html(index=False, classes='table table-centered', table_id='my-table'), unsafe_allow_html=True)
                st.markdown('<style>#my-table {width: 100%;} #my-table th, #my-table td {text-align: center;}</style>', unsafe_allow_html=True)
