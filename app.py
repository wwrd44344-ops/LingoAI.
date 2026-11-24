
import streamlit as st

st.set_page_config(page_title="LingoAI", page_icon="📚")

st.title("🌟 LingoAI")

st.subheader("Your Smart English Writing Assistant")

st.write("Write your English sentence below:")

sentence = st.text_area("English Sentence")

if st.button("Correct My Sentence"):
    if sentence:
        st.success("Your sentence has been received!")
    else:
        st.warning("Please write a sentence first.")
