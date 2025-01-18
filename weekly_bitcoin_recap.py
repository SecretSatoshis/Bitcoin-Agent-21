import openai
import pandas as pd
import io

client = openai.OpenAI(
    api_key="API_KEY_HERE"
)


ASSISTANT_ID = "asst_X3QwnFl26Uhkvb48JPwHDS0D"


urls = {
    "weekly_bitcoin_recap_summary": "https://secretsatoshis.github.io/Bitcoin-Report-Library/csv/weekly_bitcoin_recap_summary.csv",
    "historical_performance": "https://secretsatoshis.github.io/Bitcoin-Report-Library/csv/weekly_bitcoin_recap_performance_table.csv",
    "heat_map": "https://secretsatoshis.github.io/Bitcoin-Report-Library/csv/monthly_heatmap_data.csv",
    "mtd_return_comparison": "https://secretsatoshis.github.io/Bitcoin-Report-Library/csv/weekly_bitcoin_recap_mtd_return_comparison.csv",
    "ytd_return_comparison": "https://secretsatoshis.github.io/Bitcoin-Report-Library/csv/weekly_bitcoin_recap_ytd_return_comparison.csv",
    "relative_valuation": "https://secretsatoshis.github.io/Bitcoin-Report-Library/csv/weekly_bitcoin_recap_relative_value_comparison.csv",
}


PROMPT_LIBRARY = {
    "news_section": {
        "processing_type": "text",
        "instruction": """

        Please generate the news report section of the Weekly Bitcoin Recap For Secret Satoshis Newsletter using the template and data provided. 

        Write your response tone, context and narrative like you are writing for hedge fund portfolio managers and investment advisors. 

        General Rules:
        - Write in a formal and structured tone that aligns with institutional investors' expectations.
        - Use the data provided to craft the narrative. Avoid adding speculative or unverified content.  
        - Do not add personal opinions or diverge from the data.

        News Section Rules:
        1. Integrate answers to the guiding questions seamlessly within the narrative without explicitly mentioning the questions. You must answer all questions asked do not skip any guiding questions. They will be marked by "Guiding Questions:".
        2. Strictly adhere to the provided template, ensuring each section is populated with the correct corresponding data from the table.
        3. Refrain from adding any conclusions or deviating from the provided template in any way.
        4. Your focus should be on presenting a clear, coherent narrative that aligns closely with the provided template and data.
        5. Format the provided news stories into bullet points with the news source name provided in (Reported By:) at the end.
        6. Do not put "-" in front of each news story just txt no special formatting needed

        """,
        "template": """
        Complete this newsletter section template with the provided news stories URLs as news stories. Return the completed template response only.

        News Stories:
        {data}

       ----- Template Start -----

        News Stories:
        [First news story headline]. (Reported By: [News source])
        [Second news story headline]. (Reported By: [News source])
        [Next news story headline as per the provided news stories].

        News Impact:

        Given the above news stories, the potential impact on Bitcoin's price and overall adoption can be summarized as follows:
        [Write a concise 3-4 sentence summary that synthesizes the overall impact of the provided news stories. Focus on how these developments collectively influence Bitcoin’s broader market narrative, investor sentiment, and price trends. Avoid summarizing each news story individually; instead, identify common themes or trends that emerge from the collective news and assess their combined effect on market positioning and future outlook.]
                """,
    },
    "weekly_bitcoin_recap_summary": {
        "processing_type": "csv",
        "instruction": """

        Please generate the weekly summary report section of the Weekly Bitcoin Recap For Secret Satoshis Newsletter using the template and data provided. 

        Write your response tone, context and narrative like you are writing for hedge fund portfolio managers and investment advisors. 

        General Rules:
        - Write in a formal and structured tone that aligns with institutional investors' expectations.
        - Use the data provided to craft the narrative. Avoid adding speculative or unverified content.  
        - Do not add personal opinions or diverge from the data.

        """,
        "template": """
        Complete this newsletter section template with the provided data as reference. Return the completed template response only.
        
        Weekly Bitcoin Recap Summary Data:
        {data}
        Date:
        {report_date}

        ----- Template Start -----

        Current State Of The Bitcoin Market

        Market Activity

        As of [Report Date], Bitcoin’s circulating supply has reached [Bitcoin Supply] BTC—edging closer to the 21 million cap and reinforcing the narrative of its built-in scarcity.

        Turning to price, a single Bitcoin is currently trading at [Bitcoin Price USD], giving it a total market capitalization of [Bitcoin Marketcap]. At this price, one US Dollar now buys [Sats Per Dollar] satoshis—a reflection of Bitcoin’s evolving purchasing power as adoption continues to grow.
        
        On-Chain Activity

        Over the past 7 days, Bitcoin miners earned an average of $[Bitcoin Miner Revenue] per day, underscoring the [network health – robust, declining, or stable] revenue generated by the network.

        This revenue stems directly from transaction fees and block rewards, supported by an average daily transaction volume of $[Bitcoin Transaction Volume] during the same period.

        This activity highlights Bitcoin’s role as a [functional asset/store of value/medium of exchange], with [network liquidity interpretation] liquidity and active participation reinforcing its use case as both a store of value and medium of exchange.
       
        Market Adoption

        Investor sentiment, measured by the Fear and Greed Index, is classified as [Bitcoin Market Sentiment], this index consolidates multiple market indicators—such as volatility, trading volume, social media activity, and momentum to provide a snapshot of collective market emotions. 

        From an on-chain valuation perspective, Bitcoin is currently viewed as [Bitcoin Valuation]. This assessment, derived from a combination of valuation models and on-chain data, suggests that Bitcoin is [undervalued, fairly valued, overvalued] in relation to its network activity and market performance.
        
        """,
    },
    "historical_performance": {
        "processing_type": "csv",
        "instruction": """

        Please generate the historical performance report section of the Weekly Bitcoin Recap For Secret Satoshis Newsletter using the template and data provided. 

        Write your response tone, context and narrative like you are writing for hedge fund portfolio managers and investment advisors. 

        General Rules:
        - Write in a formal and structured tone that aligns with institutional investors' expectations.
        - Use the data provided to craft the narrative. Avoid adding speculative or unverified content.  
        - Do not add personal opinions or diverge from the data.

        Historical Performance Rules:
        - Round all percentage and currency values to two decimal places.
        - If no asset outperformed Bitcoin, the focus remains on Bitcoin’s leadership in performance across markets, underscoring its role as the dominant growth driver this week.  

        """,
        "template": """
        Complete this newsletter section template with the provided data as reference. Return the completed template response only.
        
        Historical Performance Data:
        {data}
        Date:
        {report_date}

        ----- Template Start -----

        ## Template completion notes ## Make sure all % values are formatted correctly to two decimal places Example % value should be 5.00%.

        Equity Market Indexes 

        Bitcoin’s week-to-date return of [7 Day Return]% is measured against major equity benchmarks, including the S&P 500 (SPY at [SPY 7 Day Return]%), the Nasdaq-100 (QQQ at [QQQ 7 Day Return]%), the US Total Stock Market (VTI at [VTI 7 Day Return]%), and International Equities (VXUS at [VXUS 7 Day Return]%). This comparisons provide insight into Bitcoin’s[alignment, divergence, or independent behavior] in the context of broader market trends and macroeconomic factors.

        Sector and Equity Benchmarking  

        Bitcoin’s performance relative to stock market sectors provides insight into its market positioning, with Technology (XLK at [XLK 7 Day Return]%), Financials (XLF at [XLF 7 Day Return]%), Energy (XLE at [XLE 7 Day Return]%), and Real Estate (XLRE at [XLRE 7 Day Return]%) reflecting trends across key sectors and framing Bitcoin’s role as a [growth asset, tech-aligned play, or uncorrelated diversifier].  
        
        Macro Asset Class Performance  

        Bitcoin’s comparative performance against key macro assets provides a lens for assessing its role in diversified portfolios, ,Gold (GLD at [GLD 7 Day Return]%), the US Dollar Index (DXY at [DXY 7 Day Return]%), Aggregate Bonds (AGG at [AGG 7 Day Return]%), and the Bloomberg Commodity Index (BCOM at [BCOM 7 Day Return]%) frame Bitcoin’s positioning as an [alternative store of value, inflation hedge, or speculative growth asset].  

        Bitcoin Industry Performance  

        Bitcoin-related equities further illustrate market sentiment and adoption, as MicroStrategy (MSTR at [MSTR 7 Day Return]%), Coinbase (COIN at [COIN 7 Day Return]%), Block (SQ at [SQ 7 Day Return]%), and Bitcoin Miners ETF (WGMI at [WGMI 7 Day Return]%) showcase Bitcoin’s positioning as a [leveraged industry play, mining-focused growth asset, or tech-aligned investment].
        
        Summary  

        Bitcoin’s [7 Day Return]% compared to global equities, sector ETFs, macro assets, and Bitcoin-related equities underscores its role as a [growth asset, diversifier, speculative instrument, etc].  
        - Correlation: Bitcoin’s relationship with [Top Correlated Asset] reflects [risk-on sentiment or alignment with macro trends], while its divergence from [Lowest Correlated Asset] highlights [hedge potential or low correlation benefits].  
        - Performance: This week’s top performer, [Top Performing Asset Above Bitcoin] (at [Top Performing Asset 7 Day Return]%), exceeded Bitcoin’s return, reinforcing sector strength or macro tailwinds.  
       
        Bitcoin’s position as a [growth outperformer or diversifier, etc] continues to evolve, but its relative performance against correlated assets provides valuable insights into market sentiment.

        """,
    },
    "heat_map": {
        "processing_type": "csv",
        "instruction": """

        Please generate the heat map report section of the Weekly Bitcoin Recap For Secret Satoshis Newsletter using the template and data provided. 

        Write your response tone, context and narrative like you are writing for hedge fund portfolio managers and investment advisors. 

        General Rules:
        - Write in a formal and structured tone that aligns with institutional investors' expectations.
        - Use the data provided to craft the narrative. Avoid adding speculative or unverified content.  
        - Do not add personal opinions or diverge from the data.

        Heatmap Section Rules:
        1. The report date is [Report Date] and should be treated as the most recent point of reference for heatmap analysis. Use [Report Date] to frame insights around the progression of the month, factoring in how much of the month has passed and what remains.
        2. Reflect the timing of the report date within the month to ensure relevant insights.  
        3. Provide forward-looking commentary that aligns with the remaining trading days in the period.  
        4. Do not speculate beyond the data provided.  
        5. Round all percentages to two decimal places example: 100.00%.

        """,
        "template": """

        Complete this newsletter section template with the provided data as reference. Return the completed template response only.
        
        Monthly Heat Map Data:
        {data}
        Date:
        {report_date}

        ----- Template Start -----

        Bitcoin Monthly Heatmap Overview and Analysis  

        Report Date: {report_date}  
        Time Context: [time_context]  

        ---

        Monthly Heatmap Insights  
        {report_date}  

        The heatmap reflects Bitcoin’s average return for [month_name] throughout its trading history. The average return for this month stands at [Current Month's Historical Average Return]%, establishing a benchmark for assessing Bitcoin’s performance this period.  

        ---

        Current Data Interpretation  

        Bitcoin’s performance for [month_name] currently stands at [Current Month's Performance]%.  
        ---

        Market Outlook for the Month  

        Considering both historical benchmarks and current performance data, the market outlook for [month_name] is framed as:  
        - [market_focus]  

                """,
    },
    "mtd_return_comparison": {
        "processing_type": "csv",
        "instruction": """

        Please generate the Month-to-Date (MTD) Return Comparison section of the Weekly Bitcoin Recap for the Secret Satoshis Newsletter using the provided template and data.  

        Write your response tone, context and narrative like you are writing for hedge fund portfolio managers and investment advisors. 

        General Rules:  
        - Maintain a professional tone aligned with institutional investor standards.  
        - Base insights strictly on the provided data without speculation.  
        - Round all financial figures and percentages to two decimal places.  
        
        MTD Return Comparison Section Rules:  
        1. The report date is [Report Date] and serves as the most recent point of reference for return analysis.  
        2. Compare current MTD performance to the historical average and comment on deviation (positive or negative) from expectations.  
        3. Adapt observations based on how the current return compares to past performance. If returns are tracking unusually high or low, highlight that trend.  
        4. Tailor the final observations and outlook section based on the timing within the month to provide actionable insights.  
        5. Provide deviation analysis by comparing the current month-to-date (MTD) return to the historical average for the month. Highlight whether Bitcoin is outperforming or underperforming.  
        6. Adapt time-based commentary dynamically to reflect insights, rather than simple statements about time remaining in the month.  
        7. Emphasize potential inflection points, highlighting if historical data suggests late-month volatility or early stagnation.  
        """,
        "template": """

        Complete this newsletter section template with the provided data. Return the completed section only.  

        MTD Return Data:  
        {data}
        
        Date:  
        {report_date}

        ----- Template Start -----  

        Bitcoin Month-to-Date Return Comparison  

        Report Date: [report_date]  
        Time Context: [time_context]  

        ---  

        MTD Performance Snapshot  
        [report_date]  

        “Bitcoin’s performance for [month_name] currently stands at [Current Month’s Performance]%, compared to the historical median return of [Current Day of Month Historical Median Return]% for this point in the month.”

        [dynamic_observation based on deviation and variance in data]  

        Based on historical trends, if Bitcoin follows its median path, the projected end-of-month price would be approximately [Projected Price Based on Median Path].  

        ---  

        Scenario Analysis  

        Historical data suggests the following potential price outcomes for Bitcoin by the end of [month_name]:  

        Base-Case (Median Historical Performance):  
        Projected Return: [Current Month's Historical Median Return]% | Projected Price: $[Projected Price Based on Median Path]  

        Bull-Case Scenario (Top 25% of Historical Returns):  
        Projected Return: [Top Quartile Return for Month]% | Projected Price: $[Projected Price Based on Top Quartile Path]  

        Bear-Case Scenario (Bottom 25% of Historical Returns):  
        Projected Return: [Bottom Quartile Return for Month]% | Projected Price: $[Projected Price Based on Bottom Quartile Path]  

        ---  

        Observations and Outlook  

        Bitcoin is projected to end the month within a range of $[Bottom Quartile Path Price] to $[Top Quartile Path Price], providing a framework to assess deviations from historical patterns.  
        
        As we conclude this week’s analysis, Bitcoin’s performance of [current_monthly_return]% [exceeds/tracks in line with/falls below] the historical average of [historical_monthly_average_return]% for this point in the month, offering valuable insight into its current momentum.

        [If outperforming: This outperformance may prompt investors to hold or reduce short-term additions, keeping core positions intact to ride ongoing momentum.]  
        [If aligning: With performance tracking near historical norms, maintaining existing allocations while staying flexible for potential dips appears prudent.]  
        [If underperforming: As Bitcoin lags behind historical averages, investors may view this as an opportunity to accumulate, anticipating a potential reversal.]  

        """,
    },
    "weekly_btc_usd": {
        "processing_type": "vision",
        "instruction": """
        Please generate the weekly bitcoin price chart analysis (OHLC BTC/USD) report section of the Weekly Bitcoin Recap For Secret Satoshis Newsletter using the template and data provided. 

        Write your response tone, context and narrative like you are writing for hedge fund portfolio managers and investment advisors. 

        General Rules:
        - Write in a formal and structured tone that aligns with institutional investors' expectations.
        - Use the data provided to craft the narrative. Avoid adding speculative or unverified content.  
        - Do not add personal opinions or diverge from the data.
        - Do not add  in output anywhere
        
        Weekly Bitcoin Price Chart Analysis Rules:
        - Review the weekly Bitcoin price OHLC chart by capturing critical information including open, high, low, and close prices (OHLC). Clearly document each component to ensure data integrity.
        - Analyze the weekly candlestick pattern to assess price direction, market sentiment, and potential trend reversals or continuations.
        - Identify and document key support and resistance levels observed on the chart. Discuss interactions with these levels (breakouts, rejections, etc.).
        - Provide insights on price movement, noting if the price trended higher, lower, or consolidated.
        - Mention interactions with trendlines (bullish/bearish) and long-term moving averages. Note if Bitcoin’s price aligns with or diverges from major technical levels.
        - Discuss the significance of psychological price barriers and their role in influencing market sentiment.
        - Outline the likelihood of potential bullish, base, and bearish price scenarios based on observed price action and the proximity to major technical levels.
        - Avoid speculative predictions and ensure commentary remains data-driven. Clearly state observations without assuming future outcomes.

        """,
        "template": """

        Complete this newsletter section template with the provided data as reference. Return the completed template response only.

        ----- Template Start -----

        ## Template notes ## Complete the [placeholder] based on the data provided in the chart

        Overview of the Weekly BTC/USD Chart:

        This week, Bitcoin [observed movement], with a [change] of [Weekly Performance]%, closing at approximately $[Current Price]. This movement [interpretation based on chart analysis].
        
        1. OHLC Review: (1-2 sentences Max)
        Analyze the price movement over the last week, highlighting the last weekly open, high, low, and close in a one sentence summary. Then discuss how these price points reflect the market’s strength, weakness, or indecision. Mention any significant price levels or trends observed from the chart.
        
        2. Candlestick Analysis: (1-2 sentences Max)
        The weekly candle shows [candle characteristics], suggesting [interpretation based on candlestick analysis].
        
        Provide a comprehensive analysis of the weekly price chart, integrating the following aspects:
        
        1. Price Trends and Directionality: (1-2 sentences Max)
        Assess the current weekly price trend (uptrend, downtrend, or sideways movement) and explain how this fits within the broader market context. Offer insights on potential price directionality based on the weekly OHLC chart, and whether the chart indicates any upcoming shifts in market momentum or trend.
        
        2. Support and Resistance Analysis: (1-2 sentences Max)
        Highlight key support and resistance levels based on the chart data. Explain how these levels influence future price action and whether they represent significant barriers or potential breakouts for price movement in either direction.
        
        Weekly Chart Scenario Outlook:

        Bullish Scenario: (1-2 sentences Max)
	    Develop a bullish scenario based on the current weekly chart and analysis. Identify conditions that could trigger upward momentum, such as key resistance breakouts or bullish candlestick patterns. Highlight the next resistance levels and discuss how sustained buying pressure might drive further price appreciation.

        Base Scenario: (1-2 sentences Max)
        Craft a base case scenario reflecting consolidation or sideways movement. Analyze the price range within which Bitcoin is likely to trade, focusing on key support and resistance levels. Address factors contributing to market indecision, and describe the conditions under which the price may break out of this range.

        Bearish Scenario: (1-2 sentences Max)
        Formulate a bearish scenario by assessing the risk of Bitcoin breaching critical support levels. Evaluate the implications of downward price action, including potential sell-offs or increased volatility. Outline the next support zones and discuss the broader market conditions that might amplify bearish sentiment.

        Summary of Outlook: (1-2 sentences Max)
        Provide a concise 1-2 sentence overview of the week’s likely price trajectory, drawing from the bullish, base, and bearish scenarios. Indicate the most probable scenario based on current trends and technical indicators, and summarize key levels to watch for potential market shifts.

        ----- Template End -----

        """,
    },
    "ytd_return_comparison": {
        "processing_type": "csv",
        "instruction": """

        Please generate the Year-to-Date (YTD) Return Comparison section of the Weekly Bitcoin Recap for the Secret Satoshis Newsletter using the provided template and data.  

        Write your response tone, context, and narrative like you are writing for hedge fund portfolio managers and investment advisors.  

        General Rules:  
        - Maintain a professional tone aligned with institutional investor standards.  
        - Base insights strictly on the provided data without speculation.  
        - Round all financial figures and percentages to two decimal places.  
        

        YTD Return Comparison Section Rules:  
        1. The report date is [Report Date] and serves as the most recent point of reference for return analysis.  
        2. Compare current YTD performance to the historical median and comment on deviation (positive or negative) from expectations.  
        3. Adapt observations based on how the current return compares to past performance. If returns are tracking unusually high or low, highlight that trend.  
        4. Tailor the final observations and outlook section based on the timing within the year to provide actionable insights.  
        5. Provide deviation analysis by comparing the current year-to-date (YTD) return to the historical median return for the year. Highlight whether Bitcoin is outperforming or underperforming.  
        6. Emphasize potential inflection points, addressing years of significant deviation or high volatility.  
        7. Incorporate variance by noting the spread between top and bottom quartile YTD returns to highlight the potential for volatility throughout the year.  

        """,
        "template": """

        Complete this newsletter section template with the provided data. Return the completed section only.  

        YTD Return Data:  
        {data}
        
        Date:  
        {report_date}

        ----- Template Start -----  

        Bitcoin Year-to-Date Return Comparison  

        Report Date: [report_date]  
        Time Context: Year-to-Date  

        ---  

        YTD Performance Snapshot  
        [report_date]  

        Bitcoin’s YTD performance currently stands at [Current YTD Performance]%, while the historical median return for this point in the year is [Current Day of Year Historical Median Return]%.  

        [dynamic_observation based on deviation and variance in data]  

        ---  
        Year End Price Scenario Analysis  

        Based on historical trends, if Bitcoin follows the median return path, the projected end-of-year price would be approximately [Projected Price Based on Median Path].  

        Historical data suggests the following potential price outcomes for Bitcoin by the end of the year:  

        Median Historical Performance:  
        Projected Return: [Historical Median Return]% | Projected Price: $[Projected Price Based on Median Path]  

        Best-Case Scenario (Top 25% of Historical Returns):  
        Projected Return: [Top Quartile Return for Year]% | Projected Price: $[Projected Price Based on Top Quartile Path]  

        Worst-Case Scenario (Bottom 25% of Historical Returns):  
        Projected Return: [Bottom Quartile Return for Year]% | Projected Price: $[Projected Price Based on Bottom Quartile Path]  

        ---  

        Observations and Outlook  

        [dynamic_observation]  

        [dynamic_end_guidance based on current timing of the year]  

        This analysis serves as a guide for evaluating Bitcoin’s performance for the remainder of the year. By comparing Bitcoin’s trajectory to historical data, readers gain valuable context to track price action, anticipate potential shifts, and make informed decisions.  

        """,
    },
    "relative_valuation": {
        "processing_type": "csv",
        "instruction": """

        Please generate the Relative Valuation Analysis section of the Weekly Bitcoin Recap for the Secret Satoshis Newsletter using the provided chart data.  

        Write in a formal, aspirational tone suitable for hedge fund portfolio managers and institutional investors.  

        General Rules:  
        General Rules:
        - Write in a formal and structured tone that aligns with institutional investors' expectations.
        - Use the data provided to craft the narrative. Avoid adding speculative or unverified content.  
        - Do not add personal opinions or diverge from the data. 
        - Round all financial figures and percentages to two decimal places.  


        Relative Valuation Analysis Section Rules:  
        1. Begin with an introduction to Bitcoin’s valuation relative to major global assets. State the current price and market cap of Bitcoin, highlighting its role as a significant macro asset.  
        2. Present a table summarizing Bitcoin’s projected price at parity with key assets.
        3. Include a section discussing assets Bitcoin has surpassed and those it is approaching, with a focus on the implications of these valuation milestones.  
        4. Provide aspirational targets by illustrating what Bitcoin’s price would be if it were to match larger assets.
        5. Leave placeholders for the AI to dynamically interpret surpassed, approaching, and aspirational targets based on the latest data.  
        6. Focus on Bitcoin’s evolving market valuation relative to key global assets, emphasizing its emerging role as a macroeconomic asset.  
        7. Clearly articulate Bitcoin’s standing compared to major assets and its path toward parity with larger asset classes. 

        """,
        "template": """

        Complete this newsletter section template with the provided chart data. Return the completed section only.  

        Report Data:  
        {data}
        
        Date:  
        {report_date}

        ----- Template Start -----  

        Bitcoin Relative Valuation Analysis  

        Report Date: [report_date]  
        ---  

        Bitcoin Relative Valuation Table  

        To understand how Bitcoin’s price could evolve, we compare its market cap to major assets.

        | Asset                      | Market Cap ($T) | Projected BTC Price at Parity ($) |  
        |----------------------------|-----------------|-----------------------------------|  
        [Re-write All Assets Provided With Bitcoin ranked correctly based on marketcap, ensure bitcoin is proper order based on marketcap]

        ---  

        Implications of Bitcoin’s Current Valuation 

        - Surpassed Assets:  
        Bitcoin’s market cap has already passed [Insert interpretation of assets Bitcoin has surpassed, their significance, and what this indicates about market positioning.]  

        - Approaching Valuation:  
        Bitcoin is closing in on the market caps of [Insert interpretation of the two assets Bitcoin is approaching above it in market cap terms, the significance of this trajectory, and potential next steps.]  

        - Aspirational Targets:  
        Looking further ahead, [Insert analysis of aspirational targets, their significance, and what achieving these thresholds would indicate for Bitcoin’s long-term valuation and market role.]  

        Bitcoin’s valuation milestones continue to reflect its increasing role as a global macro asset. As Bitcoin advances toward parity with larger assets, the market signals sustained institutional adoption and expanding recognition of its role as a store of value.
        
        For investors, these valuation insights reinforce Bitcoin’s asymmetric growth potential, offering opportunities for strategic positioning as the asset evolves in the global financial landscape.

        """,
    },
    "conclusion_section": {
        "processing_type": "static",
        "instruction": """
        Please summarize the key points from each section into a coherent and actionable conclusion for the Weekly Bitcoin Recap.
        Use the provided summaries to craft a concise, forward-looking outlook for the Bitcoin market.
        
        - Write for hedge fund managers and professional investors.
        - Maintain a formal, structured, and professional tone.
        - Avoid speculative language and ensure the summary is data-driven.
        """,
        "template": """
        Agent 21, as we complete this Weekly Bitcoin Recap, summarize the main points of each section into a coherent conclusion summary. 
    
        The objective is to capture the key insights, findings, and recommendations from each section to provide our readers with a concise and actionable summary of the entire Weekly Bitcoin Recap.
        
        Here are the summaries of each section:
        - Weekly Bitcoin Recap Summary: {weekly_bitcoin_recap_summary}
        - News Summary: {news_impact}
        - Historical Performance: {historical_performance}
        - Heat Map: {heat_map}
        - Month To Date Return Comparison: {mtd_return_comparison}
        - Year To Date Return Comparison: {ytd_return_comparison}
        - Weekly BTC/USD Chart Summary: {weekly_btc_usd}
        - Relative Valuation: {relative_valuation_analysis}
        
        Write a one-paragraph conclusion summarizing the above, providing a forward-looking outlook for the weeks ahead in the Bitcoin market.
        """,
    },
}


REVIEW_PROMPT = """
        Given the original data and generated section response, your task is to ensure this content adheres to the highest standards of accuracy and presentation. Analyze the content based on the following criteria and rewrite the content as the final draft:

        Logic Review:
        1. Verify the correctness of the data points mentioned in the generated content against the original data and prompt. 
        2. Evaluate the insights provided in the generated content. Ensure that they are logical, relevant, and accurately derived from the original data and prompt.
        3. Identify any discrepancies, inaccuracies, or areas of improvement in the generated content.
        4. Rewrite the section content to ensure its accuracy, coherence, and alignment with the original data and prompt.

        Diversity of Language and Phrasing:
        1. Pay special attention to the section language and phrasing to reduce repetitive structures.  
        2. Ensure language remains engaging by varying phrasing and sentence structure while keeping consistent with the template's tone and format.  
        3. If similar ideas are repeated across different points rewrite to emphasize subtle distinctions in market impact, signaling, or broader implications.  
        4. Focus on delivering key insights in distinct, impactful ways to maintain the reader’s interest without deviating from the provided data.  
        
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
        4. Ensure data is formatted consistently for the relevant data type percentages, currency, decimals, including capitalization, formatting, and punctuation.

        Data Formatting:
        1. References to Bitcoin price should be rounded to have no decimals.
        2. Percentages should be rounded to two decimal places and always have a % sign at the end.
        3. All financial data metrics should be rounded to two decimal places.

        Rewritten Content:
        [Write your edited / revised content here]
        """


def extract_text_from_response(response):
    # Get the last message only (the final assistant response)
    latest_message = response.data[0]  # Messages are in reverse order (latest first)

    text_output = []
    for block in latest_message.content:
        if hasattr(block, "text"):
            text_output.append(block.text.value)

    return "\n".join(text_output)


def process_csv_section(section_name, section_data, report_date):
    """
    Processes a CSV-based section by creating threads for two stages:
    - Stage 1: Generate the initial draft based on instructions and template.
    - Stage 2: Refine the draft using the review prompt within the same thread.
    """
    section_config = PROMPT_LIBRARY.get(section_name)
    if not section_config:
        print(f"Section {section_name} not found in config.")
        return None

    # Create a new thread for the section
    thread = client.beta.threads.create()

    # Stage 1: Generate Initial Draft
    template = section_config["template"].format(
        data=section_data, report_date=report_date
    )
    client.beta.threads.messages.create(
        thread_id=thread.id, role="user", content=template
    )
    run = client.beta.threads.runs.create_and_poll(
        thread_id=thread.id, assistant_id=ASSISTANT_ID
    )
    response = client.beta.threads.messages.list(thread_id=thread.id)
    initial_content = extract_text_from_response(response)

    # Stage 2: Refine the Draft using the Review Prompt
    review_prompt = f"{REVIEW_PROMPT}\n\nGenerated Content:\n{initial_content}"
    client.beta.threads.messages.create(
        thread_id=thread.id, role="user", content=review_prompt
    )
    run = client.beta.threads.runs.create_and_poll(
        thread_id=thread.id, assistant_id=ASSISTANT_ID
    )
    response = client.beta.threads.messages.list(thread_id=thread.id)
    final_content = extract_text_from_response(response)

    return final_content


def process_text_section(content):
    """
    Processes text-based sections in two stages within the same thread:
    - Stage 1: Generate the initial draft.
    - Stage 2: Refine the draft using the review prompt.
    """
    # Create a new thread for the section
    thread = client.beta.threads.create()

    # Stage 1: Generate Initial Draft
    client.beta.threads.messages.create(
        thread_id=thread.id, role="user", content=content
    )
    run = client.beta.threads.runs.create_and_poll(
        thread_id=thread.id, assistant_id=ASSISTANT_ID
    )
    response = client.beta.threads.messages.list(thread_id=thread.id)
    initial_content = extract_text_from_response(response)

    # Stage 2: Refine the Draft using the Review Prompt
    review_prompt = f"{REVIEW_PROMPT}\n\nGenerated Content:\n{initial_content}"
    client.beta.threads.messages.create(
        thread_id=thread.id, role="user", content=review_prompt
    )
    run = client.beta.threads.runs.create_and_poll(
        thread_id=thread.id, assistant_id=ASSISTANT_ID
    )
    response = client.beta.threads.messages.list(thread_id=thread.id)
    final_content = extract_text_from_response(response)

    return final_content


def process_vision_section(uploaded_file, vision_prompt):
    """
    Processes vision (image-based) sections in two stages within the same thread:
    - Stage 1: Generate the initial draft based on the uploaded image and vision-specific instructions.
    - Stage 2: Refine the draft using the review prompt.
    """
    try:
        # Upload the image to OpenAI
        file_bytes = io.BytesIO(uploaded_file.read())
        file_bytes.name = uploaded_file.name
        image_file = client.files.create(file=file_bytes, purpose="vision")

        # Create a new thread for the section
        thread = client.beta.threads.create()

        # Stage 1: Generate Initial Draft
        client.beta.threads.messages.create(
            thread_id=thread.id,
            role="user",
            content=[
                {"type": "text", "text": vision_prompt},
                {"type": "image_file", "image_file": {"file_id": image_file.id}},
            ],
        )
        client.beta.threads.runs.create_and_poll(
            thread_id=thread.id, assistant_id=ASSISTANT_ID
        )
        response = client.beta.threads.messages.list(thread_id=thread.id)
        initial_content = extract_text_from_response(response)

        # Stage 2: Refine the Draft using the Review Prompt
        review_prompt = f"{REVIEW_PROMPT}\n\nGenerated Content:\n{initial_content}"
        client.beta.threads.messages.create(
            thread_id=thread.id, role="user", content=review_prompt
        )
        client.beta.threads.runs.create_and_poll(
            thread_id=thread.id, assistant_id=ASSISTANT_ID
        )
        response = client.beta.threads.messages.list(thread_id=thread.id)

        # Return the final refined output
        return extract_text_from_response(response)

    except Exception as e:
        print(f"Error processing vision section: {e}")
        return None


def process_static_section(conclusion_template, section_outputs):
    """
    Processes static sections in two stages within the same thread:
    - Stage 1: Generate the initial draft by filling the placeholders in the template.
    - Stage 2: Refine the draft using the review prompt.
    """
    # Create a new thread for the section
    thread = client.beta.threads.create()

    # Stage 1: Generate Initial Draft
    formatted_text = conclusion_template.format(
        weekly_bitcoin_recap_summary=section_outputs.get(
            "weekly_bitcoin_recap_summary", "N/A"
        ),
        news_impact=section_outputs.get("news_section", "N/A"),
        historical_performance=section_outputs.get("historical_performance", "N/A"),
        heat_map=section_outputs.get("heat_map", "N/A"),
        mtd_return_comparison=section_outputs.get("mtd_return_comparison", "N/A"),
        ytd_return_comparison=section_outputs.get("ytd_return_comparison", "N/A"),
        weekly_btc_usd=section_outputs.get("weekly_btc_usd", "N/A"),
        relative_valuation_analysis=section_outputs.get("relative_valuation", "N/A"),
    )
    client.beta.threads.messages.create(
        thread_id=thread.id, role="user", content=formatted_text
    )
    run = client.beta.threads.runs.create_and_poll(
        thread_id=thread.id, assistant_id=ASSISTANT_ID
    )
    response = client.beta.threads.messages.list(thread_id=thread.id)
    initial_content = extract_text_from_response(response)

    # Stage 2: Refine the Draft using the Review Prompt
    review_prompt = f"{REVIEW_PROMPT}\n\nGenerated Content:\n{initial_content}"
    client.beta.threads.messages.create(
        thread_id=thread.id, role="user", content=review_prompt
    )
    run = client.beta.threads.runs.create_and_poll(
        thread_id=thread.id, assistant_id=ASSISTANT_ID
    )
    response = client.beta.threads.messages.list(thread_id=thread.id)

    return extract_text_from_response(response)


def generate_full_report(news_stories, report_date, uploaded_image=None):
    """
    Iterates through each section defined in the PROMPT_LIBRARY and processes
    CSV, text, and vision-based sections in two stages (initial + review).
    Generates the full report by compiling all section responses into a final document.
    """
    report_sections = {}

    for section, info in PROMPT_LIBRARY.items():
        processing_type = info.get("processing_type")
        section_url = urls.get(section)

        try:
            # Handle CSV-based sections
            if processing_type == "csv" and section_url:
                data_df = pd.read_csv(section_url)
                data_content = data_df.to_string(index=False)
                # Process the CSV section directly
                report_sections[section] = process_csv_section(
                    section_name=section,
                    section_data=data_content,
                    report_date=report_date,
                )

            # Handle text-based sections
            elif processing_type == "text":
                formatted_text = info["template"].format(
                    data=news_stories or "No news available."
                )
                # Process the text section directly
                report_sections[section] = process_text_section(formatted_text)

            # Handle image-based vision sections
            elif processing_type == "vision" and uploaded_image:
                # Process the vision section directly
                report_sections[section] = process_vision_section(
                    uploaded_image, info["instruction"]
                )

        except Exception as e:
            print(f"Error processing section {section}: {e}")

    # Process static conclusion section
    if "conclusion_section" in PROMPT_LIBRARY:
        section_info = PROMPT_LIBRARY["conclusion_section"]
        report_sections["conclusion_section"] = process_static_section(
            conclusion_template=section_info["template"],
            section_outputs=report_sections,
        )

    # Combine all sections into a full report
    full_report = "\n\n".join(report_sections.values())

    # Save the report to a text file
    with open("Weekly_Bitcoin_Report.txt", "w") as file:
        file.write(full_report)

    print("Report Generated Successfully!")
    return full_report

