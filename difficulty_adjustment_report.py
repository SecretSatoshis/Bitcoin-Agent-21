import pandas as pd

# URLs for Data Gathering
urls = {
    "difficulty_summary": 'https://secretsatoshis.github.io/Bitcoin-Difficulty-Report/difficulty_table.csv',
    "performance": 'https://secretsatoshis.github.io/Bitcoin-Difficulty-Report/performance_table.csv',
    "historical_performance": 'https://secretsatoshis.github.io/Bitcoin-Difficulty-Report/performance_table.csv',
    "fundamentals": 'https://secretsatoshis.github.io/Bitcoin-Difficulty-Report/fundamentals_table.csv',
    "price_valuation": 'https://secretsatoshis.github.io/Bitcoin-Difficulty-Report/valuation_table.csv',
    "onchain_valuation": 'https://secretsatoshis.github.io/Bitcoin-Difficulty-Report/valuation_table.csv',
    "relative_valuation": 'https://secretsatoshis.github.io/Bitcoin-Difficulty-Report/valuation_table.csv',
}

# Create Difficulty Adjustment Report Summary
def generate_difficulty_summary_prompt(data_path):
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

Section Goal: Provide an introduction to the difficulty report highlighting the ethos behind the report to provide a first principles perspective on where investors are in the bitcoin market cycle. Synced with the difficulty adjustment of the bitcoin network like how the network adjusts its difficulty to generate bitcoin blocks, the difficulty report provides a timely update on bitcoin investment metrics providing a long term perspective on the bitcoin market and its growth potential and current trajectory.

Data:
{}

----- Template Start -----

Introduction
Hello Bitcoin Investor,
Welcome to another edition of the Difficulty Adjustment Report. As your trusted Bitcoin Investment Analyst, I am here to guide you through the Bitcoin's market cycle, backed by the latest bitcoin blockchain and market data. Let's delve into the intricacies of the market as of [Report Date]. 

Current State of Bitcoin
As we stand on the date of [Report Date], the Bitcoin network showcases a difficulty level of [Difficulty] and a hashrate of [Hashrate] Exahash. The current supply of Bitcoin stands at [Bitcoin Supply], of the 21 Million coins to be created indicating a [percentage of bitcoin supply mined]. The last bitcoin difficulty adjustment occurred at blockheight [Block Height] with a [Last Difficulty Change] change.

Guiding Questions:

What does the current difficulty level growth indicate about the Bitcoin network's mining growth of this last difficulty period?

Market Insights
The market valuation of Bitcoin is currently at [Marketcap] billion, with each Bitcoin priced at [Price USD]. This translates to [Sats Per Dollar] per US Dollar $.

Guiding Questions:

What investment insisghts does the percentage change in price and hashrate over this difficulty period imply about the sentiment and market actions of bitcoin miners vs bitcoin investors ?

    """.format(table_string)

  return template

# Create Performance Report Content
def generate_performance_prompt(data_path):
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

Section Goal: Provide a comparative analysis of Bitcoin's difficulty period performance against other notable asset classes and indexes.This comparison offers a context for Bitcoin's standing and trajectory relative to traditional markets. Helping aid investors confidence in holding bitcoin vs other asset classes and puts bitcoins performance in context of macro markets.

Data:
{}

----- Template Start -----

Performance  Analysis

Let's now juxtapose Bitcoin's performance against other notable asset classes and indexes. As of [Report Date ], Bitcoin has experienced a [Difficulty Period Return] return.

Guiding Questions:

How does Bitcoin's difficulty period performance compare to the other traditional markets provided in the performance table?
What was the best performing Difficulty Period Return in the table during this difficulty period?
What was the worst performing Difficulty Period Return in the table during this difficulty period?
What insights can we learn from the Bitcoin difficulty period return vs these other traditional markets during this difficulty period?
    """.format(table_string,table_string)

  return template

# Create Performance Report Content
def generate_historical_performance_prompt(data_path):
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

Section Goal: Provide a comparative analysis of Bitcoin's historical performance against other notable asset classes and indexes.This comparison offers a context for Bitcoin's standing and trajectory relative to traditional markets. Helping aid investors confidence in holding bitcoin vs other asset classes and puts bitcoins performance in context of macro markets.

Data:
{}

----- Template Start -----

Historical Performance

Taking a glance at the historical data, Bitcoin has a year-to-date return of [YTD Return]. To provide a more nuanced perspective, let's delve deeper into the performance metrics over different time frames and compare it with other assets.

Guiding Questions:

How does the month-to-date (MTD) and 90-day return of Bitcoin compare to its year-to-date (YTD) return? What does this tell us about bitcoins short term medium term and long term returns?
How does bitcoins YTD return compare to its historical 4 Year CAGR? Are we above below or on trend from historical growth perspective? How does bitcoins 4 year CAGR compare to other assets?
How does Bitcoin's performance over different time frames compare to other assets in the table?
How can investors leverage the data in the performance table to understand bitcoins price performance better and make more informed investment decisions?
    """.format(table_string,table_string)

  return template

# Create Performance Report Content
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

Section Goal: a comprehensive view of the underlying fundamental metrics driving the Bitcoin network, capturing transactional activity, miner economics, and network usage. These metrics elucidate the health, growth, and engagement of the Bitcoin network, highlighting security, economic activity, and overall adoption. This provides investors a viewpoint into the fundamentals keeping them invested in the bitcoin market ensuring the first principles of the network are aligning with investment thesis about future usage and adoption of the bitcoin network.

Data:
{}

----- Template Start -----

On-Chain Transaction Activity
In the recent difficulty period, the Bitcoin network has displayed a [describe the general trend: vibrant/steady/slow] activity pace. The transaction count currently stands at [Transaction Count], [interpretation based on change: indicating a surge/drop/stability] in network transactions. This is mirrored by a transaction volume of [Transaction Volume] USD, [interpretation based on change: showcasing a high/low/moderate] volume of capital engagement in the network. Delving deeper, the average transaction size for this period stands at [Avg Transaction Size] USD, [interpretation based on change: reflecting larger/smaller/stable] individual transactions on average. Additionally, the network boasts [Active Address Count] active addresses, [interpretation based on change: highlighting a growing/steady/decreasing] community of participants in the Bitcoin ecosystem.

Guiding Questions:

What do the difficulty period performance of these transaction metrics say about the bitcoin network's economic activity?

Miner Economics
The [describe the general trend: vibrant/steady/slow] transaction activity in the Bitcoin network is fostering [describe the economic condition: substantial/moderate/low] revenues for miners. Currently, the miner revenue is at [Miner Revenue] USD, [interpretation based on change: indicating a healthy/challenging/stable] economic environment for mining activities within the network. This economic activity has also generated fees amounting to [Fees In USD] USD, which forms [calculate percentage of fees to miner revenue] percentage of the miner's revenue, showcasing a [interpretation based on percentage: healthy/challenged/stable] fee market.

Guiding Questions:

What does the fee in USD indicate about the network's fee market and its role in supporting network security?

Bitcoin Holder Behaviour
Analyzing the holder behavior within the Bitcoin network, we note that there are [+$10 USD Address] addresses holding balances greater than 10 USD, [interpretation based on change: indicating a substantial/moderate/low] number of users with investments in the network. Furthermore, [1+ Year Supply %] of the current supply has been stationary for over a year, [interpretation based on percentage: showcasing a strong/moderate/weak] holder base with a long-term investment outlook. This behavior is mirrored in the 1-year velocity of [1 Year Velocity], [interpretation based on velocity: indicating a trend of holding/trading/mixed behavior], underscoring [interpretation based on velocity: the growing/stable/decreasing] perception of Bitcoin as a reliable store of value.

Guiding Questions:

What does the number of +10 USD address balance performance across difficulty period and YTD indicate about the growth of investors holding bitcoin?
How does the 1+ year supply percentage reflect the long-term investment outlook of the holders?

    """.format(table_string)

  return template

# Create Price Valuation Report Content 
def generate_price_valuation_prompt(data_path):
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

Data:
{}

----- Template Start ----- 

Bitcoin Valuation Analysis

In this segment, we will analyze Bitcoin's current market price of [Current BTC Price]. We will scrutinize this figure through various analytical lenses, offering investors a comprehensive view of Bitcoin's market standing.

Our first lens, the Technical Price Model, is based on the 200-Day Moving Average, a trusted metric in the financial world. This model calculates the average of Bitcoin's closing prices over the past 200 days. As of now, the model price based on this average stands at [Model Price based on 200 Day MA], a [% to Model Price] difference from the current BTC price. Such deviations from this average often give us clues about market trends, offering insights into Bitcoin's long-term price trajectory. 

For those looking for entry and exit points, the buy target is set at 0.7 times the 200-day moving average price, pegging it at [Buy Target Price]. This means we are [% to Buy Target] away from this buy target. On the other hand, the sell target is 2.2 times the 200-day moving average price, translating to [Sell Target Price], which is [% to Sell Target] away from our current BTC price.
    """.format(table_string)
  return template

# Create Price On-Chain Valuation Report Content
def generate_onchain_valuation_prompt(data_path):
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

Data:
{}

----- Template Start -----

On-Chain Valuation Models

Shifting our focus to on-chain models, we're about to delve into the heart of Bitcoin – its blockchain data. These metrics give us direct insights into transactional demand, on-chain cost basis, and network revenue, serving as a gauage of Bitcoin's intrinsic value.

NVT Price Model: Transactional Demand
The NVT Price model juxtaposes Bitcoin's market capitalization with its on-chain transaction volume, offering a real-time pulse on its value relative to transactional activity. Currently, the model price stands at [NVT Price], with the model sell target set at [NVT Price Sell Target], which infers a [NVT Price % To Sell Target] percentage move to the models sell target. [Insight on Network Value vs. Transactional Activity].

Realized Price Model: On-Chain Cost Basis
Representing a historical lens, this model reflects the average price at which all bitcoins were last moved. Currently valued at [Realized Price], with the model sell target set at [Realized Price Sell Target], which infers a [Realized Price % To Sell Target] percentage move to the models sell target. [Insight on Market Sentiment and Historical Realized Cost Basis].

ThermoCap Price Model: Network Revenue
By contrasting Bitcoin's market capitalization with the cumulative mining revenue, the ThermoCap Price model highlights the economic value of network security. The model's current value is [ThermoCap Model Price], with the model sell target set at [ThermoCap Model Sell Target], which infers a [ThermoCap Model % To Sell Target] percentage move to the models sell target. [Insight on Network's Security and Economic Value based on miner revenue].

Stock-to-Flow (S/F) Model: Scarcity Value
The Stock-to-Flow model, emphasizing Bitcoin's scarcity, relates its price to the asset's scarcity. The model's ongoing valuation is [S/F Model Price], with the model sell target set at [S/F Model Sell Target], which infers a [S/F Model % To Sell Target] percentage move to the models sell target. [Insight on Bitcoin's Scarcity and Value Proposition].
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
Please generate a report section using the template and data provided. As you structure the narrative:

1. Integrate answers to the guiding questions seamlessly within the narrative without explicitly mentioning the questions. You must answer all questoins asked do not skip any guiding questions. They will be marked by "Guiding Questions:".
2. Strictly adhere to the provided template, ensuring each section is populated with the correct corresponding data from the table.
3. Refrain from adding any conclusions or deviating from the provided script in any way.
4. Your focus should be on presenting a clear, coherent narrative that aligns closely with the provided template and data.

Data:
{}

----- Template Start -----

Relative Valuation Models

In the vast landscape of investment assets, it's crucial to position Bitcoin within a comparative framework. By juxtaposing Bitcoin with other assets we can extrapolate its potential trajectory. Allow me to guide you through this comparative lens.

Silver's Legacy:
Bitcoin stands presently at [Bitcoin Price]. Projecting its trajectory to possibly mirror the market cap of all mined silver in the next decade, our model presents a Sell Target at [Silver Market Cap Sell Target], a [Silver Market Cap % To Sell Target] difference from the prevailing Bitcoin price.

The Monarch's Money – UK M0:
When we juxtapose Bitcoin with the UK's entire monetary base (M0), we can compare bitcoin to a historical global reserve currency. The Sell Target, which aligns Bitcoin's value with the UK's M0, is positioned at [UK M0 Price Sell Target], a difference of [UK M0 Price% To Sell Target].

Tech Titan – Apple's Market Cap:
Drawing a parallel between Bitcoin and Apple's market capitalization provides another lens of analysis. The  Sell Target, symbolizing Bitcoin's potential parity with Apple's market cap, stands at [Apple Market Cap Sell Target], marking a [Apple Market Cap % To Sell Target] difference.

Dollar Dominance – US M0 Money Supply:
Comparing Bitcoin with the US's monetary base (M0) reveals bitcoins potential to rival the leading fiat currency. The Sell Target, where Bitcoin meets the US M0 in value, is discerned at [US M0 Price Sell Target], with a [US M0 Price % To Sell Target] gap.

The Golden Standard:
Gold, an age-old store of value, offers a significant benchmark. Envisioning Bitcoin to parallel the market cap of all mined gold in a decade, the Sell Target, marking Bitcoin's potential gold equivalence, is pegged at [Gold Market Cap Sell Target], a [Gold Market Cap % To Sell Target] variance.

Guiding Questions:
How do the relative valuation models assist in understanding Bitcoin's growth trajectory and adoption cycle?
What insights can investors glean from these comparisons to formulate investment strategies?
    """.format(table_string)

  return template

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
4. Ensure data is formatted consistently for the relevant data type percentages, currency, decimals, including capitalization, formating, and punctuation.

Original Data:
{original_data}

Generated Content:
{ai_output}

Rewriten Content:
"""
    return analysis_prompt

# Mapping URLs to their respective prompt functions
prompt_functions = {
    "difficulty_summary": generate_difficulty_summary_prompt,
    "performance": generate_performance_prompt,
    "historical_performance": generate_historical_performance_prompt,
    "fundamentals": generate_fundamentals_prompt,
    "price_valuation": generate_price_valuation_prompt,
    "onchain_valuation": generate_onchain_valuation_prompt,
    "relative_valuation": generate_relative_valuation_prompt,
}

# Function to Generate and Edit Content
def generate_and_edit_content(prompt_url, template_function, chat_llm_chain):
    initial_prompt = template_function(prompt_url)
    initial_output = chat_llm_chain.predict(human_input=initial_prompt)
    # Run Second Round Edits
    edit_prompt = analyze_output(initial_prompt, initial_output)
    edited_output = chat_llm_chain.predict(human_input=edit_prompt)
    return edited_output

# Closing Signature Section
signature_template = f""""
Final Thoughts

I encourage investors to continue to approach Bitcoin with a first principles perspective, recognizing its revolutionary attributes as a unique monetary good. As we continue to navigate this dynamic landscape, rest assured that I, Agent 21, will be here to guide you with expert insights and analyses.
Until the next difficulty adjustment,

Agent 21
"""

# Intro Discalimer Template Section
disclaimer_template = f"""
*Disclaimer*: Agent 21 is an AI persona created by Secret Satoshis. The insights and opinions expressed by Agent 21 are generated by a Large Language Model (Chat-GPT 4). Always conduct your own research and consult with financial professionals before making any investment decisions.

Agent 21 GitHub | Report Data

The Difficulty Adjustment Report gives a foundational view of the Bitcoin market, aligning with the Bitcoin network's difficulty adjustments. The report provides updates on Bitcoin on-chain metrics and its long-term market outlook.
"""

# Intro Discalimer Template Section
executive_summary = f"""
Market Trends and Performance: Uncover the latest shifts and performance indicators in the Bitcoin market, showcasing its performance in the broader financial landscape.

Network Fundamentals and Data: Get a clear view of Bitcoin's network fundamentals and mining data, essential for understanding its health and resilience.

Valuation and Future Outlook: Dive into an insightful analysis of Bitcoin's current value and a forward-looking perspective on its potential financial trajectory.
"""
# Conclusion Template Section
instagram_template = """
Given the full Difficulty Adjustment Report, I'd like to generate concise, engaging marketing copy for my instagram post.

Your task is to extract key insights from the report and present them in a format similar to the example provided. Each point should include the same  emoji in the template, the same category title, and then a new short compelling statement that reflects the latest data. The copy should be structured as follows:

- Example Format: 
👾 Network Dynamics: Bitcoin's +5.07% difficulty adjustment signals a resilient, growing mining sector. 
🌐 On-Chain Activity: Despite slight dips, transaction volumes remain robust at $5.49 Billion. 
🔍 Valuation Insight: Bitcoin's current $37,482 price suggests significant growth potential.

Please ensure that:
1. The insights are accurate and reflect the latest data in the report.
2. The format is consistent with the provided example.
3. The language is clear, engaging, and suitable for marketing purposes.

Data:
{}

Template:
👾 Network Dynamics: 
🌐 On-Chain Activity:
🔍 Valuation Insight:
"""

def generate_full_report(chat_llm_chain):
  sections = {}
  for section, url in urls.items():
      sections[section] = generate_and_edit_content(url, prompt_functions[section], chat_llm_chain)
  
  # Conclusion Template Section
  conclusion_input_template = f"""
  Agent 21, as we conclude this comprehensive analysis, I'd like you to distill the essence of each section into a coherent conclusion. The objective is to capture the key insights, findings, and recommendations from each section to provide our readers with a concise and actionable summary of the entire report. Use your expertise to bring together the various elements, highlighting the overarching narrative and the transformative potential of Bitcoin. Here are the summaries of each section:
  - Difficulty Adjustment Summary: {sections['difficulty_summary']}
  - Performance: {sections['performance']}
  - Historical Performance: {sections['historical_performance']}
  - Fundamentals: {sections['fundamentals']}
  - Price Valuation: {sections['price_valuation']}
  - On-chain Valuation: {sections['onchain_valuation']}
  - Relative Valuation: {sections['relative_valuation']}

  Write a one paragraph summary of the conclusion. Include any relevant highlights and recommendations from each section.

  Guiding Questions:
  Based on the current report data and anlaysis, what is the future price outlook for bitcoin based on data provided?
  How can investors align their investment strategies with the evolving Bitcoin landscape?
  """

  # Generate the conclusion and executive summary
  conclusion = chat_llm_chain.predict(human_input=conclusion_input_template.format(sections=sections))
  
  # Compile the full report
  full_report = disclaimer_template + executive_summary + "\n".join(sections.values()) + "\n" + conclusion + signature_template
  instagram_post = chat_llm_chain.predict(human_input=instagram_template.format(full_report))
  
  # Append Instagram post content to the full report
  full_report = full_report + "\n\nInstagram Post Content:\n" + instagram_post

  with open('Difficulty Adjustment Report.txt', 'w') as f:
    f.write(full_report)
    print("Report generated successfully!")
  return full_report





