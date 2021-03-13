import streamlit as st
import plotly.graph_objs as go
import json
from helpers import preprocess, preprocess_acs, filter_zip, _max_width_

def app():
    _max_width_()
    main_df = preprocess()
    acs_df = preprocess_acs()
    
    st.title('Filterable Philly Zip Code Map of Residential Tax Delinquencies and Census Metrics')
    st.write('Interactive breakdown of total accounts and principal due for actionable delinquent residential accounts in Philly, which can be filterd to show areas by levels of income, poverty, and unemployment from the census.')
    st.write('Use the dropdown menu to select a given delinquency metric to be displayed on the map, then a census metric to filter the map. Use the resulting slider to select the census metric threshold determining which zip codes to display. Hover over an area to view the corresponding metric value and zip code number.')
    
    c1, c2 = st.beta_columns(2)
    metric = c1.selectbox('Select Delinquency Metric', ('Total Accounts', 'Total Principal Due'))
    demo = c1.selectbox('Select Census Metric', ['Households Median Income', 'Percent Below Poverty', 'Unemployment Rate'])
    
    demo_filter = '_'.join([w for w in demo.split(' ')])
    if demo == 'Households Median Income':
        demo_slider = c1.slider('Households Median Income Below', 20000, 110000, 110000, 1000)
        acs_df = acs_df[acs_df[demo_filter] < demo_slider]
    else:
        if demo == 'Percent Below Poverty':
            demo_slider = c1.slider('Percent Below Poverty Above', 5, 50, 5, 1)
        else:
            demo_slider = c1.slider('Unemployment Rate Above', 2, 20, 2, 1)
        acs_df = acs_df[acs_df[demo_filter] > demo_slider]
    zips_filter = acs_df['Zip_Code'].tolist()
        
    philly = (40.00, -75.16)
    zips_geo = 'Zipcodes_Poly.geojson'
    with open(zips_geo) as f:
        zips_data = json.load(f)
    
    by_zip = filter_zip(main_df, metric)
    by_zip = by_zip[by_zip.index.isin(zips_filter)]
    z = by_zip.values.tolist()
    locations = [str(int(x)) for x in by_zip.index.tolist()]
    
    map_fig = go.FigureWidget(go.Choroplethmapbox(geojson=zips_data,
                                          z=z,
                                          locations=locations,
                                          featureidkey="properties.CODE",
                                          colorscale='YlOrRd'
                                          ))
    map_fig.update_layout(mapbox_style="carto-positron",
                   mapbox_zoom=9, mapbox_center = {"lat": philly[0], "lon": philly[1]})
    map_fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0}, height=600, width=540)
    
    c2.plotly_chart(map_fig)