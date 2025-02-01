import google.generativeai as genai
import streamlit as st
import os

# Set the API key using the appropriate method (consult the API's documentation)
genai.configure(api_key="AIzaSyAlle9GSvwPtmFfuN1i1HLCccYvKT_xtjw")
# Make sure the configuration is correct, as per the API you are using

def generate_content(prompt):
    model = genai.GenerativeModel(model_name="gemini-2.0-flash-exp")
    response = model.generate_content(prompt)
    return response.text

def main():
    st.title("STARBOYS AI-powered content generator for blogging & SEO")
    st.markdown("Generate high-quality blog titles, outlines, drafts, and meta descriptions.")

    topic = st.text_input("Enter a topic or keyword:", placeholder="e.g., Benefits of yoga")

    content_type = st.selectbox("Select content type to generate:",
                                ["Blog Titles", "Outlines", "Drafts", "Meta Descriptions"])
    
    if st.button("Generate content"):
        if topic:
            with st.spinner("Generating content..."):
                if content_type == "Blog Titles":
                    prompt = f"Generate 5 creative blog titles about {topic}."
                elif content_type == "Outlines":
                    prompt = f"Generate a detailed blog outline about {topic}."
                elif content_type == "Drafts":
                    prompt = f"Write a detailed blog draft about {topic}."
                elif content_type == "Meta Descriptions":
                    prompt = f"Generate an SEO-friendly meta description about {topic}."
                else:
                    prompt = ""

                try:
                    generated_content = generate_content(prompt)
                    st.subheader(f"Generated {content_type}:")
                    st.write(generated_content)
                except Exception as e:
                    st.error(f"Error generating content: {e}")
        else:
            st.warning("Please enter a topic or keyword!")

if __name__ == "__main__":
    main()
