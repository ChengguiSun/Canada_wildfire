import streamlit as st
import pandas as pd
import plotly.graph_objects as go

def property_losses(fireLoss):
    st.title('Property Losses Caused by Forest Fires by Year from 1990 to 2020')

    st.markdown('''
    ### To interact with the plot below: **hover** over the plot to view data values, and use the **legend** on the left to toggle visibility of different jurisdictions.
    ''')

    Loss = fireLoss.copy()

    # Remove National Parks only
    Loss = Loss[
        ~Loss['Jurisdiction'].str.strip().str.lower().isin(['national parks'])
    ]

    Loss['Dollars'] = pd.to_numeric(Loss['Dollars'], errors='coerce').fillna(0)

    N = 5

    # Alphabetical order: A, B, C, ...
    jurisdiction_order = sorted(Loss['Jurisdiction'].dropna().unique())

    # Plot jurisdiction order excludes Canada
    plot_jurisdiction_order = sorted(
        [j for j in Loss['Jurisdiction'].dropna().unique() if j != 'Canada']
    )

    fig_loss = go.Figure()

    for jurisdiction in plot_jurisdiction_order:
        jurisdiction_df_loss = Loss[Loss['Jurisdiction'] == jurisdiction].sort_values('Year')

        fig_loss.add_trace(
            go.Bar(
                x=jurisdiction_df_loss['Year'],
                y=jurisdiction_df_loss['Dollars'],
                name=jurisdiction
            )
        )

    fig_loss.update_layout(
        title='',
        barmode='stack',
        xaxis_title='Year',
        yaxis_title='Dollars',
        xaxis_showgrid=False,
        yaxis_showgrid=False,
        legend=dict(x=-1, y=0.5, orientation="h", traceorder="normal")
    )

    st.plotly_chart(fig_loss, use_container_width=True)

    st.markdown('''
    ### To explore the table below, utilize the filters to narrow down specific years or jurisdictions.\
        By default, the table displays 5 rows. However, once filters are applied, all entries meeting the criteria will be displayed.
    ''')

    col3_1, col3_2 = st.columns(2)

    with col3_1:
        selected_year = st.multiselect(
            'Filter by Year',
            sorted(Loss['Year'].unique()),
            key='year3'
        )

        selected_jurisdiction = st.multiselect(
            'Filter by Jurisdiction',
            options=jurisdiction_order,
            key='jurisdiction3'
        )

    if selected_year or selected_jurisdiction:
        filtered_loss = Loss[
            (Loss['Year'].isin(selected_year if selected_year else Loss['Year'].unique())) &
            (Loss['Jurisdiction'].isin(selected_jurisdiction if selected_jurisdiction else jurisdiction_order))
        ]

        filtered_loss = filtered_loss.sort_values(['Jurisdiction', 'Year'])

        with col3_2:
            st.write(
                filtered_loss.to_html(
                    index=False,
                    classes='table table-centered',
                    table_id='my-table'
                ),
                unsafe_allow_html=True
            )
            st.markdown(
                '<style>#my-table {width: 100%;} #my-table th, #my-table td {text-align: center;}</style>',
                unsafe_allow_html=True
            )

    else:
        default_loss = Loss[Loss['Jurisdiction'] == 'Canada'].sort_values('Year').tail(N)

        with col3_2:
            st.write(
                default_loss.to_html(
                    index=False,
                    classes='table table-centered',
                    table_id='my-table'
                ),
                unsafe_allow_html=True
            )
            st.markdown(
                '<style>#my-table {width: 100%;} #my-table th, #my-table td {text-align: center;}</style>',
                unsafe_allow_html=True
            )