import streamlit
import pandas
import snowflake.connector
streamlit.stop()


streamlit.header('Breakfast Menu')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Advaco')

import requests
streamlit.header("Fruityvice Fruit Advice!")

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_data_row = my_cur.fetchone()

streamlit.text("Hello from Snowflake:")
streamlit.text(my_data_row)




my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * from fruit_load_list")
my_data_row = my_cur.fetchall()
streamlit.text("The fruit load list contains")
streamlit.text(my_data_row)

my_data_row = my_cur.fetchone()
streamlit.header("The fruit load list contains")
streamlit.dataframe(my_data_row)

my_cur.execute("insert into FRUIT_LOAD_LIST values ('from streamlir')")


