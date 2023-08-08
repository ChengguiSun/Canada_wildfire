import streamlit as st
import pandas as pd
import plotly.graph_objects as go

def fire_counts(fireNumber):
    st.title('Number of Forest Fires by Month from 1990 to 2020')
    
    st.markdown('''
    ### To interact with the Plot below: **hover** over the plot to view data values, and use the **legend** on the left to toggle visibility of different jurisdictions.
    ''')

    # Load and plot data
    num = fireNumber.copy()  # using the filtered dataframe
    num['Time'] = pd.to_datetime(num['Year'].astype(str) + '-' + num['Month'].astype(str), format="%Y-%B")  # convert Time to datetime object
    
    N = 5  # Default number of rows to display

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
        fig_num.add_trace(go.Scatter(x= jurisdiction_df['Time'], y= jurisdiction_df['Number'], 
                                mode='lines', name = jurisdiction))

    # Set the title and labels
    fig_num.update_layout(title='', 
                    xaxis_title='Time', yaxis_title='Number',
                    xaxis_showgrid=False, yaxis_showgrid=False,
                    legend=dict(x=-1, y=0.5, orientation="h"))
        
    # Update y-axis to display only years
    fig_num.update_xaxes(tickformat="%Y")

    # Show the plot
    st.plotly_chart(fig_num, use_container_width=True)  # plot the figure
    
    
    st.markdown('''
    ### To interact with the Table below: use the **filters** below the plot to select specific years, months, or jurisdictions.\
        By default, the table displays 5 rows. However, once filters are applied, all entries meeting the criteria will be displayed.
    ''')
    
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
            