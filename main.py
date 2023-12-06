# Import Needed Librarys
import streamlit as st
import difficulty_adjustment_report
import ai_agent
import weekly_market_update

# Initialize the AI agent
chat_llm_chain = ai_agent.init_ai_agent()
vision_llm_chain = ai_agent.init_ai_agent()

# Start Report Generation
st.title('Agent 21 Newsletter Generator')

# Report type selection
report_type = st.selectbox('Select Report Type', ['Difficulty Report', 'Weekly Market Update'])

# Input for news stories as a single string
news_stories = ''
if report_type == 'Weekly Market Update':
    news_stories = st.text_input('Enter News Stories (comma-separated)')

# Report generation trigger
if st.button('Generate Report'):
    if report_type == 'Difficulty Report':
        report = difficulty_adjustment_report.generate_full_report(chat_llm_chain)
    elif report_type == 'Weekly Market Update':
        # Pass news stories as a single string
        report = weekly_market_update.generate_full_report(chat_llm_chain, news_stories)
    st.text(report)  # Display the generated report
