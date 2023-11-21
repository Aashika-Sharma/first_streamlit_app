import streamlit

streamlit.title('My Parents new healthy diner')

streamlit.header(' 🥣 Breakfast Menu')
streamlit.text(' 🥗 Omega 3 and blueberry oatmeal')
streamlit.text(' 🐔 Kale,Spinach and Rocket smoothie')
streamlit.text('🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import python 
my_fruit_list = pandas.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')
streamlit.dataframe(my_fruit_list)
