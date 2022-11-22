import streamlit as st

from Intro.intro import intro


def main():
    st.header("Github Actions")

    menu = [
        "Intro",
    ]

    sub_page = st.sidebar.selectbox("Menu", menu)

    if sub_page == "Intro":
        intro()


if __name__ == "__main__":
    main()
