import streamlit as st
import requests

st.title("IntelliLoan Document Processor")

# File uploader
uploaded_file = st.file_uploader("Choose a file", type=["jpg", "jpeg", "png"])

# Check if a file has been uploaded
if uploaded_file is not None:
    st.image(uploaded_file, caption='Uploaded Image', use_column_width=True)

    if st.button("Process"):
        # Convert file to format required by requests
        files = {
            "file": (uploaded_file.name, uploaded_file.getvalue(), uploaded_file.type)
        }

        try:
            response = requests.post("http://localhost:8000/upload/", files=files)
            result = response.json()
            st.write("📄 Extracted Text:")
            st.code(result.get("extracted_text", "No text found."))
            st.write("Raw server response:")
            st.json(result)
        except Exception as e:
            st.error("❌ Failed to process document.")
            st.code(response.text)
            st.exception(e)
            