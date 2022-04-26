from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

st.set_page_config(page_title="Marine Protected Areas", page_icon="🌊", layout="centered", initial_sidebar_state="auto", menu_items=None)

"""
# Welcome to Marine Protected Areas Project!
This website is here to introduce you to Marine protected areas and guide you through the Flickr dataset about the MPAs...

Below you can see how awesome the Streamlit app is :P
"""

with st.echo(code_location='below'):
    total_points = st.slider("Number of points in spiral", 1, 5000, 2000)
    num_turns = st.slider("Number of turns in spiral", 1, 100, 9)

    Point = namedtuple('Point', 'x y')
    data = []

    points_per_turn = total_points / num_turns

    for curr_point_num in range(total_points):
        curr_turn, i = divmod(curr_point_num, points_per_turn)
        angle = (curr_turn + 1) * 2 * math.pi * i / points_per_turn
        radius = curr_point_num / total_points
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        data.append(Point(x, y))

    st.altair_chart(alt.Chart(pd.DataFrame(data), height=500, width=500)
        .mark_circle(color='#0068c9', opacity=0.5)
        .encode(x='x:Q', y='y:Q'))
        
st.markdown("## Introduction")
'''
Text for intro
'''
st.markdown("## Basic statistics")
'''
Text for basic stats
'''
st.markdown("## Data Analysis")
'''
Text for data analysis
'''
st.markdown("### Temporal Data")
'''
Text for Temporal data
'''
st.markdown("### Spatial Data")
'''
Text for spatial data
'''
st.markdown("### Machine Learning")
'''
Text for machine learning
'''
st.markdown("### Conclusion")
'''
Text for conclusion
'''