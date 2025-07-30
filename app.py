import streamlit as st
import openai
import fitz 

st.set_page_config(page_title="AI Resume Critique Tool")

client = openai.OpenAI(
    api_key=st.secrets["OPENAI_API_KEY"] if "OPENAI_API_KEY" in st.secrets else "sk-..."
)

st.title("🤖 AI Resume Critique Tool")
st.markdown("Upload your resume (PDF) and let AI help you improve it!")

def extract_text_from_pdf(pdf_file):
    doc = fitz.open(stream=pdf_file.read(), filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    return text
def get_resume_feedback(resume_text):
    prompt = f"""
    You are an expert career coach. Analyze the following resume and give improvement suggestions:
    1. Grammar and formatting
    2. Missing sections
    3. Keyword optimization
    4. Overall tone and effectiveness

    Resume:
    {resume_text}
    """
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

uploaded_file = st.file_uploader("Upload your resume (PDF)", type="pdf")

if uploaded_file:
    with st.spinner("Analyzing your resume..."):
        resume_text = extract_text_from_pdf(uploaded_file)
        if resume_text.strip():
            feedback = get_resume_feedback(resume_text)
            st.subheader("📋 AI Feedback:")
            st.write(feedback)
        else:
            st.error("Could not extract text from the uploaded PDF.")

        
