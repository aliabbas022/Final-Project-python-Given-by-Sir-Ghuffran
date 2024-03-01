from os import name
import streamlit as st
import random
import tkinter as tk

st.header("Woodloo ")
st.title("Guessing The Words")
st.write("Welcome to Woodloo")
def start_game():
    st.write("Game started!")
def main():
    st.title("Test Yourself")
if st.button("Start Game"):
        start_game()

if __name__ == "__main__":
    main()



def main():
    name = st.text_input("Enter your name:")

if name:
        st.write(f"Hello Champ!")

if __name__ == "__main__":
    main()

