import streamlit as st

from Intro.intro import intro
from Advanced.advanced import advanced


def main():
    st.header("Github Actions")

    menu = [
        "Intro", "Advanced"
    ]

    sub_page = st.sidebar.selectbox("Menu", menu)

    if sub_page == "Intro":
        intro()
    if sub_page == "Advanced":
        advanced()


if __name__ == "__main__":
    main()
