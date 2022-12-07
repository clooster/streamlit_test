import streamlit
import pandas
import requests

streamlit.title("Menu")
streamlit.header("Breakfast Menu")
streamlit.text("Kale and eggs")

fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
fruit_list = fruit_list.set_index("Fruit")
fruit_selected = streamlit.multiselect("Pick a fruit", list(fruit_list.index), ['Avocado','Strawberries'])
streamlit.dataframe(fruit_list.loc[fruit_selected])



streamlit.dataframe(fruityvice_normalized)
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + "kiwi")

fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
