
import streamlit
import pandas

streamlit.title("My parents new healthy dinner!")

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)


streamlit.header("Menu")
streamlit.text("testing...")
streamlit.text("testing..Third.!.")
