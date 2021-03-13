import streamlit as st
import pandas as pd
import numpy as np

@st.cache(allow_output_mutation = True, show_spinner=False)
def preprocess():
    df = pd.read_csv('real_estate_tax_delinquencies.csv')
    df = df[(df['building_category'] == 'residential')&(df['is_actionable']==True)]
    return df

@st.cache(allow_output_mutation = True, show_spinner=False)
def preprocess_acs():
    df = pd.read_csv('acs_metrics.csv')
    df = df.apply(pd.to_numeric)
    df[df < 0] = np.nan
    df = df.reset_index()
    return df

@st.cache(allow_output_mutation = True, show_spinner=False)
def filter_zip(df, metric):
    if metric == 'Total Accounts':
        return df['zip_code'].value_counts()
    else:
        return df.groupby('zip_code')['principal_due'].sum().sort_values(ascending=False)

def _max_width_():
    max_width_str = f"max-width: 1100px;"
    st.markdown(
        f"""
    <style>
    .reportview-container .main .block-container{{
        {max_width_str}
    }}
    </style>    
    """,
        unsafe_allow_html=True,
    )