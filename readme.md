# Agent 21 Newsletter Writer

## Description
**Agent 21** is a tool designed to generate specialized Bitcoin newsletters by leveraging AI agents for analyzing market data and on-chain metrics. It produces insightful, data-driven reports, with three primary report types:
1. **Weekly Bitcoin Recap**
2. **Difficulty Adjustment Report**
3. **Weekly Market Update**

## Features
- **User-Friendly Interface**: Built with Streamlit for a simple, intuitive user experience.
- **Three Report Types**: Generate either a *Difficulty Report*, *Weekly Market Update*, or *Weekly Bitcoin Recap*.
- **Custom AI Agents**: Uses advanced AI agents (`chat_llm_chain`, `vision_llm_chain`, and `review_llm_chain`) for data processing, visual data analysis, and content editing.
- **Personalized Input**: Incorporates user-provided news stories and input data into reports.
- **Data-Driven Insights**: AI-driven analysis using various financial datasets for comprehensive insights.

## Installation and Setup

### 1. Clone the Repository
```bash
git clone https://github.com/SecretSatoshis/Bitcoin-Agent-21
cd Bitcoin-Agent-21
```

### 2. Install Dependencies
Ensure that you have Python installed, then run the following command to install all required dependencies:
```bash
pip install -r requirements.txt
```

### 3. Configure OpenAI API Key
To run the application, you'll need an OpenAI API key:
- Sign up at [OpenAI](https://beta.openai.com/signup/) to get an API key.
- The OpenAI API key is hardcoded in `ai_agent.py`. You need to replace the placeholder key in the following line with your actual OpenAI API key:
      ```
      openai_api_key = "your-api-key"
      ```

## Usage
1. **Launch the Application**
   Run the application locally using Streamlit:
   ```bash
   streamlit run main.py
   ```

2. **Generate Reports**
   Select the type of report you want to generate (Difficulty Report, Weekly Market Update, or Weekly Bitcoin Recap), enter any required input (e.g., news stories or date), and click "Generate Report".

### AI Agent Configuration

- **Text Processing** (`chat_llm_chain`): This AI agent generates the textual content of the reports, including market summaries and insights.
- **Visual Data Analysis** (`vision_llm_chain`): This agent analyzes visual data such as Bitcoin price charts and integrates the analysis into the reports.
- **Content Review** (`review_llm_chain`): The review agent is responsible for reviewing and refining the generated content to ensure coherence and quality before final output.

## Report Types

### 1. **Difficulty Adjustment Report** (`difficulty_adjustment_report.py`):
   - Provides an overview of Bitcoin’s mining difficulty and market performance.
   - Summarizes performance analysis and key on-chain fundamentals.

### 2. **Weekly Market Update** (`weekly_market_update.py`):
   - A comprehensive summary of Bitcoin’s weekly market activity.
   - Includes market performance, historical trends, and analysis of the latest news impacts.

### 3. **Weekly Bitcoin Recap** (`weekly_bitcoin_recap.py`):
   - Focuses on Bitcoin’s weekly trading activity, price movements, and market outlook.
   - Integrates uploaded charts and visual data into the analysis.
   - Summarizes key news stories, market sentiment, and provides a forward-looking outlook.

## Workflow Overview

### Data Gathering
- The application gathers data from external sources such as CSV files hosted on Secret Satoshis and other financial data repositories.
- This ensures the reports are built using up-to-date market information.

### Report Generation
- Each section of the report is created using pre-defined templates that ensure consistency and accuracy.
- Reports are customized based on user inputs (e.g., news stories, dates, images).

### AI-Powered Content Creation and Review
- **Initial Draft Generation**: The `chat_llm_chain` generates the first draft for each report section.
- **Content Review**: The `review_llm_chain` is responsible for refining and ensuring the accuracy of the generated content before final output.

### Final Report Compilation
- All sections are compiled, including news summaries, visual data analysis, performance summaries, and a concluding outlook.
- The final report is output as a complete document with all relevant insights.

## Data Sources
- **Bitcoin Difficulty Report**: [Secret Satoshis - Bitcoin Difficulty Report](https://github.com/SecretSatoshis/Bitcoin-Difficulty-Report)
- **Weekly Market Update**: [Secret Satoshis - Bitcoin Weekly Market Update](https://github.com/SecretSatoshis/Bitcoin-Weekly-Market-Update)
- **Additional Data Sources**:
   - Yahoo Finance (for traditional market comparisons)
   - Coinmetrics (on-chain and market data)
   - CoinGecko (comprehensive cryptocurrency data)

## License
This project is licensed under the terms of the **GPLv3** license.
