from os import name
import streamlit as st
import random
import tkinter as tk

st.header("Woodloo ")
st.title("Guessing The Words")
st.write("Welcome to Woodloo")



def main():
    name = st.text_input("Enter your name:")

if name:
        st.write(f"Hello Champ!")

if __name__ == "__main__":
    main()

import streamlit as st

def main():    
    answer = st.radio("Are You ready?", ("Yes", "No"))
    if answer == "No":
        st.write("so why are you here?! hehe")
    elif answer == "Yes":
        st.write("start playing!")
        st.write("You have 3 hints to the secret word, then you'll have to guess it.!")

if __name__ == "__main__":
    main()

def start_game():
    st.write("Game started!")

def main():
    st.title("Test Yourself")
if st.button("Start Game"):
        start_game()

if __name__ == "__main__":
    main()

if __name__ == "__main__":
    main()

