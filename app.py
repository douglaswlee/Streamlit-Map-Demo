import streamlit as st

import home_map
import alt_map

def main():
    DELINQUENCY_LINK = 'https://www.opendataphilly.org/dataset/property-tax-delinquencies'
    ZIPS_LINK = 'https://www.opendataphilly.org/dataset/zip-codes'
    CENSUS_API_LINK = 'https://www.census.gov/data/developers/data-sets/acs-1year.html'
    PAGES = {
        "Side-by-Side": home_map,
        "Filtered" : alt_map
    }
    st.sidebar.title('A Basic Demo with Maps: Philly Residential Tax Delinquencies & Census Metrics')
    st.sidebar.markdown(
        'Philly Zip Code Map of Actionable Residential Tax Delinquencies '
        'and Census Metrics (Median Income, Percent Below Poverty Line, Unemployment) '
        'from the American Community Survey (ACS), collected by the U.S. Census Bureau.\n\n'
        'An account is delinquent when Real Estate Tax is still unpaid on January 1 the following year the tax was due. Actionable accounts are those the City are currently working to collect.\n\n'
    )
    selection = st.sidebar.radio("Please select a page", list(PAGES.keys()))
    page = PAGES[selection]
    
    st.sidebar.markdown(
        f'''Delinquency Data: [OpenDataPhilly Property Tax Delinquencies]({DELINQUENCY_LINK})<br>'''
        f'''Census Data: [ACS API]({CENSUS_API_LINK})<br>'''
        f'''Zipcode Data: [OpenDataPhilly Zip Codes]({ZIPS_LINK})''', unsafe_allow_html=True
    )
    
    page.app()

if __name__ == '__main__':
    main()
