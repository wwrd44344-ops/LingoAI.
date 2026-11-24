import streamlit as st
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

st.set_page_config(page_title="LingoAI", page_icon="✨", layout="centered")

st.title("✨ LingoAI")
st.subheader("Your Smart English Writing Assistant")
st.write("Write your English sentence below:")

@st.cache_resource
def load_model():
    model_name = "google/flan-t5-base"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
    return tokenizer, model

with st.spinner("Loading AI model... (This takes a moment on first run)"):
    tokenizer, model = load_model()

def generate_response(prompt):
    inputs = tokenizer(prompt, return_tensors="pt", max_length=512, truncation=True)
    outputs = model.generate(**inputs, max_length=150)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

sentence = st.text_area("English Sentence", placeholder="Example: I has a book.")

if st.button("Correct My Sentence"):
    if sentence.strip():
        with st.spinner("Analyzing and correcting your sentence..."):
            corrected = generate_response(f"Correct the grammar and spelling of this English sentence: {sentence}")
            improved = generate_response(f"Rewrite this sentence to sound more natural and professional: {sentence}")
            
            st.success("Analysis Complete!")
            
            st.markdown("### ✅ Corrected Sentence:")
            st.info(corrected)
            
            st.markdown("### 💡 Better Phrasing:")
            st.write(improved)
    else:
        st.warning("Please write a sentence first.")
