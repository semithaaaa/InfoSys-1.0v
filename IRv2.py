import streamlit as st
from ir_vsm import search_vsm, search_qlm_jm, tfidf_matrix, vectorizer, file_names, doc_term_probs, collection_term_probs

# Custom CSS for styling (modified for centered bottom image)
st.markdown("""
    <style>
        .title-text {
            font-size: 2.5em;
            font-weight: bold;
            text-align: center;
            color: #2F4F4F;
        }
        .header-image-container {
            display: flex;
            justify-content: center;
            margin-bottom: 20px;
        }
        .header-image-container img {
            width: 50%;
        }
        .credit-text {
            text-align: center;
            font-size: 1.2em;
            color: #555555;
            margin-top: 50px;
        }
        .tabs-font {
            font-size: 1.1em;
        }
        #bottom-left-image {  /* Centered bottom image styles */
            position: fixed;
            bottom: 10px;          /* Distance from bottom */
            left: 50%;             /* Start at horizontal center */
            transform: translateX(-50%); /* Shift left by 50% of width */
            width: 50px;           /* Adjust image width as needed */
            height: auto;          /* Maintain aspect ratio */
            opacity: 0.7;         /* Opacity */
            z-index: 100;         /* Ensure it's on top */
        }
    </style>
""", unsafe_allow_html=True)

# Display an image at the top
st.markdown(
    '<div class="header-image-container"><img src="https://my.barton.ac.uk/digital/wp-content/uploads/sites/4/2019/09/Ted-712x321.png" alt="InfoSys 1.0v"></div>',
    unsafe_allow_html=True,
)

# Title and introduction
st.markdown('<div class="title-text">InfoSys 1.0v</div>', unsafe_allow_html=True)
st.write("Welcome to the Information Retrieval System For TedTalks!")
st.write("Higher National Diploma In Data Science 23.2 (F/T)")
st.write("InfoSys 1.0v allows you to search and retrieve documents based on your query using either the Vector Space Model (VSM) or Query Likelihood Model (QLM) with Jelinek-Mercer Smoothing.")

# Input fields
query = st.text_input("Enter your query:")
num_results = st.slider("Select the number of results to display:", 1, 20, 10)
lambda_param = st.slider("Set Jelinek-Mercer lambda parameter:", 0.0, 1.0, 0.2, 0.05)

# Tabs for VSM and QLM
tabs = st.tabs(["Vector Space Model (VSM)", "Query Likelihood Model (QLM)"])
with tabs[0]:
    st.markdown('<div class="tabs-font">### VSM - Results: ###</div>', unsafe_allow_html=True)
    if query:
        results_vsm = search_vsm(query, tfidf_matrix, vectorizer, file_names)[:num_results]
        for file_name, score in results_vsm:
            st.write(f"{file_name} - Score: {score}")

with tabs[1]:
    st.markdown('<div class="tabs-font">### QLM - Results (Jelinek-Mercer Smoothing) ###:</div>', unsafe_allow_html=True)
    if query:
        results_qlm = search_qlm_jm(query, doc_term_probs, collection_term_probs, file_names, lambda_param)[:num_results]
        for file_name, score in results_qlm:
            st.write(f"{file_name} - Score: {score}")

# Project credits
st.markdown('<div class="credit-text">Project by</div>', unsafe_allow_html=True)
st.markdown('<div class="credit-text">COHNDDS232F--001</div>', unsafe_allow_html=True)
st.markdown('<div class="credit-text">COHNDDS232F--011</div>', unsafe_allow_html=True)
st.markdown('<div class="credit-text">COHNDDS232F--020</div>', unsafe_allow_html=True)
st.markdown('<div class="credit-text">COHNDDS232F--013</div>', unsafe_allow_html=True)


# Centered bottom image
st.markdown(
    """
    <div>
        <img id="bottom-left-image" src="https://cdn0.iconfinder.com/data/icons/social-media-2092/100/social-61-512.png" alt="Social Media Icon">
    </div>
    """,
    unsafe_allow_html=True,
)