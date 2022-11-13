
import streamlit
import pandas

streamlit.title("My parents new healthy dinner!")

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

streamlit.dataframe(my_fruit_list)

friuts_selected = streamlit.multiselect("Pick some fruits", list(my_fruit_list.index), ['Avocado', 'Strawberries'])

fruits_to_show= streamlit.my_fruit_list.loc[fruits_selected]

streamlit.dataframe(fruits_to_show)


streamlit.header("Menu")
streamlit.text("testing...")
streamlit.text("testing..Third.!.")
