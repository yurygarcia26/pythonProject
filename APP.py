import streamlit as st
import numpy as np
import pandas as pd
from aux_function import *

#####


def main():
    st.title("Mi primer dashboard in python")
    st.header("Soy Feliz")
    st.write("Hola Mundo no Ameli")




##-------------------------------------------------------------------
login_blocks = generate_login_block()
password = login(login_blocks)

if is_authenticated(password):
    clean_blocks(login_blocks)
    main()
elif password:
    st.info("Please enter a valid password")