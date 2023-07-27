# main Python app
import streamlit as st
import streamlit.components.v1 as stc

from ml_page import run_ml_app

html_temp = """
            <div style="background-color:#3872fb;padding:10px;border-radius:10px">
		    <h1 style="color:white;text-align:center;">Sleep Disorder Prediction App </h1>
		    <h4 style="color:white;text-align:center;">Terrarium Team</h4>
		    </div>
            """

desc_temp = """
            ### Sleep Disorder Prediction App
            This app will be used to predict if a person with condition is having sleeping disorder
            #### Data Source
            - TBA
            #### App Content
            - Exploratory Data Analysis
            - Machine Learning Section
            """

def main():
    stc.html(html_temp)

    menu = ["Home","Machine Learning"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Home":
        st.subheader("Home")
        st.markdown(desc_temp, unsafe_allow_html=True)
    elif choice == "Machine Learning":
        run_ml_app()
    

if __name__ == '__main__':
    main()