import streamlit as st
import plotly.graph_objs as go
import json
from helpers import preprocess, preprocess_acs, filter_zip, _max_width_
    
def app():
    _max_width_()
    
    st.title('Side-by-Side Philly Zip Code Map of Residential Tax Delinquencies and Census Metrics')
    st.write('Interactive breakdown of total accounts and principal due for actionable delinquent residential accounts in Philly, side-by-side with income, poverty, and unemployment data from the census.')
    st.write('Use the dropdown menus to select a given delinquency and census metric associated with the corresponding map. Hover over an area to view the corresponding metric value and zip code number. While far from perfectly correlated, zip codes with larger total number of delinquent accounts and total principal due tend to have higher poverty levels and unemployment rates and lower median incomes.')
    
    main_df = preprocess()
    
    c1, c2 = st.beta_columns(2)
    
    metric = c1.selectbox('Select Delinquency Metric', ('Total Accounts', 'Total Principal Due'))
    
    philly = (40.00, -75.16)
    zips_geo = 'Zipcodes_Poly.geojson'
    with open(zips_geo) as f:
        zips_data = json.load(f)
    
    by_zip = filter_zip(main_df, metric)
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
    
    c1.plotly_chart(map_fig)
    
    acs_df = preprocess_acs()
    acs_metric = c2.selectbox('Select Census Metric', ('Households Median Income', 'Percent Below Poverty', 'Unemployment Rate'))
    
    acs_map_fig = go.FigureWidget(go.Choroplethmapbox(geojson=zips_data,
                                          z=acs_df['_'.join([w for w in acs_metric.split(' ')])],
                                          locations=acs_df['Zip_Code'],
                                          featureidkey="properties.CODE",
                                          colorscale='YlOrRd'
                                         ))
    acs_map_fig.update_layout(mapbox_style="carto-positron",
                   mapbox_zoom=9, mapbox_center = {"lat": philly[0], "lon": philly[1]})
    acs_map_fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0}, height=600, width=540)
    
    c2.plotly_chart(acs_map_fig)