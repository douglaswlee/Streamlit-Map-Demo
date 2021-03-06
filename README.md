# Streamlit Demo App: Maps and Dropdown/Slider Interactions!

*TODO: Comment/clean up code in all *.py files and finish/link notebook for obtaining data from ACS API*

An extremely basic [Streamlit](https://www.streamlit.io/) app to demonstrate interactions with choropleth maps using dropdown menus and sliders -- specifically, breaking down Philadelphia zip codes by cases and principals due of residential tax delinquencies against census metrics such as median income, poverty level, and unemployment rate.

[Delinquency data](https://www.opendataphilly.org/dataset/property-tax-delinquencies) in **real_estate_tax_delinquencies.csv** and [zip code polygon data](https://www.opendataphilly.org/dataset/zip-codes) in **Zipcodes_Poly.geojson** from OpenDataPhilly.

Census data in **acs_metrics.csv** obtained from the [American Community Survey (ACS) 1-Year Data API](https://www.census.gov/data/developers/data-sets/acs-1year.html) from the United States Census Bureau. See (notebook to be organized and linked) for details on obtaining data from this API.

Check out the app [here](https://share.streamlit.io/douglaswlee/streamlit-map-demo/app.py).