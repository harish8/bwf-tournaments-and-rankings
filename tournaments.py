# AUTOGENERATED! DO NOT EDIT! File to edit: tournaments_eda.ipynb.

# %% auto 0
__all__ = []

# %% tournaments_eda.ipynb 2
# import the neccessary packages
import streamlit as st

from streamlit_jupyter import StreamlitPatcher, tqdm

import pandas as pd
import io


# %% tournaments_eda.ipynb 4
st.title("BWF Tournaments")

# %% tournaments_eda.ipynb 5
st.markdown(f" ## Fetch the data from csv file and store it in a variable.")

# %% tournaments_eda.ipynb 6
tournaments_df = pd.read_csv('./data/tournaments.csv', index_col=0)

# %% tournaments_eda.ipynb 7
# To display the output in your Streamlit app, pipe the output of df.info to a buffer instead of sys.stdout, 
# get the buffer content, and display it with st.text like so:
buffer = io.StringIO()
tournaments_df.info(buf=buffer)
df_tournaments_info = buffer.getvalue()

st.text(df_tournaments_info)

# %% tournaments_eda.ipynb 8
st.write(tournaments_df.describe())

# %% tournaments_eda.ipynb 9
st.markdown(
"""
As we see the total count for each column other than type is 325. And the total count in Type is only 250. so need to figure out what types are missing and how to fill those or remove those if necessary. 

Aditionally from the original dataset there's no index column. let's start with adding index column to the dataframe. 
"""
)

# %% tournaments_eda.ipynb 10
# add a new integer index column to the dataframe
tournaments_df.reset_index(inplace=True)
tournaments_df = tournaments_df.rename_axis('Index')

# %% tournaments_eda.ipynb 11
st.write(tournaments_df.head())

# %% tournaments_eda.ipynb 12
st.markdown(
"""
Now we have added the proper integier index column let's focus on missing values in type.  
"""
)

# %% tournaments_eda.ipynb 13
# find if there's any missing values. 
tournaments_df[tournaments_df.isna().any(axis=1)]
