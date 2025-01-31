import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="India Data Visualization",
    page_icon="🌏",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("All about India")
df = pd.read_csv('ind')
list_of_states =list(df['State'].unique())
list_of_states.insert(0 , 'Overall India')

st.sidebar.title("India ka Data Vsiualization")

selected_state = st.sidebar.selectbox('Select a Stae' ,list_of_states)
primary = st.sidebar.selectbox('Select a Primary Parameter',sorted(df.columns[5:]))
secondary = st.sidebar.selectbox('Select a secondary Parameter',sorted(df.columns[5:]))

plot = st.sidebar.button('plot Graph')
if plot:
    if selected_state == 'Overall India':
        fig = px.scatter_mapbox(df ,lat='Latitude',
                                lon= 'Longitude',
                                size = primary ,
                                color = secondary,
                                zoom = 4,
                                size_max = 35 ,
                                mapbox_style = "open-street-map",
                                width = 1200 ,
                                height = 700 ,
                                hover_name= "District",
                                color_continuous_scale = ["violet" ,"indigo" ,"blue","green","yellow","orange" ,"red"])
        fig.update_layout(
            mapbox_center = {"lat":20.5937 ,"lon":78.9629},
            dragmode ="zoom" ,autosize =True)
        st.plotly_chart(fig, use_container_width=True)

    else:
        state_df = df[df['State'] == selected_state]
        fig = px.scatter_mapbox(state_df,
                                lat='Latitude',
                                lon='Longitude',
                                size=primary,
                                color=secondary,
                                zoom= 5,

                                size_max=30,
                                mapbox_style="carto-positron",
                                width=1200,
                                height=700,
                                hover_name="District",
                                color_continuous_scale = ["violet" ,"indigo" ,"blue","green","yellow","orange" ,"red"])
        fig.update_layout(dragmode="zoom", autosize=True)
        st.plotly_chart(fig ,use_container_width=True)