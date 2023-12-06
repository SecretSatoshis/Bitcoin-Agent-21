# Project Title: Agent 21 Newsletter Writer

## Description
Agent 21 is an advanced tool designed for creating specialized Bitcoin newsletters. It leverages AI agents to analyze market and on-chain data to generate insightful and data-driven reports. The tool offers two main types of reports: Difficulty Adjustment Reports and Weekly Market Updates.

## Features
- **User-Friendly Interface**: Built with Streamlit for intuitive user interaction.
- **Two Report Types**: Options to generate either a 'Difficulty Report' or a 'Weekly Market Update'.
- **Custom AI Agents**: Uses specialized AI agents (`chat_llm_chain` and `vision_llm_chain`) for processing and report generation.
- **Personalized Input**: Capability to incorporate user-input news stories into reports.
- **Data-Driven Insights**: AI agents employ a various financial dataset for comprehensive market insights.

## Installation and Setup
- **Requirements**: Python, Streamlit, and dependencies listed in `requirements.txt`.
- **API Key Configuration**: The tool requires configuration with an OpenAI API key for full functionality.

## Usage
- **Application Launch**: Run the replit applicatoin or run the main.py file in local enviroment.

## AI Agent and Report Generation

### AI Agent Configuration
The AI agent configuration in the Agent 21 Newsletter Generator is a crucial aspect of its functionality. It involves setting up two specialized AI agents, `chat_llm_chain` and `vision_llm_chain`, integrated with OpenAI's GPT-4 model. These agents are central to the application's ability to process and analyze data:

- **Textual Data Processing (`chat_llm_chain`)**: This AI agent is responsible for generating textual content for the reports. It is configured with a specific prompt template that guides its content generation, ensuring that the output adheres to the style and tone of Agent 21's persona. The agent is designed to provide insightful and authoritative analysis, making it an integral part of the report generation process.

- **Visual Data Analysis (`vision_llm_chain`)**: This agent is tasked with interpreting and analyzing visual data, such as charts and graphs. It plays a key role in generating the Weekly Market Update reports, where visual data interpretation is crucial.

### Report Modules Description
The application features two main report modules, each designed to cater to different aspects of Bitcoin market analysis:

- **`difficulty_adjustment_report.py`**: This module generates the Difficulty Adjustment Report. It pulls data from predefined URLs and utilizes various functions to create a summary, performance analysis, and fundamentals overview. Each section is carefully crafted to provide a comprehensive view of Bitcoin's difficulty adjustment and its implications on the market.

- **`weekly_market_update.py`**: This module is responsible for creating the Weekly Market Update reports. It focuses on a range of analyses including market summaries, trading performance, historical performance, and news impact. This module integrates various data sources and employs specialized functions to present a detailed overview of the current state of the Bitcoin market.

## AI Persona: Agent 21 Overview
Agent 21 is conceptualized as a highly knowledgeable and experienced Bitcoin Investment Analyst, serving as the cornerstone of the report generation process:

- **Background and Education**: Agent 21 is portrayed as having an extensive educational background in economics and finance, with a specific focus on Bitcoin and blockchain technology. This includes degrees from prestigious institutions and specialized training in Bitcoin investments.
- **Professional Experience and Certifications**: The persona boasts a rich professional history in investment analysis, portfolio management, and financial planning. Agent 21 is characterized as having top-tier certifications like CFA and CFP, emphasizing a deep understanding of both traditional and bitcoin-centric investment strategies.
- **Skills and Traits**: Agent 21 is equipped with a blend of analytical and technical skills, proficient in market trend analysis and blockchain technology. The persona also demonstrates strong research capabilities and effective communication skills, making complex investment strategies understandable to a broad audience.
- **Investment Framework and Philosophy**: This AI persona operates under a well-defined investment framework that incorporates a first-principles approach to Bitcoin investment, emphasizing the cryptocurrency's unique attributes, market dynamics, and technological advancements.
- **Narrative Tone and Writing Style**: Agent 21's narrative style is knowledgeable and authoritative, reflecting a high level of expertise, yet remains approachable and clear to ensure accessibility for all levels of Bitcoin investors.
- **Content Goal and Target Audience**: The primary aim is to cater to long-term Bitcoin investors who value deep, fundamental analysis and a technology-focused approach. The content is designed to be insightful for both seasoned investors and newcomers to the Bitcoin market.

## Instructions for AI Persona Use
The use of Agent 21 within the report generation process follows specific guidelines to ensure accuracy, relevance, and integrity:

- **Data-Driven Analysis**: Agent 21's analysis is firmly rooted in historical data and current market trends. This includes a thorough examination of market patterns, transactional activities, and other key metrics that influence Bitcoin's market behavior.
- **Avoiding Speculation**: The persona is designed to avoid speculative language, focusing instead on logical reasoning and evidence-based conclusions. This approach ensures that the insights and recommendations are grounded in solid data and factual information.
- **Clear and Decisive Language**: The content generated by Agent 21 is characterized by assertiveness and clarity. Recommendations and insights are presented in a decisive manner, offering concrete and actionable advice to investors.
- **Adherence to Template and Style**: Agent 21 consistently adheres to a predefined template and style guide. This ensures that all generated content maintains a professional, balanced, and concise format, aligning with the overall tone and objectives of the report.

## Workflow Overview

### Data Gathering
The data gathering process is automated, pulling information from Secret Satoshis data sources. These sources are specified within the script via URLs, ensuring that the reports are based on up-to-date and relevant market data.

### Report Section Generation
Each report section is generated using specific functions that process CSV data and narrative templates. These functions are tailored to ensure consistency and accuracy in the report's content, adhering to the predefined structure and format.

### Content Generation with AI Agent
The `chat_llm_chain` AI agent is employed to generate initial drafts for each report section. This process involves feeding input data and narrative templates to the AI agent, which then produces content drafts that serve as the basis for each report section.

### Editing and Analysis of Generated Content
Once the AI agent generates the initial content, it undergoes a phase of editing and analysis. This phase is critical to ensure the accuracy, coherence, and alignment of the content with the project's objectives. It involves cross-verifying data points, logical assessment of insights, and refining the narrative to match Agent 21's authoritative yet approachable tone.

### Compilation of the Full Report
The final step in the workflow is the compilation of the full report. This involves combining the executive summary, individual sections, conclusion, signature, and disclaimer into a cohesive and polished document.

### Final Report Output
The final output from the Agent 21 Newsletter Generator is a comprehensive, data-driven report. These reports provide in-depth insights into various aspects of Bitcoin's market and network health, making them invaluable tools for investors and analysts in the cryptocurrency space.

## Report Generation Objectives for Difficulty Adjustment Report
The Difficulty Adjustment Report offers a comprehensive analysis of Bitcoin's mining and market dynamics, focusing on key aspects that influence investment decisions:

- **Difficulty Summary**: Provides an introduction to and analysis of the Bitcoin market, focusing on mining difficulty and its implications for investors.
- **Performance Analysis**: Compares Bitcoin's performance with other asset classes, offering insights into its relative market standing.
- **Fundamentals**: Analyzes key on-chain metrics such as transactional activity, miner economics, and network usage, highlighting the health and growth of the Bitcoin network.
- **Price and On-Chain Valuation**: Evaluates Bitcoin's valuation from both market and on-chain perspectives, providing a multifaceted view of its financial health.
- **Relative Valuation**: Assesses Bitcoin's potential trajectory and growth prospects by comparing it with other significant assets and monetary systems.

## Report Generation Objectives for Weekly Market Update
The Weekly Market Update provides a timely and detailed overview of the current state of the Bitcoin market, analyzing various factors that could impact short-term and long-term investment strategies:

- **Weekly Market Summary**: Offers an up-to-date overview of the Bitcoin market, encapsulating the latest trends and market sentiments.
- **Trading Week Performance**: Compares Bitcoin's performance during the past trading week with other asset classes, giving insights into its recent market behavior.
- **Historical Performance**: Reviews Bitcoin's past performance metrics, presenting a historical context to understand its long-term market trends.
- **Market Analysis**: Delivers in-depth insights into Bitcoin's current market behavior, including trading ranges and investment potential.
- **Heatmap Analysis**: Provides a visual representation of Bitcoin's performance patterns over time, aiding in the identification of market trends.
- **Fundamentals Analysis**: Examines the underlying metrics that indicate the health and growth of the Bitcoin network, such as transaction volume and active addresses.
- **News Impact**: Analyzes the potential impact of recent news stories on the Bitcoin market, offering context for how current events may influence its value and adoption.

## Bitcoin Data
The project primarily utilizes CSV files from GitHub repositories under the Secret Satoshis account, focusing on different aspects of the Bitcoin market:

- **Difficulty Adjustment Data**: 
  - Source: [Secret Satoshis - Bitcoin Difficulty Report](https://github.com/secretsatoshis/Bitcoin-Difficulty-Report)
  - Description: Data regarding Bitcoin's mining difficulty, network performance, and related metrics.

- **Weekly Market Data**: 
  - Source: [Secret Satoshis - Bitcoin Weekly Market Update](https://github.com/secretsatoshis/Bitcoin-Weekly-Market-Update)
  - Description: Weekly updates on Bitcoin’s market performance, trading metrics, and on-chain analysis.

- **Yahoo Finance**: 
  - Website: [Yahoo Finance](https://finance.yahoo.com)
  - Description: Used for obtaining traditional financial market data and indices, enabling a comparative analysis with Bitcoin and other cryptocurrencies.

- **Coinmetrics**:
  - Website: [Coinmetrics](https://coinmetrics.io)
  - Description: Offers detailed cryptocurrency network data, including on-chain metrics and market indicators.

- **CoinGecko**:
  - Website: [CoinGecko](https://www.coingecko.com)
  - API: [CoinGecko API](https://www.coingecko.com/en/api)
  - Description: Provides comprehensive data on cryptocurrencies, including price, volume, market cap, and more.

## License
- This project is licensed under the terms of the GPLv3 license.
