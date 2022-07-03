# -*- coding: utf-8 -*-
"""
Created on Sun Jul  3 12:43:35 2022

@author: Ed.Morris
"""

# Portfolio home page

import streamlit as st

#######################
# Dashboard config
#######################

st.set_page_config(page_title = 'Home', page_icon = '🏠', layout = 'wide')

st.write("""
          # Sports Analytics Portfolio ⚽🏀🎾⛳
          """)

st.markdown("""
            Welcome to my Sports Analytics Portfolio Dashboard.
            \n Use the arrow in the top left to open the sidebar.
            \n In the "Portfolio" page, you will be able to find examples of my analyses.
            \n Feel free to keep up to date with my work by following my socials, or get in touch via email.
            
    ### Contact:
    - **Email:** datawithed@outlook.com
            
    ### Socials:
    - **Twitter:** @datawithed
    - **Instagram:** @data_with_ed
            """)
