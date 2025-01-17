# Bitcoin Agent 21

This repository contains the code for generating the **Weekly Bitcoin Recap**, a weekly newsletter for the Secret Satoshis community. It provides a focused analysis of Bitcoin's weekly market performance, price trends, on-chain activity, and valuation metrics. 

## About the Project

The Weekly Bitcoin Recap is created using **Bitcoin Agent 21**, a Bitcoin AI Agent developed by Secret Satoshis. It compiles data from curated Bitcoin datasets and user-provided inputs, such as news stories and Bitcoin price charts, into a structured newsletter. The system uses the **OpenAI Agent API** to streamline content generation and review processes.

### Data Sources
The newsletter is powered by data from Secret Satoshis github repositories:
- [Bitcoin Report Library](https://secretsatoshis.github.io/Bitcoin-Report-Library/)

## Installation and Setup

### Clone the Repository
```bash
git clone https://github.com/SecretSatoshis/Weekly-Bitcoin-Recap
cd Weekly-Bitcoin-Recap
```

### Install Dependencies
Make sure Python is installed, then run:
```bash
pip install -r requirements.txt
```

### Configure OpenAI API Key
Replace the placeholder in the code with your OpenAI API key:
```python
client = openai.OpenAI(api_key="your-api-key")
```

## Usage

1. **Run the Application**:
   Launch the application using Streamlit:
   ```bash
   streamlit run main.py
   ```

2. **Provide Input**:
   - Add **news stories** relevant to Bitcoin for inclusion in the analysis.
   - Enter the **report date** for context.
   - Upload a **Bitcoin price chart** to include technical analysis.

3. **Generate the Report**:
   Click "Generate Report" to produce the Weekly Bitcoin Recap. The output will be displayed in the app and saved as a `.txt` file.

## About Secret Satoshis

The Secret Satoshis platform is dedicated to Bitcoin education and analysis. The Bitcoin Agent 21 tool is part of a larger suite of resources designed to empower the community with actionable Bitcoin insights.

## License

This project is licensed under the **GPLv3 License**. See the [LICENSE](LICENSE) file for details.
