import streamlit as st
import utils as util

# Set page configuration
st.set_page_config(
    page_title="Embedded Systems",
    page_icon='🤖',
    layout='centered',
    initial_sidebar_state='collapsed'
)

# Header
st.header("Embedded System AI Assistant ")


# Text input with tooltip
input_text = st.text_input("Ask me Anything", help="Type your query here")

# Columns for additional fields
col1, col2 = st.columns([5, 5])

with col1:
    language = st.selectbox('Select Language', ('C', 'C++', 'None'), index=0, help="Choose the programming language")
with col2:
    blog_style = st.selectbox('Help assistant for', ('To Generate the Code', 'Optimize the Code', 'Testing the Code', 'Generate the Text'), index=0, help="Select the type of assistance you need")

# Button to generate response with loading indicator
submit = st.button("Generate")
if submit:
    with st.spinner('Processing...'):
        output = util.getLLamaresponse(input_text, language, blog_style)
        cleaned_output = util.replace_strings_with_space(output)
        st.write(cleaned_output)

# Feedback section
st.sidebar.header("Feedback")
feedback = st.sidebar.text_area("Your feedback", help="Let us know your thoughts or report issues")
if st.sidebar.button("Submit Feedback"):
    st.sidebar.write("Thank you for your feedback!")