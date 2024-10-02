import pandas as pd
import ai_agent

# URLs for Data Gathering
urls = {
    "weekly_market_summary": "https://secretsatoshis.github.io/Bitcoin-Weekly-Market-Update/weekly_summary.csv",
    "historical_performance": "https://secretsatoshis.github.io/Bitcoin-Difficulty-Report/performance_table.csv",
    "heat_map": "https://secretsatoshis.github.io/Bitcoin-Weekly-Market-Update/monthly_heatmap_data.csv",
    # "on_chain_fundamentals": 'https://secretsatoshis.github.io/Bitcoin-Difficulty-Report/fundamentals_table.csv',
    # "price_model": 'https://secretsatoshis.github.io/Bitcoin-Difficulty-Report/model_table.csv',
    # "relative_valuation": 'https://secretsatoshis.github.io/Bitcoin-Difficulty-Report/model_table.csv',
}

## Vision API Functions ---


# Function to Analyze Visual Data and Create Report Sections
def generate_and_edit_vision_content(vision_prompt, image_path, chat_llm_chain):
    # Invoke the Vision API with the provided prompt and image path
    vision_output = ai_agent.invoke_vision_api(vision_prompt, image_path)
    vision_analysis = vision_output.choices[0].message.content

    # Run Second Round Edits using the analyze_output function
    edit_prompt = analyze_output(vision_prompt, vision_analysis)
    edited_vision_output = chat_llm_chain.predict(human_input=edit_prompt)
    return edited_vision_output


# Function to perform vision analysis of bitcoin OHLC chart
def weekly_bitcoin_outlook(image):
    vision_tasks = [
        {
            "prompt": """
      Please generate a report using only the template and data provided. Write your reponse tone and narrative like you are writting for an professional bitcion hedge fund portfolio manager / investment advisor. As you structure the narrative:

      1. Strictly adhere to the provided template, ensuring each section is populated with the correct corresponding data from the image.
      2. Refrain from adding any conclusions or deviating from the provided script in any way.
      3. Your focus should be on presenting a clear, coherent narrative that aligns closely with the provided template and data.
     ----- Template Start -----

### Market Commentary: Week of [Current Week Date]

Current Price: $[Current Price]  
Weekly Performance: [Weekly Performance]%  
Range: Low $[Low Price] | High $[High Price]

Opening Price: The week opened at $[Open]
Weekly High: The peak was recorded at $[High]
Weekly Low: The lowest point reached was $[Low]
Projected Close: The closing price stands at $[Close]

Key Resistance Levels:
$[Key Resistance Level 1] (e.g., 2021 ATH)
$[Key Resistance Level 2] (e.g., All-Time High)
Key Support Levels:
$[Key Support Level 1] (e.g., 2021 ATH Monthly Close)
$[Key Support Level 2] (e.g., Bear Case EOY 2024)

### Year-End Market Outlook

Projected Outcome:
Bear Scenario Likelihood: [Bear Scenario Probability]%
Base Scenario Likelihood: [Base Scenario Probability]%
Bull Scenario Likelihood: [Bull Scenario Probability]%

Overview of the Weekly BTC/USD Chart:

1. Price Movement:
  This week, Bitcoin [observed movement], with a [change] of [Weekly Performance]%, closing at approximately $[Current Price]. This movement [interpretation based on chart analysis].
2. Candlestick Analysis:
  The weekly candle shows [candle characteristics], suggesting [interpretation based on candlestick analysis].
3. Weekly OHLC Price Chart Analysis and Market Commentary:
Provide a comprehensive analysis of the weekly OHLC (Open, High, Low, Close) chart, integrating the following aspects:

Price Movement:
Analyze the price movement over the week, highlighting the weekly open, high, low, and close. Discuss how these price points reflect the market’s strength, weakness, or indecision. Mention any significant price levels or trends observed from the chart.
Support and Resistance Analysis:
Highlight key support and resistance levels based on the chart data. Explain how these levels influence future price action and whether they represent significant barriers or potential breakouts for price movement in either direction.
Price Trends and Directionality:
Assess the current weekly price trend (uptrend, downtrend, or sideways movement) and explain how this fits within the broader market context. Offer insights on potential price directionality based on the weekly OHLC chart, and whether the chart indicates any upcoming shifts in market momentum or trend.
General Market Commentary:
Summarize the market’s overall behavior and potential outlook based on the weekly OHLC chart. Discuss how the observed trends, price patterns, and technical factors could affect the positioning of a portfolio manager, with specific insights on managing risk, identifying opportunities, and adjusting strategy as needed.

Short-Term Outlook:

Given the current market momentum, Bitcoin is likely to [anticipated action] the key support/resistance at $[Key Level]. Holding above/below this level is crucial to [anticipated result]. Conversely, [anticipated action] the $[Key Level] could [anticipated result] towards $[Next Target Level].

If current trends persist and Bitcoin [interpreted action], we might see the price [anticipated outcome] the bear case scenario of $[Bear Case Price] by the end of 2024. [Interpreted action] could position Bitcoin to align with the base case scenario of $[Base Case Price] by EOY 2024.For the bullish scenario to materialize, Bitcoin would need to [interpreted action]. This would set the stage for a potential rally towards $[Bull Case Price], supported by [positive market catalysts].

### Strategic Guidance for Investors

1.Risk Management:
Understanding the inherent volatility in Bitcoin markets is crucial. Long-term investors should focus on the broader market trends. Short-term fluctuations are common, but maintaining a long-term perspective can help navigate through the volatility.

2. Accumulate on Dips:
For long-term investors, accumulating Bitcoin during these dips, especially near strong support levels like $[Key Support Level], could be a strategic move, anticipating future bullish movements post-halving.
----- Template End -----
    """,
            "image": image,
        }
    ]

    vision_summaries = {}
    for task in vision_tasks:
        vision_output = ai_agent.invoke_vision_api(task["prompt"], task["image"])
        vision_summaries[task["prompt"]] = vision_output

    return vision_summaries


## Free Content Functions ---


def generate_news_impact_prompt(news_stories):
    # Construct the template with the news stories appended
    template = f"""
Please generate a report using the template and data provided. Write your reponse tone and narrative like you are writting for an professional bitcion hedge fund portfolio manager / investment advisor. As you structure the narrative:

1. Integrate answers to the guiding questions seamlessly within the narrative without explicitly mentioning the questions. You must answer all questoins asked do not skip any guiding questions. They will be marked by "Guiding Questions:".
2. Strictly adhere to the provided template, ensuring each section is populated with the correct corresponding data from the table.
3. Refrain from adding any conclusions or deviating from the provided script in any way.
4. Your focus should be on presenting a clear, coherent narrative that aligns closely with the provided template and data.
5. Format the provided news stories into bullet points with the news source name provided in () at the end.
6. Do not put "-" in front of each news story just txt no special formatting needed

News Stories:
{news_stories}

----- Template Start -----

News Stories:
- [First news story headline]
[What This Means for You Bullet point impact of the news story. No longer then 1 sentence.]
- [Second news story headline]
[What This Means for You Bullet point impact of the news story. No longer then 1 sentence.]
- [Next news story headline as per the provided news stories]
[What This Means for You Bullet point impact of the news story. No longer then 1 sentence.]

News Impact:
Given the above news stories, the potential impact on Bitcoin's price and overall adoption can be summarized as follows:
[Provide a summary of the expected bitcoin price impact based on news stories]

Guiding Questions:
- What cumulative impact could these news stories have on investor sentiment and genreal bitcoin market trends and performance?

----- Recap of Expectations -----
To ensure the effectiveness of the narrative:
- Strictly follow the provided template structure.
- Focus on clear, coherent reporting without deviations.

"""
    return template


# Function to generate and edit news contentsection
def generate_and_edit_news_content(chat_llm_chain, review_llm_chain, news_stories):
    # Generate initial prompt with news stories
    initial_prompt = generate_news_impact_prompt(news_stories)

    # Get initial output from the AI model
    initial_output = chat_llm_chain.predict(human_input=initial_prompt)

    # Run Second Round Edits using the analyze_output function
    edit_prompt = analyze_output(initial_prompt, initial_output)
    edited_output = review_llm_chain.predict(human_input=edit_prompt)

    return edited_output


# Create Weekly Bitcoin Recap
def generate_weekly_bitcoin_recap_prompt(data_path):
    # Read the data from the CSV file
    df = pd.read_csv(data_path)

    # Convert the dataframe to a formatted string
    table_string = df.to_string(index=False)

    # Construct the template with the table data appended
    template = """
Please generate a report using the template and data provided. Write your reponse tone and narrative like you are writting for an professional bitcion hedge fund portfolio manager / investment advisor. As you structure the narrative:

1. Strictly adhere to the provided template, ensuring each section is populated with the correct corresponding data from the table.
2. Refrain from adding any conclusions or deviating from the provided script in any way.
3. Your focus should be on presenting a clear, coherent narrative that aligns closely with the provided template and data.

Data:
{}

----- Template Start -----

Current State Of The Bitcoin Market

On [Report Date], the market capitalization of Bitcoin is currently valued at [Market Cap], with the price per Bitcoin at [Bitcoin Price USD]. This price translates to a value of [Sats per Dollar] satoshis per US dollar. Satoshis per US Dollar represents the number of satoshis—the smallest unit of Bitcoin—that one US dollar can purchase. 

Bitcoin currently holds a [Bitcoin Dominance Percentage]% share of the total cryptocurrency market. This level of dominance [indicates Bitcoin’s growing/receding] influence compared to alternative cryptocurrencies.

The 24-hour trading volume is [Bitcoin Trading Volume] billion, highlighting the [intensity/moderation] of trading activity.

Current market sentiment is characterized as [Bitcoin Market Sentiment], with the overall market trend described as [Bitcoin Market Trend].

Bitcoin’s valuation is categorized as [Bitcoin Valuation], suggesting that the market views Bitcoin as [undervalued/fairly valued/overvalued].

----- Recap of Expectations -----
To ensure the effectiveness of the narrative:
- Strictly follow the provided template structure.
- Focus on clear, coherent reporting without deviations.
    """.format(table_string)
    return template


# Create Performance Report Content
def generate_historical_performance_prompt(data_path):
    # Read the data from the CSV file
    df = pd.read_csv(data_path)

    # Convert the dataframe to a formatted string
    table_string = df.to_string(index=False)

    # Construct the template with the table data appended
    template = """
Please generate a report using the template and data provided. Write your reponse tone and narrative like you are writting for an professional bitcion hedge fund portfolio manager / investment advisor. As you structure the narrative:

1. Integrate answers to the guiding questions seamlessly within the narrative without explicitly mentioning the questions. You must answer all questoins asked do not skip any guiding questions. They will be marked by "Guiding Questions:".
2. Strictly adhere to the provided template, ensuring each section is populated with the correct corresponding data from the table.
3. Refrain from adding any conclusions or deviating from the provided script in any way.
4. Your focus should be on presenting a clear, coherent narrative that aligns closely with the provided template and data.

Data:
{}

----- Template Start -----

Bitcoin’s year-to-date return of [YTD Return]% provides a reference point for the performance of traditional financial indexes and asset classes.

Current Performance Snapshot

Recent 7-Day Return: [7-Day Return]%
Month-to-Date Return: [Month-to-Date Return]%
90-Day Growth: [90-Day Growth]%
Year-to-Date Return: [YTD Return]%

Historical Performance

Taking a glance at the historical data, Bitcoin has a year-to-date return of [YTD Return]. 

YTD Performance Comparison:
Bitcoin’s year-to-date return of [YTD Return]% compared to the Nasdaq (at [Nasdaq YTD Return]%) and the S&P 500 (at [S&P 500 YTD Return]%) offers insight into Bitcoin’s performance relative to the broader equity markets. [Interpretation based on Bitcoin's relative performance to these indexes].
Sector-Specific ETFs Comparison:
The returns of sector-focused ETFs like the XLF Financials ETF (at [XLF YTD Return]%), the FANG+ ETF (at [FANG+ ETF YTD Return]%), and the BITQ Crypto Industry ETF (at [BITQ YTD Return]%) give insight into how Bitcoin’s performance compares to both traditional sectors and crypto-related assets. [Interpretation based on Bitcoin's relative performance to these indexes].
Commodities and Safe-Haven Assets:
Comparing Bitcoin to Gold (with a YTD return of [Gold YTD Return]%), the Bloomberg Commodity Index (at [Bloomberg Commodity YTD Return]%), the TLT Treasury Index (at [TLT YTD Return]%), and the US Dollar Index (DXY) (at [US Dollar YTD Return]%) highlights its relationship with traditional safe-haven and low-risk assets. [Interpretation based on Bitcoin's relative performance to these indexes].

Bitcoin’s [YTD Return]% compared to traditional indexes like the Nasdaq and S&P 500 highlights its [relative performance]. This comparison positions Bitcoin as [interpretation based on growth, diversification, or other factors]. Its returns relative to sector ETFs and safe-haven assets such as Gold [potential insights], which could inform portfolio positioning for [growth/diversification/other considerations].

----- Recap of Expectations -----
To ensure the effectiveness of the narrative:
- Format all percentages to two decimal places and always use a % following percentage values.
- Seamlessly integrate all guiding questions.
- Strictly follow the provided template structure.
- Focus on clear, coherent reporting without deviations.
    """.format(table_string, table_string)
    return template


# Create Heatmap Report
def generate_heatmap_prompt(data_path, report_date):
    # Read the data from the single CSV file
    df = pd.read_csv(data_path)

    # Convert the dataframe to a formatted string
    table_string = df.to_string(index=False)

    # Construct the template with the table data appended
    template = """
Please generate a report using the template and data provided. Write your reponse tone and narrative like you are writting for an professional bitcion hedge fund portfolio manager / investment advisor. As you structure the narrative:

1. Integrate answers to the guiding questions seamlessly within the narrative without explicitly mentioning the questions. You must answer all questoins asked do not skip any guiding questions. They will be marked by "Guiding Questions:".
2. Strictly adhere to the provided template, ensuring each section is populated with the correct corresponding data from the table.
3. Refrain from adding any conclusions or deviating from the provided script in any way.
4. Your focus should be on presenting a clear, coherent narrative that aligns closely with the provided template and data.
5. For refrence in the template below the report date is [Todays Date] use this date for generating the heatmap to formulate the rest of the narrative template using [Todays Date] as the most recent date as the refrence point for heatmap.
6. Take into account [Todays Date] in your analysis so you understand where we are in the progression of time throughout the month and how close we are to the end of the month. Exmaple: If we are at the start of the month then we still have a lot of time to analyze the month ahead through progression of time but if its at the end then we can tell the month is about to end and we can focus on the month ahead / review on month etc.
Data:
{}

----- Template Start -----
Bitcoin Monthly Heatmap Overview and Analysis

Report Date: {}

Deciphering Bitcoin's Historical Heatmap

The Bitcoin performance heatmap is an invaluable tool for visualizing the currency's historical market fluctuations, offering a window into its potential future behavior. By overlaying historical performance data onto the current market landscape, the heatmap not only recounts Bitcoin's past but also serves as a navigational beacon for predicting its market trajectory.

Monthly Heatmap Insights
[Report Date]

Central to our analysis is the monthly heatmap, which analyzes the average return for [Current Month] throughout Bitcoin's history. The average return for this month, historically at [Current Month's Historical Average Return]%, establishes a benchmark for assessing the current month's performance against long-term patterns.

Current Data Interpretation

For the current month of [Current Month], the observed performance is [Current Month's Performance]%. When compared with the historical average of [Current Month's Historical Average Return]%, this performance offers a [Bullish/Bearish] outlook, indicating [Explanation of Current Market Behavior].

Market Outlook for the Month

Given the current performance and historical data analysis, the market outlook for [Current Month] is [Market Outlook Description].

----- Recap of Expectations -----
To ensure the effectiveness of the narrative:
- Strictly follow the provided template structure.
- Focus on clear, coherent reporting without deviations.
    """.format(table_string, report_date)
    return template


## Premium Report Section ---


# Create Fundamentals Report Content
def generate_fundamentals_prompt(data_path):
    # Read the data from the CSV file
    df = pd.read_csv(data_path)

    # Convert the dataframe to a formatted string
    table_string = df.to_string(index=False)

    # Construct the template with the table data appended
    template = """
Please generate a report using the template and data provided. Write your reponse tone and narrative like you are writting for an professional bitcion hedge fund portfolio manager / investment advisor. As you structure the narrative:

0. Put each sentence on a new line 
1. Integrate answers to the guiding questions seamlessly within the narrative without explicitly mentioning the questions. You must answer all questoins asked do not skip any guiding questions. They will be marked by "Guiding Questions:".
2. Strictly adhere to the provided template, ensuring each section is populated with the correct corresponding data from the table.
3. Refrain from adding any conclusions or deviating from the provided script in any way.
4. Your focus should be on presenting a clear, coherent narrative that aligns closely with the provided template and data.

Section Goal: a comprehensive view of the underlying fundamental metrics driving the Bitcoin network, capturing transactional activity, miner economics, and network usage. These metrics elucidate the health, growth, and engagement of the Bitcoin network, highlighting security, economic activity, and overall adoption. This provides investors a viewpoint into the fundamentals keeping them invested in the bitcoin market ensuring the first principles of the network are aligning with investment thesis about future usage and adoption of the bitcoin network.

Data:
{}

----- Template Start -----

On-Chain Transaction Activity
Over the past 7 days, the Bitcoin network has displayed a [describe the general trend: vibrant/steady/slow] activity pace. The transaction count currently stands at [Transaction Count], [interpretation based on change: indicating a surge/drop/stability] in network transactions. This is mirrored by a transaction volume of [Transaction Volume] USD, [interpretation based on change: showcasing a high/low/moderate] volume of capital engagement in the network. Diving deeper, the average transaction size for this period stands at [Avg Transaction Size] USD, [interpretation based on change: reflecting larger/smaller/stable] individual transactions on average. Additionally, the network boasts [Active Address Count] active addresses, [interpretation based on change: highlighting a growing/steady/decreasing] community of participants in the Bitcoin ecosystem.

Guiding Questions:

What does the 7 day performance of these transaction metrics say about the bitcoin network's economic activity?

Miner Economics
The [describe the general trend: vibrant/steady/slow] transaction activity in the Bitcoin network is fostering [describe the economic condition: substantial/moderate/low] revenues for miners. Currently, the miner revenue is at [Miner Revenue] USD, [interpretation based on change: indicating a healthy/challenging/stable] economic environment for mining activities within the network. This economic activity has also generated fees amounting to [Fees In USD] USD, which forms [calculate percentage of fees to miner revenue] percentage of the miner's revenue, showcasing a [interpretation based on percentage: healthy/challenged/stable] fee market.

Guiding Questions:

What does the fee in USD indicate about the network's fee market and its role in supporting network security?

Bitcoin Holder Behaviour
Analyzing the holder behavior within the Bitcoin network, we note that there are [+$10 USD Address] addresses holding balances greater than 10 USD, [interpretation based on change: indicating a substantial/moderate/low] number of users with investments in the network. Furthermore, [1+ Year Supply %] of the current supply has been stationary for over a year, [interpretation based on percentage: showcasing a strong/moderate/weak] holder base with a long-term investment outlook. This behavior is mirrored in the 1-year velocity of [1 Year Velocity], [interpretation based on velocity: indicating a trend of holding/trading/mixed behavior], underscoring [interpretation based on velocity: the growing/stable/decreasing] perception of Bitcoin as a reliable store of value.

Guiding Questions:

What does the number of +10 USD address balance performance across 7 day period and YTD indicate about the growth of investors holding bitcoin?
How does the 1+ year supply percentage reflect the long-term investment outlook of the holders?

----- Recap of Expectations -----
To ensure the effectiveness of the narrative:
- Seamlessly integrate all guiding questions.
- Strictly follow the provided template structure.
- Focus on clear, coherent reporting without deviations.
    """.format(table_string)
    return template


# Create Price Model Report Content
def generate_price_model_prompt(data_path):
    # Read the data from the CSV file
    df = pd.read_csv(data_path)

    # Convert the dataframe to a formatted string
    table_string = df.to_string(index=False)

    # Construct the template with the table data appended
    template = """
Please generate a report using the template and data provided. Write your reponse tone and narrative like you are writting for an professional bitcion hedge fund portfolio manager / investment advisor. As you structure the narrative:

1. Integrate answers to the guiding questions seamlessly within the narrative without explicitly mentioning the questions. You must answer all questoins asked do not skip any guiding questions. They will be marked by "Guiding Questions:".
2. Strictly adhere to the provided template, ensuring each section is populated with the correct corresponding data from the table.
3. Refrain from adding any conclusions or deviating from the provided script in any way.
4. Your focus should be on presenting a clear, coherent narrative that aligns closely with the provided template and data.

Data:
{}

----- Template Start ----- 
4 Year CAGR: Reflects a growth trajectory based on past performance, with current projections indicating a conservative estimate if the growth rate remains steady, and a bullish estimate for an accelerated growth rate.

Conservative Estimate: $52,385
Bullish Estimate: $65,761
Current 4 Year CAGR: [Current 4 Year CAGR Placeholder]

The current market price of Bitcoin is [Current Market Price Placeholder], which positions it [Above/Below] our conservative and [Above/Below] bullish CAGR estimates. The Current CAGR, at [Current 4 Year CAGR Placeholder], is [Above/Below] the Conservative 4 Year CAGR of 24% and [Above/Below] the Bullish 4 Year CAGR value of 55%, showcasing that the model currently views Bitcoin as [overvalued/ fairly/ undervalued] in historical context.

Stock To Flow: Associates Bitcoin's price with its diminishing rate of production, suggesting a higher value as scarcity increases, with conservative and bullish scenarios reflecting varying degrees of market response.

Conservative Estimate: $111,690
Bullish Estimate: $153,000
Current S2F Multiple: [Current S2F Multiple Placeholder]

With the current price of Bitcoin at [Current Market Price Placeholder], it's [Above/Below] the S2F model's conservative and [Above/Below] bullish estimates. . The current S2F multiple, at [Current S2F Multiple Placeholder], is [Above/Below] the average multiple of 1.14 and [Above/Below] the 90th percentile value of 1.72, showcasing that the model currently views Bitcoin as [overvalued/ fairly/ undervalued] in historical context.

200 Day MA Multiple: This indicator compares the current market price to a 200-day moving average, with conservative estimates based on historical movements and bullish projections forecasting a significant uptick.

Conservative Estimate: $48,104
Bullish Estimate: $72,845
Current 200 Day MA Multiple: [Current 200 Day MA Placeholder]

At the present Bitcoin price of [Current Market Price Placeholder], we are tracking [Above/Below] the conservative and [Above/Below] bullish 200 Day MA estimates. The Current 200 Day MA Multiple, at [Current 200 Day MA Placeholder], is [Above/Below] the average multiple of 1.14 and [Above/Below] the 90th percentile value of 1.72, showcasing that the model currently views Bitcoin as [overvalued/ fairly/ undervalued] in historical context.

Realized Price Multiple: Takes into account the average price at which all bitcoins were last moved, with a conservative estimate close to this realized price and a bullish estimate predicting a higher market valuation.

Conservative Estimate: $50,445
Bullish Estimate: $77,895
Current Realized Price Multiple: [Current Realized Price Placeholder]

Bitcoin's current market price of [Current Market Price Placeholder] is [Above/Below]  conservative and [Above/Below] bullish realized price predictions. The Realized Price Multiple, at [Current Realized Price Placeholder], is [Above/Below] the average multiple of 1.68 and [Above/Below] the 90th percentile value of 2.59, showcasing that the model currently views Bitcoin as [overvalued/ fairly/ undervalued] in historical context.

Thermocap Price Multiple: Evaluates the cumulative revenue of miners to gain insights into the Bitcoin's valuation, with conservative estimates assuming steady valuation and bullish estimates expecting increased miner revenue.

Conservative Estimate: $59,682
Bullish Estimate: $116,904
Current Thermocap Multiple: [Current Thermocap Multiple Placeholder]

The market price of Bitcoin at [Current Market Price Placeholder] is [Above/Below]  conservative and [Above/Below] bullish realized price predictions. The Thermocap Multiple, at [Current Thermocap Multiple Placeholder], is [Above/Below] the average multiple of 14.96 and [Above/Below] the 90th percentile value of 29.30, showcasing that the model currently views Bitcoin as [overvalued/ fairly/ undervalued] in historical context.

Production Cost Multiple: Reflects the balance of market price and production costs, where the conservative estimate maintains equilibrium and the bullish estimate forecasts rising production costs contributing to a higher market price.

Conservative Estimate: $69,226
Bullish Estimate: $142,903
Current Production Cost Multiple: [Current Production Cost Placeholder]

Currently, Bitcoin's price of [Current Market Price Placeholder] is [Above/Below] our conservative and [Above/Below] bullish production cost model estimates. The current Production Cost Multiple, at [Current Thermocap Multiple Placeholder], is [Above/Below] the average multiple of 1.03 and [Above/Below] the 90th percentile value of 2.13, showcasing that the model currently views Bitcoin as [overvalued/ fairly/ undervalued] in historical context.

Guiding Questions:

Write a short 1-3 sentence section summary of the findings of this section and the impact it has on bitcoins price outlook heading into end of year 2024.

----- Recap of Expectations -----
To ensure the effectiveness of the narrative:
- Strictly follow the provided template structure.
- Focus on clear, coherent reporting without deviations.
    """.format(table_string)

    return template


# Create Relative Valuation Report Content
def generate_relative_valuation_prompt(data_path):
    # Read the data from the CSV file
    df = pd.read_csv(data_path)

    # Convert the dataframe to a formatted string
    table_string = df.to_string(index=False)

    # Construct the template with the table data appended
    template = """
Please generate a report using the template and data provided. Write your reponse tone and narrative like you are writting for an professional bitcion hedge fund portfolio manager / investment advisor. As you structure the narrative:

1. Integrate answers to the guiding questions seamlessly within the narrative without explicitly mentioning the questions. You must answer all questoins asked do not skip any guiding questions. They will be marked by "Guiding Questions:".
2. Strictly adhere to the provided template, ensuring each section is populated with the correct corresponding data from the table.
3. Refrain from adding any conclusions or deviating from the provided script in any way.
4. Your focus should be on presenting a clear, coherent narrative that aligns closely with the provided template and data.
5. No speical fomratting just plain text no need to bold or highlgiht any sections.

Data:
{}

----- Template Start -----

Relative Valuation Models

In the vast landscape of investment assets, it's crucial to position Bitcoin within a comparative framework. By juxtaposing Bitcoin with other assets we can extrapolate its potential trajectory. Allow me to guide you through this comparative lens.

Tech Companies' Market Cap Comparison:
In the realm of digital innovation, comparing Bitcoin with the market capitalizations of leading technology companies like Apple, Microsoft, Alphabet, Amazon, and Meta offers insights into its potential as a disruptive force. This comparison underscores Bitcoin's growing influence and potential market value in the context of the global technology sector, highlighting its standing relative to established tech giants.

Apple: If Bitcoin were to match Apple's market cap, it would reach a price level of [Input Apple Price Level Here].
Microsoft: Equating Bitcoin to Microsoft's market cap would see it at a price level of [Input Microsfot Price Level Here].
Alphabet (Google): Matching Alphabet's valuation would set Bitcoin's price level at [Input Alphabet Price Level Here].
Amazon: For Bitcoin to equal Amazon's market cap, its price level would be [Input Amazon Price Level Here].
Meta (Facebook): If Bitcoin's market cap were equivalent to Meta's, the price level would be [Input Meta Price Level Here].

Monetary Base (M0) Comparison:
Analyzing Bitcoin in relation to the monetary bases (M0) of significant economies such as the Eurozone, United States, China, Japan, and the United Kingdom illuminates its emerging role as a digital monetary asset. This perspective allows us to assess Bitcoin's capacity to act as a global reserve currency, positioning it within the broader landscape of traditional fiat currencies.

Eurozone: Matching the Eurozone's M0 would put Bitcoin's price level at [Input EurozonePrice Level Here].
United States: To reach the US M0, Bitcoin's price level would be [Input United States Price Level Here].
China: Equating Bitcoin to China's M0 would result in a price level of [Input China Price Level Here].
Japan: If Bitcoin matched Japan's M0, its price level would be [Input Japan Price Level Here].
United Kingdom: To equal the UK's M0, Bitcoin's price level would be [Input United Kingdom Price Level Here].

Gold Market Comparison:
Comparing Bitcoin with the gold market offers a perspective on its potential as a digital store of value. This comparison draws parallels between Bitcoin's scarcity and decentralized nature with gold's historical role as a hedge against inflation and economic uncertainty, emphasizing Bitcoin's place as "digital gold" in the modern financial ecosystem.
Country Holdings in Gold: If Bitcoin's market cap were equivalent to nation state holdings of gold, the price level would be [Input Country Holding Price Level Here].
Private Investment in Gold: If Bitcoin's market cap were equivalent to private investments in gold, the price level would be [Input Private Investment in Gold Price Level Here].
Total Gold Market: For Bitcoin to match the total gold market valuation, its price level would be [Input Total Gold Market Price Level Here].

Guiding Questions:

Write a short 1-3 sentence section summary of the findings of this section and the impact it has on bitcoins price outlook heading into end of year 2024.    

----- Recap of Expectations -----
To ensure the effectiveness of the narrative:
- Strictly follow the provided template structure.
- Focus on clear, coherent reporting without deviations.
""".format(table_string)
    return template


# Create Edited Report Sections
def analyze_output(original_data, ai_output):
    analysis_prompt = f"""
Given the original data and generated content, your task is to ensure this content adheres to the highest standards of accuracy and presentation. Analyze the content based on the following criteria and rewrite the content as the final draft:

Logic Review:
1. Verify the correctness of the data points mentioned in the generated content against the original data and prompt. 
2. Evaluate the insights provided in the generated content. Ensure that they are logical, relevant, and accurately derived from the original data and prompt.
3. Identify any discrepancies, inaccuracies, or areas of improvement in the generated content.
4. Rewrite the section content to ensure its accuracy, coherence, and alignment with the original data and prompt.

Content Style / Tone Review:
1. Is the content clear, concise, and free from jargon or overly complex sentences, reflecting Agent 21's expertise?
2. Does it strictly adhere to the provided template, ensuring each section is populated with the corresponding data from the table?
3. Is the tone professional and neutral, avoiding any biased or overly casual language, while maintaining the character of Agent 21?
4. Is the content structured logically, with a smooth flow of ideas from one section to the next, and does it answer all the guiding questions provided?
5. Does it refrain from adding any conclusions or deviating from the provided script in any way?

Content Style Review:
No Use Of Characters:
1. No use of characters like "-" or "*" 
2. No need to start of lists with - or bold txt with * plain txt is fine.

Grammar & Syntax Review:
1. Identify any grammatical or syntactic errors present in the content.
2. Check for consistent tense, voice, and subject-verb agreement throughout the content.
3. Ensure sentences are structured logically, without any awkward phrasings or redundancies.

Punctuation & Formatting Review:
1. Examine the content for correct punctuation usage, including commas, periods, semicolons, and quotation marks.
2. Ensure paragraphs and sentences are of appropriate length, facilitating easy readability.
3. Confirm that any lists, bullet points, or numbered items are formatted consistently.
4. Ensure data is formatted consistently for the relevant data type percentages, currency, decimals, including capitalization, formating, and punctuation.

Data Formatting:
1. Refrences to Bitcoin price should be rounded to have no decmials.
2. Percentages should be rounded to two decimal places and alwasy have a % sign at the end.
3. All financial data metrics should be rounded to two decimal places.

Original Data:
{original_data}

Generated Content:
{ai_output}

Rewriten Content:
"""
    return analysis_prompt


# Mapping URLs to their respective prompt functions
prompt_functions = {
    "weekly_market_summary": generate_weekly_bitcoin_recap_prompt,
    "historical_performance": generate_historical_performance_prompt,
    "heat_map": generate_heatmap_prompt,
    # "on_chain_fundamentals": generate_fundamentals_prompt,
    # "price_model": generate_price_model_prompt,
    # "relative_valuation": generate_relative_valuation_prompt,
}


# Function to Generate and Edit Content
def generate_and_edit_content(
    prompt_url, template_function, chat_llm_chain, review_llm_chain, report_date=None
):
    if report_date:
        initial_prompt = template_function(prompt_url, report_date)
    else:
        initial_prompt = template_function(prompt_url)

    initial_output = chat_llm_chain.predict(human_input=initial_prompt)
    edit_prompt = analyze_output(initial_prompt, initial_output)
    edited_output = review_llm_chain.predict(human_input=edit_prompt)
    return edited_output


# Closing Signature Section
signature_template = f""""
Final Thoughts

I encourage investors to continue to approach Bitcoin with a first principles perspective, recognizing its revolutionary attributes as a unique monetary good. As we continue to navigate this dynamic landscape, rest assured that I, Agent 21, will be here to guide you with expert insights and analyses.
Until the next Monday,

Agent 21
"""

# Intro Discalimer Template Section
disclaimer_template = f"""
*Disclaimer*: Agent 21 is an AI persona created by Secret Satoshis. The insights and opinions expressed by Agent 21 are generated by a Large Language Model (Chat-GPT 4). Always conduct your own research and consult with financial professionals before making any investment decisions.

Agent 21 GitHub | Report Data

Start your week with the Weekly Bitcoin Recap, exclusively from SecretSatoshis.com. Delivered every Monday morning, our newsletter distills the pivotal developments, market shifts, and essential on-chain metrics from the Bitcoin industry into digestible insights. Tailored for those eager to lead the conversation, it offers a strategic lens on the week's events, ensuring you're not just up-to-date but truly ahead of the curve. 

Whether you're deep in the Bitcoin world or just starting to explore, the Weekly Bitcoin Recap is your go-to source for navigating the complexities of the cryptocurrency world with confidence.
"""

# Conclusion Template Section
copy_template = """
Given the full Weekly Bitcoin Recap, I'd like to generate concise, engaging marketing copy for my post.

Your task is to extract key insights from the report and present them in a format similar to the example provided. Each point should follow the template, the same section title, and then a have new short compelling statement that reflects the latest Weekly Bitcoin Recap. The copy should be structured as follows:

Example Format: 
Stay Ahead with the Latest Bitcoin Insights!

Week X - Weekly Bitcoin Recap: 

Why Subscribe?

In This Weekly Bitcoin Recap
[Insert a two sentence summary of the findings of this weeks Weekly Bitcoin Recap and the impact it has on bitcoins price]

👉 Subscribe Now: Join the Secret Satoshis Newsletter: https://lnkd.in/eNiybtuk

Stay informed, stay ahead. Join the Secret Satoshis community for critical weekly insights.

Please ensure that:
1. The insights are accurate and reflect the latest data in the report.
2. The format is consistent with the provided example.
3. The language is clear, engaging, and suitable for marketing purposes.

Data:
{}
"""


def generate_full_report(
    chat_llm_chain, review_llm_chain, news_stories, report_date, image
):
    sections = {}

    news_impact_content = generate_and_edit_news_content(
        chat_llm_chain, review_llm_chain, news_stories
    )
    sections["news_impact"] = news_impact_content

    for section, url in urls.items():
        if section == "heat_map":
            sections[section] = generate_and_edit_content(
                url,
                prompt_functions[section],
                chat_llm_chain,
                review_llm_chain,
                report_date,
            )
        else:
            sections[section] = generate_and_edit_content(
                url, prompt_functions[section], chat_llm_chain, review_llm_chain
            )

    vision_analysis_results = weekly_bitcoin_outlook(image)
    for prompt, summary in vision_analysis_results.items():
        sections["weekly_btc_usd"] = summary

    # Conclusion Template Section
    conclusion_input_template = f"""
Agent 21, as we complete this Weekly Bitcoin Recap, I'd like you to summarize the main points of each section into a coherent conclusion summary. 
  
The objective is to capture the key insights, findings, and recommendations from each section to provide our readers with a concise and actionable summary of the entire Weekly Bitcoin Recap and provide forward looking outlook to help guide them in the weeks ahead in the bitcoin market. 

Use your expertise to bring together the various sections, highlighting the overarching narrative and the essential insights.

  Here are the summaries of each section:
  - Weekly Market Summary: {sections['weekly_market_summary']}
  - News Summary: {sections['news_impact']}
  - Weekly BTC/USD Chart Summary: {sections['weekly_btc_usd']}
  - Historical Performance: {sections['historical_performance']}
  - Heat Map: {sections['heat_map']}

Write a one-paragraph conclusion summarizing the above, providing a forward-looking outlook for our subscribers. Help guide them in the weeks ahead in the Bitcoin market by highlighting key news stories from the prior week and what to watch for moving forward for bitcoins price based on latest market devlopments and performance metrics.
  """

    # Generate the conclusion and executive summary
    conclusion = chat_llm_chain.predict(
        human_input=conclusion_input_template.format(sections=sections)
    )

    full_report = (
        disclaimer_template
        + "\n".join(sections.values())
        + "\n"
        + conclusion
        + signature_template
    )

    # Generate the conclusion and executive summary
    copy_output = chat_llm_chain.predict(human_input=copy_template.format(full_report))
    full_report = full_report + "\n\n" + copy_output

    with open("Weekly Bitcoin Recap.txt", "w") as f:
        f.write(full_report)
        print("Report generated successfully!")
    return full_report
