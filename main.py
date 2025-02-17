import streamlit as st
import weekly_bitcoin_recap
import datetime

# Start Report Generation
st.title("Secret Satoshis Bitcoin Agent 21 Newsletter Application")

# Input for news stories
news_stories = st.text_area("Enter News Stories")

# Input for report date
report_date = st.text_input(
    "Enter Date (YYYY-MM-DD)", value=datetime.date.today().strftime("%Y-%m-%d")
)

# File uploader for weekly Bitcoin chart (accepts image uploads)
uploaded_image = st.file_uploader(
    "Upload Weekly Bitcoin Chart (.png, .jpg, .jpeg)", type=["png", "jpg", "jpeg"]
)

# Report generation trigger
if st.button("Generate Report"):
    if uploaded_image:
        # Generate the Weekly Bitcoin Recap report
        report = weekly_bitcoin_recap.generate_full_report(
            news_stories,
            report_date,
            uploaded_image,
            weekly_bitcoin_recap.REVIEW_PROMPT,
        )
        # Display the generated report
        st.text_area("Weekly Bitcoin Recap", report, height=600)
    else:
        st.warning("Please upload a weekly Bitcoin chart.")
