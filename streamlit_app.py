import streamlit
import pandas

streamlit.title("Menu")
streamlit.header("Breakfast Menu")
streamlit.text("Kale and eggs")

fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(fruit_list)
