import pandas as pd
import ai_agent

# URLs for Data Gathering
urls = {
    "weekly_market_summary": 'https://secretsatoshis.github.io/Bitcoin-Weekly-Market-Update/weekly_summary.csv',
    "trading_week_performance": [
      'https://secretsatoshis.github.io/Bitcoin-Weekly-Market-Update/crypto_performance_table.csv',
      'https://secretsatoshis.github.io/Bitcoin-Weekly-Market-Update/equities_performance_table.csv',
      'https://secretsatoshis.github.io/Bitcoin-Weekly-Market-Update/index_performance_table.csv',
      'https://secretsatoshis.github.io/Bitcoin-Weekly-Market-Update/macro_performance_table.csv',
    ],
    "historical_performance": [
      'https://secretsatoshis.github.io/Bitcoin-Weekly-Market-Update/crypto_performance_table.csv',
      'https://secretsatoshis.github.io/Bitcoin-Weekly-Market-Update/equities_performance_table.csv',
      'https://secretsatoshis.github.io/Bitcoin-Weekly-Market-Update/index_performance_table.csv',
      'https://secretsatoshis.github.io/Bitcoin-Weekly-Market-Update/macro_performance_table.csv',
    ],
    "trading_range_analysis":  [
      'https://secretsatoshis.github.io/Bitcoin-Weekly-Market-Update/supplemental_trading_range_data_5000.csv',
      'https://secretsatoshis.github.io/Bitcoin-Weekly-Market-Update/supplemental_trading_range_data_1000.csv',
    ],
    "roi_analysis":  [
      'https://secretsatoshis.github.io/Bitcoin-Weekly-Market-Update/roi_table.csv',
    ],
    "heat_map": [
      'https://secretsatoshis.github.io/Bitcoin-Weekly-Market-Update/supplemental_data_weekly_heatmap.csv',
      'https://secretsatoshis.github.io/Bitcoin-Weekly-Market-Update/monthly_heatmap_data.csv',
      
    ],
    "fundamentals": 'https://secretsatoshis.github.io/Bitcoin-Weekly-Market-Update/fundamentals_valuation_table.csv',
}

# Create Weekly Market Update Summary
def generate_weekly_market_summary_prompt(data_path):
  # Read the data from the CSV file
  df = pd.read_csv(data_path)

  # Convert the dataframe to a formatted string
  table_string = df.to_string(index=False)

  # Construct the template with the table data appended
  template = """
Please generate a report section using the template and data provided. As you structure the narrative:

1. Integrate answers to the guiding questions seamlessly within the narrative without explicitly mentioning the questions. You must answer all questoins asked do not skip any guiding questions. They will be marked by "Guiding Questions:".
2. Strictly adhere to the provided template, ensuring each section is populated with the correct corresponding data from the table.
3. Refrain from adding any conclusions or deviating from the provided script in any way.
4. Your focus should be on presenting a clear, coherent narrative that aligns closely with the provided template and data.

Section Goal: Provide an introduction to the weekly market update highlighting the ethos behind the report to provide a first principles perspective on where investors are in the bitcoin market cycle. Delivered every Sunday morning the weekly market update provides a timely update on bitcoin market metrics providing a short term perspective on the bitcoin market and its current market scenario and its weekly outlook.

Data:
{}

----- Template Start -----

Introduction
Hello Bitcoin Investor,

Welcome to another edition of the "Weekly Market Summary". As your trusted Bitcoin Investment Analyst, I am here to guide you through the Bitcoin's market cycle, backed by the latest bitcoin blockchain and market data. Let's delve into the intricacies of the market as of [Report Date]. 

Weekly Market Summary
Current State of Bitcoin
On [Report Date], the market capitalization of Bitcoin is currently valued at [Market Cap], with the price per Bitcoin at [Bitcoin Price USD]. This price translates to a value of [Sats per Dollar] satoshis per US dollar. Bitcoin's marketcap dominance of the total cryptocurrency market is [Bitcoin Dominance Percentage]%, underscoring its influential position. Over the last 24 hours, the trading volume has reached [Bitcoin Trading Volume] billion, reflecting its global market trading activity. The prevailing sentiment in the Bitcoin market is [Bitcoin Market Sentiment], with a market trend that is notably [Bitcoin Market Trend]. Currently, Bitcoin's trading status is one that I classify as [Bitcoin Valuation].

    """.format(table_string)

  return template


# Create Performance Report Pt1
def generate_price_trading_week_performance_prompt(data_path):
  # Initialize an empty string to hold all table data
  combined_table_string = ""

  # Iterate through each data path, read the data, and append it to the combined string
  for path in data_path:
      df = pd.read_csv(path)
      table_string = df.to_string(index=False)
      combined_table_string += "\nData from {}:\n{}\n".format(path, table_string)

  # Convert the dataframe to a formatted string
  table_string = df.to_string(index=False)

  # Construct the template with the table data appended
  template = """
Please generate a report section using the template and data provided. As you structure the narrative:

1. Integrate answers to the guiding questions seamlessly within the narrative without explicitly mentioning the questions. You must answer all questoins asked do not skip any guiding questions. They will be marked by "Guiding Questions:".
2. Strictly adhere to the provided template, ensuring each section is populated with the correct corresponding data from the table.
3. Refrain from adding any conclusions or deviating from the provided script in any way.
4. Your focus should be on presenting a clear, coherent narrative that aligns closely with the provided template and data.

Section Goal: Provide a comparative analysis of Bitcoin's weekly performance against other crypto currencies, equities, macro asset classes and indexes.This comparison offers a context for Bitcoin's standing and trajectory relative to traditional markets. Helping aid investors confidence in holding bitcoin vs other asset classes and puts bitcoins performance in context of macro markets.

Data:
{}

----- Template Start ----- 

Comparative Analysis
Let's see how Bitcoin's performance measured against the broader financial markets. As of [Report Date ] Bitcoin has experienced a trading week return of [Trading Week Return]. In a dynamic investment landscape, assessing Bitcoin's performance against a diverse array of assets and asset classes is essential to understand its role and relative strength as a potential investment vehicle. This comparison will illuminate Bitcoin's behavior in the context of broader market movements, providing investors with a clearer picture of its position during the trading week.

Guiding Questions:

How does Bitcoin's trading week return performance compare VS Nasdaq, US Dollar Index, Gold, Treasury Index, Commodity Index?
What insights can we learn from the Bitcoin trading week return vs these other traditional markets, crypto markets and bitcoin related equities during this trading week?

Example of Expected Output, respond with your updated analysis of current data:

In the realm of cryptocurrencies and stocks, Bitcoin has outshined its counterparts with its week-to-date return standing at 6.44%. Ethereum (ETH) and Ripple (XRP) trailed behind with returns of -7.58% and -2.69%, respectively. Bitcoin-related equities also showed mixed performances, with MicroStrategy (MSTR) posting a positive return of 5.17%, while Square (SQ) and Coinbase (COIN) experienced declines of -2.58% and -2.35% respectively.

Turning to the broader indexes and macroeconomic indicators, Bitcoin's performance was robust when compared to traditional financial markets. The Nasdaq Composite saw a modest increase of 0.62%, and the S&P 500 index climbed by 0.84%, both falling short of Bitcoin's impressive gains. Financials, represented by the XLF Financials ETF, were up by 1.42%, and the energy sector, indicated by the XLE Energy ETF, showed a notable increase of 4.70% but still did not surpass Bitcoin's return. The FANG+ ETF, which includes some of the biggest tech giants, had a week-to-date return of 2.46%, indicating a positive week for technology stocks but again not reaching the heights of Bitcoin's performance.

The US Dollar Index, a key benchmark for the international value of the US dollar, had an increment of 0.17%, indicating relative stability in the forex markets. Gold Futures, usually a haven during market uncertainty, experienced a slight dip of 0.08%. The 20+ Year Treasury Bond ETF, a reflection of long-term government debt instruments, decreased by 0.92%, while the Bloomberg Commodity Index, a diversified basket of commodities, grew by 1.94%.

In conclusion, Bitcoin's significant week-to-date return of 6.44% positions it as a standout performer not only within the cryptocurrency space but also across a wide range of traditional asset classes. This week's data suggests that Bitcoin is maintaining its appeal as an investment, potentially offering a higher yield in a week that saw varied performances from other assets and asset classes. Such comparative analysis can reinforce investor confidence in Bitcoin's ability to act as a dynamic component of a diversified investment portfolio.
    """.format(table_string)
  return template


# Create Performance Report Pt2
def generate_price_historical_performance_prompt(data_path):
  # Initialize an empty string to hold all table data
  combined_table_string = ""

  # Iterate through each data path, read the data, and append it to the combined string
  for path in data_path:
      df = pd.read_csv(path)
      table_string = df.to_string(index=False)
      combined_table_string += "\nData from {}:\n{}\n".format(path, table_string)

  # Convert the dataframe to a formatted string
  table_string = df.to_string(index=False)

  # Construct the template with the table data appended
  template = """
Please generate a report section using the template and data provided. As you structure the narrative:

1. Integrate answers to the guiding questions seamlessly within the narrative without explicitly mentioning the questions. You must answer all questoins asked do not skip any guiding questions. They will be marked by "Guiding Questions:".
2. Strictly adhere to the provided template, ensuring each section is populated with the correct corresponding data from the table.
3. Refrain from adding any conclusions or deviating from the provided script in any way.
4. Your focus should be on presenting a clear, coherent narrative that aligns closely with the provided template and data.

Section Goal: Provide a comparative analysis of Bitcoin's weekly performance against other crypto currencies, equities, macro asset classes and indexes.This comparison offers a context for Bitcoin's standing and trajectory relative to traditional markets. Helping aid investors confidence in holding bitcoin vs other asset classes and puts bitcoins performance in context of macro markets.

Data:
{}

----- Template Start ----- 
Historical Performance

Taking a glance at the historical data, Bitcoin has a month-to date return of [MTD- Return] and a year-to-date return of [YTD Return]. 

Guiding Questions:

How does Bitcoins trading week return compare to the month-to-date (MTD) and year-to-date (YTD) return? What does this tell us about bitcoins short term medium term and long term returns?
    """.format(table_string)
  return template

# Create Market Analysis Report
def generate_trading_range_analysis_prompt(data_path):
  # Initialize an empty string to hold all table data
  combined_table_string = ""

  # Iterate through each data path, read the data, and append it to the combined string
  for path in data_path:
      df = pd.read_csv(path)
      table_string = df.to_string(index=False)
      combined_table_string += "\nData from {}:\n{}".format(path, table_string)

  # Convert the dataframe to a formatted string
  table_string = df.to_string(index=False)

  # Construct the template with the table data appended
  template = """
Please generate a report section using the template and data provided. As you structure the narrative:

1. Integrate answers to the guiding questions seamlessly within the narrative without explicitly mentioning the questions. You must answer all questoins asked do not skip any guiding questions. They will be marked by "Guiding Questions:".
2. Strictly adhere to the provided template, ensuring each section is populated with the correct corresponding data from the table.
3. Refrain from adding any conclusions or deviating from the provided script in any way.
4. Your focus should be on presenting a clear, coherent narrative that aligns closely with the provided template and data.

Data:
{}

----- Template Start -----
As we dissect Bitcoin's market activity, the trading ranges reveal a historical perspective of market behavior. Bitcoin is currently navigating the [Current Price Bucket 1k], a range that holds importance both in the narrower 1K range and the broader [Current Price Bucket 5k] range. Over its lifespan, this specific interval has recorded a [interpret based on data: small, moderate, significant] number of trading days, amounting to  [Current Price Bucket 1k] in the 1K range. This activity level is [interpret based on data: an anomaly, typical, indicative] of a [interpret based on data: marginal, noteworthy, pivotal] trend in Bitcoin's trading history.

Guiding Questions:
Based on the historical trading days, what does the data suggest about market liquidity and investor sentiment within these ranges?

Understanding these historical patterns is vital. It informs investors about the regions where Bitcoin might experience greater levels of market scrutiny. Such insights are essential for strategic positioning, as these ranges could dictate the strength of the market's response to Bitcoin's approach, potentially leading to inflection points in price movement.
""".format(table_string)

  return template


# Create Market Analysis Report
def generate_roi_analysis_prompt(data_path):
  # Initialize an empty string to hold all table data
  combined_table_string = ""

  # Iterate through each data path, read the data, and append it to the combined string
  for path in data_path:
      df = pd.read_csv(path)
      table_string = df.to_string(index=False)
      combined_table_string += "\nData from {}:\n{}\n".format(path, table_string)

  # Convert the dataframe to a formatted string
  table_string = df.to_string(index=False)

  # Construct the template with the table data appended
  template = """
Please generate a report section using the template and data provided. As you structure the narrative:

1. Integrate answers to the guiding questions seamlessly within the narrative without explicitly mentioning the questions. You must answer all questoins asked do not skip any guiding questions. They will be marked by "Guiding Questions:".
2. Strictly adhere to the provided template, ensuring each section is populated with the correct corresponding data from the table.
3. Refrain from adding any conclusions or deviating from the provided script in any way.
4. Your focus should be on presenting a clear, coherent narrative that aligns closely with the provided template and data.

Data:
{}

----- Template Start -----
Turning our attention to Bitcoin's Return on Investment (ROI), the data narrates a story of market performance across various time frames. An immediate market reaction is captured by a 3-day ROI of [3 Day ROI], serving as a pulse check for Bitcoin's volatility. Over a broader timeframe, the 30-day ROI of [30 Day ROI] provides insight into the short-term investment performance.

The medium-term sentiment, often swayed by broader economic indicators and sentiment, is encapsulated by a 1-year ROI of [1 Year ROI]. Meanwhile, a 5-year ROI of [5 Year ROI] reflects upon a journey through bull and bear markets, booms and busts, echoing a long-term conviction in Bitcoin's overarching value proposition.

Guiding Question
Is there a timeframe that bitcoin does not have a positive ROI? If so what does that tell us about its historical performance in the context of all its ROI timeframes? 
What does the ROI Table tell us about bitcoins short term and long term return profile and investment characteristics?
    """.format(table_string)

  return template

# Create Heatmap Report
def generate_heatmap_prompt(data_path):
  # Initialize an empty string to hold all table data
  combined_table_string = ""

  # Iterate through each data path, read the data, and append it to the combined string
  for path in data_path:
      df = pd.read_csv(path)
      table_string = df.to_string(index=False)
      combined_table_string += "\nData from {}:\n{}\n".format(path, table_string)
    
  # Convert the dataframe to a formatted string
  table_string = df.to_string(index=False)

  # Construct the template with the table data appended
  template = """
Please generate a report section using the template and data provided. As you structure the narrative:

1. Integrate answers to the guiding questions seamlessly within the narrative without explicitly mentioning the questions. You must answer all questoins asked do not skip any guiding questions. They will be marked by "Guiding Questions:".
2. Strictly adhere to the provided template, ensuring each section is populated with the correct corresponding data from the table.
3. Refrain from adding any conclusions or deviating from the provided script in any way.
4. Your focus should be on presenting a clear, coherent narrative that aligns closely with the provided template and data.
5. For refrence in the template below the report date is [Todays Date] use this date for generating the heatmap to formulate the rest of the narrative template using [Todays Date] as the most recent date as the refrence point for heatmap.
Data:
{}


----- Template Start -----
For refrence in the template below the report date is [Todays Date] use this date for the data to formulate the rest of the narrative template using the most recent date as the refrence point.


In this section of our Weekly Market Update, we turn to the historical heatmaps, which layer past performance over the present, offering us a spectrum of Bitcoin's historical performance. These maps are not just a record of what has been but a potential guide to what might be, especially when viewed through the lens of average returns for the current month and last week's performance.

Weekly Heatmap Reflection:
The weekly heatmap for [Todays Date] which is the [Current Week Number] week of the year showcases [Insert Interpretation of This Week's Performance]. Comparing this to the historical average, we see that Bitcoin has [Outperformed/Underperformed] this week's average return. As we approach next week, historically, the average return for week [Next Week Number] has been [Next Week Avg Return], setting a [Positive/Negative] expectation for the upcoming week.

Monthly Heatmap Perspective:
Delving deeper, the monthly heatmap highlights the average return for the current month over previous years. For the month of [Current Month], the average return has been [Current Month's Historical Average Return]. This figure gives us a historical benchmark against which to measure this month's performance. Should the current trend align with or diverge from this average, it provides a [Bullish/Bearish] signal for Bitcoin's short-term trajectory.
    """.format(table_string)

  return template

# Create Fundamentals Report
def generate_fundamentals_prompt(data_path):
  # Read the data from the CSV file
  df = pd.read_csv(data_path)

  # Convert the dataframe to a formatted string
  table_string = df.to_string(index=False)

  # Construct the template with the table data appended
  template = """
Please generate a report section using the template and data provided. As you structure the narrative:

1. Integrate answers to the guiding questions seamlessly within the narrative without explicitly mentioning the questions. You must answer all questoins asked do not skip any guiding questions. They will be marked by "Guiding Questions:".
2. Strictly adhere to the provided template, ensuring each section is populated with the correct corresponding data from the table.
3. Refrain from adding any conclusions or deviating from the provided script in any way.
4. Your focus should be on presenting a clear, coherent narrative that aligns closely with the provided template and data.

Section Goal: A comprehensive view of the underlying fundamental metrics driving the Bitcoin network, capturing transactional activity, miner economics, and network usage. These metrics elucidate the health, growth, and engagement of the Bitcoin network, highlighting security, economic activity, and overall adoption. This provides investors a viewpoint into the fundamentals keeping them invested in the bitcoin market ensuring the first principles of the network are aligning with investment thesis about future usage and adoption of the bitcoin network.

Data:
{}

----- Template Start -----

Our Weekly Market Update is committed to providing a thorough analysis of Bitcoin's on-chain metrics, key to understanding the network's resilience, economic pulse, and user engagement. The forthcoming data serves as a vital sign of the cryptocurrency's foundational health.

Network Performance Analysis:
The network's user growth is quantified by the Total Address Count, which now stands at [Total Address Count Placeholder], having shifted by [Total Address Count 7 Day Avg % Change Placeholder] over the last week. This change, alongside the [Address Count > $10 7 Day Avg % Change Placeholder] increase in addresses holding over $10, currently at [Address Count > $10 Placeholder], offers insights into the evolving landscape of Bitcoin ownership. The activity within the network is further detailed by the Active Addresses, which number [Active Addresses Placeholder], shifting by [Active Addresses 7 Day Avg % Change Placeholder], and may imply a [Analysis Placeholder] in on-chain transactions or wallet activities.

The enduring confidence in Bitcoin is reflected in the percentage of Supply Held for 1+ Year, now at [Supply Held 1+ Year % Placeholder], which has experienced a change of [Supply Held 1+ Year % 7 Day Avg % Change Placeholder], indicative of a strong holder sentiment. Transaction activity, as seen through the count of [Transaction Count Placeholder] and the volume at [Transaction Volume Placeholder], both experiencing changes of [Transaction Count 7 Day Avg % Change Placeholder] and [Transaction Volume 7 Day Avg % Change Placeholder] respectively, speaks volumes about the network's utilization and economic throughput.

Security Metrics & Miner Economics:
In terms of network security, the Hash Rate stands at [Hash Rate Placeholder] despite a [Hash Rate 7 Day Avg % Change Placeholder] change, while the Network Difficulty currently stands at  [Network Difficulty Placeholder], changing by [Network Difficulty 7 Day Avg % Change Placeholder]. These figures collectively represent the competitive and secure environment in which miners operate. Miner Revenue, now at [Miner Revenue Placeholder], has seen an [change placeholder] of [Miner Revenue 7 Day Avg % Change Placeholder], with the Fee Percentage of Reward at [Fee % Of Reward Placeholder], suggesting a [Analysis Placeholder] in network transaction demand.

Supply Dynamics and Valuation Indicators:
The Bitcoin Supply, marginally expanding by [Bitcoin Supply 7 Day Avg % Change Placeholder] to [Bitcoin Supply Placeholder], along with the percentage of total supply issued creeping up to [Bitcoin Supply 7 Day Avg % Change Placeholder], ensures the scarcity narrative of Bitcoin remains robust. The Annual Inflation Rate at [Annual Inflation Rate Placeholder], alongside the Velocity at [Velocity Placeholder], provides a deeper understanding of Bitcoin's economic throughput and velocity of money within its ecosystem.

Market Valuation Perspective:
A close look at valuation metrics reveals a market cap appreciation to [Market Cap Placeholder], a change of [Market Cap 7 Day Avg % Change Placeholder], aligning with the Bitcoin Price, which has appreciated by [Bitcoin Price 7 Day Avg % Change Placeholder] to [Bitcoin Price Placeholder]. The slight increments in the Realised Price at [Realised Price Placeholder] and Thermocap Price at [Thermocap Price Placeholder] add nuance to our understanding of Bitcoin's market valuation beyond the immediate price movements.

Guiding Questions:
Given the shifts in Bitcoin price, how might investors interpret Bitcoin's market performance in light of the economic signals from the network?
    """.format(table_string)

  return template

# Function to Analyze Visual Data and Create Report Sections
def generate_and_edit_vision_content(vision_prompt, image_url, chat_llm_chain):
    # Invoke the Vision API with the provided prompt and image URL
    vision_output = ai_agent.invoke_vision_api(vision_prompt, image_url)
    vision_analysis = vision_output.choices[0].message.content

    # Run Second Round Edits using the analyze_output function
    edit_prompt = analyze_output(vision_prompt, vision_analysis)
    edited_vision_output = chat_llm_chain.predict(human_input=edit_prompt)
    return edited_vision_output

def generate_news_impact_prompt(news_stories):
  # Construct the template with the news stories appended
  template = f"""
Please generate a report section using the template and data provided. As you structure the narrative:

1. Integrate answers to the guiding questions seamlessly within the narrative without explicitly mentioning the questions. You must answer all questoins asked do not skip any guiding questions. They will be marked by "Guiding Questions:".
2. Strictly adhere to the provided template, ensuring each section is populated with the correct corresponding data from the table.
3. Refrain from adding any conclusions or deviating from the provided script in any way.
4. Your focus should be on presenting a clear, coherent narrative that aligns closely with the provided template and data.
5. Format the provided news stories into bullet points with the news source name provided in () at the end.
6. Provide a summary at the end of the news stories, discussing their potential impact on Bitcoin's price and overall adoption in both the short and long term.

News Stories:
{news_stories}

----- Template Start -----

News Stories:
- [Bullet point format of first news story]
- [Bullet point format of second news story]
- [More bullet points as per the provided news stories]

News Impact:
Given the above news stories, the potential impact on Bitcoin's price and overall adoption can be summarized as follows:
[Provide a brief summary of the expected impact]

Guiding Questions:
- What cumulative effect could these stories have on investor sentiment and market trends?
- Are there any particular areas of Bitcoin's ecosystem that these news stories specifically influence (e.g., regulatory, technological, societal)?
"""
  return template

def generate_and_edit_news_content(chat_llm_chain,news_stories):
  # Generate initial prompt with news stories
  initial_prompt = generate_news_impact_prompt(news_stories)

  # Get initial output from the AI model
  initial_output = chat_llm_chain.predict(human_input=initial_prompt)

  # Run Second Round Edits using the analyze_output function
  edit_prompt = analyze_output(initial_prompt, initial_output)
  edited_output = chat_llm_chain.predict(human_input=edit_prompt)

  return edited_output

# Create Edited Report Sections
def analyze_output(original_data, ai_output):
    analysis_prompt = f"""
Given the original data and generated content, your task is to ensure this content adheres to the highest standards of accuracy and presentation. Analyze the content based on the following criteria and rewrite the content as the final draft:

Logic Review:
1. Verify the correctness of the data points mentioned in the generated content against the original data and prompt. 
2. Evaluate the insights provided in the generated content. Ensure that they are logical, relevant, and accurately derived from the original data and prompt.
3. Highlight any discrepancies, inaccuracies, or areas of improvement in the generated content.
4. Rewrite the section content to ensure its accuracy, coherence, and alignment with the original data and prompt.

Content Style Review:
1. Is the content clear, concise, and free from jargon or overly complex sentences, reflecting Agent 21's expertise?
2. Does it strictly adhere to the provided template, ensuring each section is populated with the corresponding data from the table?
3. Is the tone professional and neutral, avoiding any biased or overly casual language, while maintaining the character of Agent 21?
4. Is the content structured logically, with a smooth flow of ideas from one section to the next, and does it answer all the guiding questions provided?
5. Does it refrain from adding any conclusions or deviating from the provided script in any way?

Grammar & Syntax Review:
1. Identify any grammatical or syntactic errors present in the content.
2. Check for consistent tense, voice, and subject-verb agreement throughout the content.
3. Ensure sentences are structured logically, without any awkward phrasings or redundancies.

Punctuation & Formatting Review:
1. Examine the content for correct punctuation usage, including commas, periods, semicolons, and quotation marks.
2. Ensure paragraphs and sentences are of appropriate length, facilitating easy readability.
3. Confirm that any lists, bullet points, or numbered items are formatted consistently.
4. Ensure data is formatted consistently for the relevant data type percentages, currency no decimal value, decimals just to two places, including capitalization, formating, and punctuation.

Original Data:
{original_data}

Generated Content:
{ai_output}

Rewriten Content:
"""
    return analysis_prompt

def perform_vision_analysis(chat_llm_chain):
  vision_tasks = [
    {
      "prompt": """
      Please generate a report section using the template and data provided. As you structure the narrative:

      1. Integrate answers to the guiding questions seamlessly within the narrative without explicitly mentioning the questions. You must answer all questoins asked do not skip any guiding questions. They will be marked by "Guiding Questions:".
      2. Strictly adhere to the provided template, ensuring each section is populated with the correct corresponding data from the image.
      3. Refrain from adding any conclusions or deviating from the provided script in any way.
      4. Your focus should be on presenting a clear, coherent narrative that aligns closely with the provided template and data.
      ----- Template Start -----
      Overview
      The chart displays Bitcoin's weekly price dynamics represented through an OHLC (Open, High, Low, Close) format, enriched with multiple technical indicators that provide depth to the market analysis.

      Latest Weekly Candle Breakdown:

      Opening Price: The week opened at [Insert Opening Price], indicating a start above the key psychological level of [Insert Psychological Level, if applicable].
      Weekly High: The high reached [Insert Weekly High], potentially testing the resistance level at [Insert Resistance Level, if applicable].
      Weekly Low: A low of [Insert Weekly Low], which could have tested the previous support zone at [Insert Support Zone, if applicable].
      Projected Close: A projected close at [Insert Projected Close] could suggest [Insert Interpretation of Market Sentiment] sentiment as the week concludes.
      Mid-Term Trend Analysis:
      
      Over the past five weeks, the price movement has shown a trend that could be described as [Insert Trend Interpretation].

      Candlestick Chart Patterns:
      This week's candlestick formation aligns with a pattern that typically [insert candlestick pattern implication, e.g., 'indicates indecision', 'foreshadows a continuation', 'predicts a reversal', etc.] in market sentiment. Such formations are critical for [insert purpose, e.g., 'timing entry and exit points', 'gauging potential trend reversals', 'setting risk management parameters', etc.].

      Potential Upside Resistance:
      
      Immediate Resistance: The recent high at [Insert Immediate Resistance Price] may act as immediate resistance, along with [Insert Other Resistance Levels] at [Insert Resistance Prices].
      Consolidation Zones: The area between [Insert Consolidation Zone Range] has acted as a consolidation zone, which might now present resistance.
      Downside Support:
      
      [Insert Moving Average Name]: Currently at [Insert MA Value], this level is considered a significant support level, informed by historical price reactions.
      Previous Support Zones: Previous lows around [Insert Previous Low Support Zone] have been observed as strong support levels, potentially indicating a floor if retested.
      
      On-Chain Indicator Insights:
      
      Realized Price & Multiples: Bitcoin's trading above the realized price and its multiples may indicate [Insert Interpretation Based on On-Chain Data].
      Thermocap Levels: The [Insert Specific Thermocap Level] is traditionally associated with market tops, serving as a key resistance level to watch.
      
      Conclusion:
      
      Given the current price action and historical price patterns, Bitcoin might display [Insert Interpretation of Market Resilience] with a possibility for [Insert Potential Market Outcome]. The immediate resistance at the recent high of [Insert Immediate Resistance Price] and the reaction around the [Insert Specific Thermocap Level] price are critical for assessing the ongoing market momentum. The support levels, including the [Insert Specific Moving Average] and the realized price, form robust defenses against downturns, with the zone around [Insert Specific Support Zone] acting as a pivotal line against bearish trends."
      """,
      "image_url": "https://secretsatoshis.github.io/Bitcoin-Weekly-Market-Update/ohlc_chart.png"
    },
    {
      "prompt": """
      Please write a YOY Price chart analysis  using the chart and data provided. Structure the narrative as follows:

      1. Integrate answers to the guiding questions seamlessly within the narrative without explicitly mentioning the questions. You must answer all questoins asked do not skip any guiding questions. They will be marked by "Guiding Questions:".
      2. Strictly adhere to the provided template, ensuring each section is populated with the correct corresponding data from the image.
      3. Refrain from adding any conclusions or deviating from the provided script in any way.
      4. Your focus should be on presenting a clear, coherent narrative that aligns closely with the provided template and data.
      ----- Template Start -----
      Overview
      The provided chart with Bitcoin's Year-Over-Year (YOY) return plotted against its price on a logarithmic scale is a vital tool for investors aiming to understand the cyclical nature of Bitcoin's market performance. The logarithmic scale smoothens Bitcoin's exponential price ascension, making the cyclical patterns of return more discernible.

      Investors should note the following cyclical trends evident from the YOY return:

Recurring Peaks and Troughs: The chart exhibits distinct cycles where YOY returns peak followed by periods of retracement. These cycles can be correlated with market sentiment, where peaks often coincide with heightened investor enthusiasm, and troughs may reflect periods of market skepticism or consolidation.

Expansion and Correction Phases: The cycles depicted in the chart can be broken down into phases of expansion, where YOY returns and prices surge, and correction, where they retract. Identifying the start and end of these phases could be critical for investors to time their market entry and exits more effectively.

Historical Cycle Lengths: By observing the duration between the peaks and troughs of YOY returns on the chart, investors can estimate the length of past Bitcoin cycles. Recognizing these patterns can provide insights into the potential timing of future cycles.

The latest data point shows a YOY return of [Insert Latest YOY Return]% at a price of [Insert Latest Bitcoin Price]. When placed in the context of Bitcoin's historical cycles, this point suggests we are in [Insert Interpretation of Market Phase: 'an upturn phase', 'a consolidation phase', etc.]. Comparing the current YOY return to previous cycles can help investors gauge whether we are [Insert Interpretation of Cycle Timing: 'early', 'mid-way', 'late'] in this phase, which is essential for strategizing upcoming investment decisions.
      """,
      "image_url": "https://secretsatoshis.github.io/Bitcoin-Weekly-Market-Update/log_return_yoy.png"
    }
  ]

  vision_summaries = {}
  for task in vision_tasks:
      summary = generate_and_edit_vision_content(
          task["prompt"], 
          task["image_url"], 
          chat_llm_chain
      )
      vision_summaries[task["prompt"]] = summary

  return vision_summaries

# Function to Generate and Edit Content
def generate_and_edit_content(prompt_url, template_function, chat_llm_chain):
  # Check if the input is a list (for multiple URLs) or a single URL
  if isinstance(prompt_url, list):
      # Generate initial prompt for multiple URLs
      initial_prompt = template_function(prompt_url)
  else:
      # Generate initial prompt for a single URL
      initial_prompt = template_function(prompt_url)

  # Rest of the function remains the same
  initial_output = chat_llm_chain.predict(human_input=initial_prompt)
  # Run Second Round Edits
  edit_prompt = analyze_output(initial_prompt, initial_output)
  edited_output = chat_llm_chain.predict(human_input=edit_prompt)
  return edited_output

# Mapping URLs to their respective prompt functions
prompt_functions = {
    "weekly_market_summary": generate_weekly_market_summary_prompt,
    "trading_week_performance": generate_price_trading_week_performance_prompt,
    "historical_performance": generate_price_historical_performance_prompt,
    "trading_range_analysis": generate_trading_range_analysis_prompt,
    "roi_analysis": generate_roi_analysis_prompt,
    "heat_map": generate_heatmap_prompt,
    "fundamentals": generate_fundamentals_prompt,
}

# Closing Signature Section
signature_template = f""""
Final Thoughts

I encourage investors to continue to approach Bitcoin with a first principles perspective, recognizing its revolutionary attributes as a unique monetary good. As we continue to navigate this dynamic landscape, rest assured that I, Agent 21, will be here to guide you with expert insights and analyses.
Until the next sunday,

Agent 21
"""

# Intro Discalimer Template Section
disclaimer_template = f"""
*Disclaimer*: Agent 21 is an AI persona created by Secret Satoshis. The insights and opinions expressed by Agent 21 are generated by a Large Language Model (Chat-GPT 4). Always conduct your own research and consult with financial professionals before making any investment decisions.

Agent 21 GitHub | Report Data

The Weekly Market Summary gives a foundational view of the Bitcoin market, delivery every Sunday Morning. The report provides updates on Bitcoin investment metrics and its short-term market outlook.
"""

def generate_full_report(chat_llm_chain,news_stories):
  sections = {}

  for section, url in urls.items():
      sections[section] = generate_and_edit_content(url, prompt_functions[section], chat_llm_chain)

  # Perform vision analysis and add the results to the report
  vision_analysis_results = perform_vision_analysis(chat_llm_chain)
  for prompt, summary in vision_analysis_results.items():
      sections[prompt] = summary

  news_impact_content = generate_and_edit_news_content(chat_llm_chain, news_stories)
  sections['news_impact'] = news_impact_content
    
  # Conclusion Template Section
  conclusion_input_template = f"""
  Agent 21, as we conclude this comprehensive analysis, I'd like you to distill the essence of each section into a coherent conclusion. The objective is to capture the key insights, findings, and recommendations from each section to provide our readers with a concise and actionable summary of the entire report. Use your expertise to bring together the various elements, highlighting the overarching narrative and the transformative potential of Bitcoin. Here are the summaries of each section:
  - Weekly Market Summary: {sections['weekly_market_summary']}
  - News Summary: {sections['news_impact']}
  - Trading Week Performance: {sections['trading_week_performance']}
  - Historical Performance: {sections['historical_performance']}
  - Trading Ragne: {sections['trading_range_analysis']}
  - ROI Analysis: {sections['roi_analysis']}
  - Heat Map: {sections['heat_map']}
  - Fundamentals: {sections['fundamentals']}

  Write a one paragraph summary of the conclusion. Include any relevant highlights and recommendations from each section.

  Guiding Questions:
  Based on the current report data and anlaysis, what is the future price outlook for bitcoin based on data provided?
  How can investors align their investment strategies with the evolving Bitcoin landscape?
  What is the bitcoin performance outlook for next week?
  """

  # Generate the conclusion and executive summary
  conclusion = chat_llm_chain.predict(human_input=conclusion_input_template.format(sections=sections))

  # Executive Summary Template Section
  executive_summary_input_template =f"""
  Agent 21, as we conclude this comprehensive analysis, I'd like you to distill the essence of each weekly market summary section into an executive summary. The objective is to capture the key insights, findings, and recommendations from each weekly market summary section to provide our readers with a concise and actionable summary of the entire report. Use your expertise to bring together the various elements, highlighting the overarching weekly market summary. This output should be in short 5 bullet format one setence each. Here are the summaries of each section:
  {conclusion}
  """
  # Conclusion Template Section
  instagram_template = """
  Given the full Weekly Market Update Report, I'd like to generate concise, engaging marketing copy for my instagram post.

  Your task is to extract key insights from the report and present them in a format similar to the example provided. Each point should include the same  emoji in the template, the same category title, and then a new short compelling statement that reflects the latest data. The copy should be structured as follows:

  - Example Format: 
  📈 Market Dynamics: Bitcoin reaches the $39K-$40K range, showcasing growth amid dynamic market conditions. 
  🌍 Major Developments: Anticipation builds for SEC's approval of Bitcoin ETFs, alongside impactful exchange regulatory events. 
  💡 Investment Insights: Bitcoin leads with a 6% weekly return, outperforming traditional assets like gold and government bonds. 

  Please ensure that:
  1. The insights are accurate and reflect the latest data in the report.
  2. The format is consistent with the provided example.
  3. The language is clear, engaging, and suitable for marketing purposes.

  Data:
  {}

  Template:
  📈 Market Dynamics: 
  🌍 OMajor Developments:
  💡 Investment Insights:
  """
  # Generate the executive summary
  executive_summary = chat_llm_chain.predict(human_input=executive_summary_input_template.format(conclusion=conclusion))

  # Compile the full report
  full_report = disclaimer_template + executive_summary + "\n".join(sections.values()) + "\n" + conclusion + signature_template
  instagram_post = chat_llm_chain.predict(human_input=instagram_template.format(full_report))
  
  # Append Instagram post content to the full report
  full_report = full_report + "\n\nInstagram Post Content:\n" + instagram_post
  
  with open('Weekly Market Summary.txt', 'w') as f:
    f.write(full_report)
    print("Report generated successfully!")
  return full_report
