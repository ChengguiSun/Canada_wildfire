import streamlit as st
import pandas as pd
import plotly.graph_objects as go

def burned_area(fireArea):
    st.title('Area Burned by Forest Fires by Month from 1990 to 2020')

    # Load and plot data
    area = fireArea.copy()  # using the filtered dataframe
    area['Time'] = pd.to_datetime(area['Year'].astype(str) + '-' + area['Month'].astype(str), format="%Y-%B")  # convert Time to datetime object
    
    N = 5  # Default number of rows to display

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
        fig_area.add_trace(go.Scatter(x= jurisdiction_df_area['Time'], y= jurisdiction_df_area['Area (hectares)'], 
                                mode='lines', name= jurisdiction))

    # Set the title and labels
    fig_area.update_layout(title='', 
                    xaxis_title='Time', yaxis_title='Area (hectares)',
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