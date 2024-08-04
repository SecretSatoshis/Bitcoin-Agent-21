# Import Needed Libraries
import streamlit as st
import difficulty_adjustment_report
import ai_agent
import weekly_market_update
import weekly_bitcoin_recap

# Initialize the AI agent
chat_llm_chain = ai_agent.init_ai_agent()
vision_llm_chain = ai_agent.init_ai_agent()

# Start Report Generation
st.title('Secret Satoshis Bitcoin Agent 21 Newsletter Application')

# Report type selection
report_type = st.selectbox('Select Newsletter Type', ['Difficulty Report', 'Weekly Market Update', 'Weekly Bitcoin Recap'])

# Input for news stories as a single string
news_stories = ''
if report_type in ['Weekly Market Update', 'Weekly Bitcoin Recap']:  # Check for either report that requires news input
    news_stories = st.text_input('Enter News Stories (comma-separated)')

# Input for date for narrative as a single string
report_date = ''
if report_type in ['Weekly Bitcoin Recap']:  # Check for either report that requires news input
  report_date = st.text_input('Enter Date (YYYY-MM-DD)')

# File uploader for the weekly Bitcoin chart
weekly_bitcoin_chart = None
if report_type == 'Weekly Bitcoin Recap':
    weekly_bitcoin_chart = st.file_uploader("Upload Weekly Bitcoin Chart (.png)", type=["png"])

# Report generation trigger
if st.button('Generate Report'):
    if report_type == 'Difficulty Report':
        report = difficulty_adjustment_report.generate_full_report(chat_llm_chain)
    elif report_type == 'Weekly Market Update':
        # Pass news stories as a single string
        report = weekly_market_update.generate_full_report(chat_llm_chain, news_stories)
    elif report_type == 'Weekly Bitcoin Recap':  
        if weekly_bitcoin_chart:
          # Generate the report
          report = weekly_bitcoin_recap.generate_full_report(chat_llm_chain, news_stories, report_date, weekly_bitcoin_chart)
    st.text_area("Weekly Bitcoin Recap", report)
