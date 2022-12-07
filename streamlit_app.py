import streamlit
import pandas

streamlit.title("Menu")
streamlit.header("Breakfast Menu")
streamlit.text("Kale and eggs")

fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
fruit_list = fruit_list.set_index("Fruit")
fruit_selected = streamlit.multiselect("Pick a fruit", list(fruit_list.index), ['Avocado','Strawberries'])
streamlit.dataframe(fruit_list.loc(fruit_selected))
