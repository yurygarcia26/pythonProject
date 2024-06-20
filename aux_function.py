import pandas as pd
import numpy as np
import streamlit as st

def is_authenticated(password):
    return password == "admin360"

def generate_login_block():
    block1 = st.empty()
    block2 = st.empty()

    return block1, block2

def clean_blocks(blocks):
    for block in blocks:
        block.empty()

def login(blocks):
    blocks[0].markdown("""<style> input { -webkit-text-security: disc; } </style>""", unsafe_allow_html=True)
    return blocks[1].text_input('Password')