import streamlit as st
import pandas as pd
import plotly.graph_objects as go

def property_losses(fireLoss):
    st.title('Property Losses Caused by Forest Fires by year from 1990 to 2020')

    Loss = fireLoss.copy()
    N = 5  # Default number of rows to display 
    # Create a new figure
    fig_loss = go.Figure()

    # Get unique jurisdictions and years for multiselect options
    
    
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
        selected_year = st.multiselect('Filter by Year', fireLoss['Year'].unique(), key='year3')
        selected_jurisdiction = st.multiselect('Filter by Jurisdiction', options=unique_jurisdictions_loss, key='jurisdiction3')

        # Filter data based on selected year and jurisdiction
        if selected_year or selected_jurisdiction:
            filtered_loss = fireLoss[(fireLoss['Year'].isin(selected_year if selected_year else fireLoss['Year'].unique())) &
                                    (fireLoss['Jurisdiction'].isin(selected_jurisdiction if selected_jurisdiction else unique_jurisdictions_loss))]
            
            # Show the full table
            with col3_2:
                st.write(filtered_loss.to_html(index=False, classes='table table-centered', table_id='my-table'), unsafe_allow_html=True)
                st.markdown('<style>#my-table {width: 100%;} #my-table th, #my-table td {text-align: center;}</style>', unsafe_allow_html=True)
        else:
            # If no filters applied, only display the last 5 rows
            with col3_2:
                st.write(fireLoss.tail(N).to_html(index=False, classes='table table-centered', table_id='my-table'), unsafe_allow_html=True)
                st.markdown('<style>#my-table {width: 100%;} #my-table th, #my-table td {text-align: center;}</style>', unsafe_allow_html=True)
                