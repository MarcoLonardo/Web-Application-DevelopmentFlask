[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-f059dc9a6f8d3a56e377f745f24479a46679e63a5d9fe6f495e02850cd0d8118.svg)](https://classroom.github.com/online_ide?assignment_repo_id=6729803&assignment_repo_type=AssignmentRepo)
# COMP0034 Coursework 1 template repository

Repository Link: https://github.com/ucl-comp0035/comp0034-cw1-i-MarcoLonardo.git 

### Set-up instructions

No particular set-up instructions
All the requirements should be installed from requirements.txt.

## Explanation and evaluation of the design of the visualizations

This web application showcases the "Ease of Doing Business" across Europe and it has been developed in response to the European Commission's future investment plans. In their fight to reduce economic inequalities across Europe, a clear awareness of the ease of doing business across Europe could help the EU Commission develop more impactful and targeted investment initiatives. Thus, the main aim of this web application is to provide the EU Commission Leadership team with strategic and actionable insights regarding the current "Ease of Doing Business" Performance across Europe. This performance is measured focusing on the following four indicators from the last 5 years (2016 - 2020):

1. Getting Credit
2. Resolving Insolvency
3. Starting a business
4. Trading across borders


An additional indicator, "Overall Score" has been introduced to describe the average performance of each country throughout this timeframe. It is assumed that these 5 indicators best address the EU Team's interests and requirements identified in COMP0035. Therefore, reducing the scope to these 5 indicators has been a key factor to ensure that the visualizations are easy to interpret, insightful and relevant to the target audience.
The web application is divided into three groups of visualization, each focused on addressing a specific question (identified in COMP0035). The required data used to answer each of the questions is from the Doing Business Database published by the World Bank https://databank.worldbank.org/source/doing-business. Nevertheless, each of the visualizations has been designed and coded in relation to the specific question. For this reason, there are three different versions of the prepared dataset, each one with a specific data structured best addressing the three questions. The three questions that this web app aims to answer are:
Which countries have the lowest/highest Overall Score for every year and how does this compare with the European Average?
Which challenges have the European countries been facing from 2016 to 2020?

Across the four indicators, has the performance of each country been increasing or decreasing from 2016 to 2020?
The target audience of the web application is the EU Commission Leadership Team: a team of experienced leaders specialising in a particular sector (such as legal, environmental, economic). An example of the target audience can be shown with the following persona: Robert Rossi, the Legislative Lead at the EU Commission.
[Target.Audience.Persona.-.Robert.Rossi (2).pdf](https://github.com/ucl-comp0035/comp0034-cw1-i-MarcoLonardo/files/8079369/Target.Audience.Persona.-.Robert.Rossi.2.pdf)


As described in COMP0035 and considering the personas, we can expect the audience to be busy individuals accustomed to renowned newspapers such as The Economist and the Financial Times. Moreover, it is also to consider that their familiarity with technology is unlikely to be high. Therefore, the visualizations and the web app has been designed aiming for clarity, conciseness and intuitive filtering features.


### Visualization 1 - Choropleth Geographic Map
The target audience of this visualization is the European Commission Leadership Team and it aims to provide an intuitive understanding of countries' individual performances. Indeed, this visualization aims to answer the following question: "Which countries have the lowest/highest Overall Score for every year and how does this compare with the European Average?".

When answering this question, it was important to consider the trade-off in visualization using the visualization wheel https://ryanwingate.com/visualization/guidelines/visualization-wheel/ . We can expect The EU Leadership Team's preferences to be far away from engineers and scientists but closer to the ones of journalists. Therefore, visualization 1 will prioritise the following three principles from  Cairo's visualization wheel: decoration, lightness and figuration. Prioritising these aspects also allowed us to ensure that data was accessible and shallow rather than too deep and complex. https://ryanwingate.com/visualization/guidelines/visualization-wheel/. This is an important aspect because deep and complex data can be overwhelming for our target audience and clarity and easy interpretation have been identified as the most convenient communication styles for our personas. To address figuration, the choropleth has been identified as one of the most suitable charts for this target audience because it provides a pragmatic and intuitive physical representation of Europe's current situation. This type of chart would also address the audience's needs for conciseness. Indeed, this type of chart does not require particular attention and the differences can be spotted quickly https://maps-for-excel.com/blog/choropleth-map-in-the-analysis-on-the-map/#:~:text=The%20advantages%20of%20a%20choropleth,picture%20in%20a%20comprehensible%20way. Other geographical maps could also have been helpful in this scenario (i.e. tilemaps). Nevertheless, they require longitudinal and latitudinal coordinates in our data, whereas outline maps such as choropleth c sean integrate seamlessly with the country codes of our dataset https://plotly.com/python/plotly-express/#highlevel-features. Another important characteristic for visualization 1 was lightness, therefore it was a key priority to ensure that only the most important information is displayed. For this reason, the regional scope of the choropleth has been reduced to Europe. A statistics card has been added to improve clarity and help the team benchmark performance with the European average. Finally, a continuous and diverging colour scale (BrBG) has been applied for a more intuitive narrative regarding positive and negative performance. To improve the decoration aspect, the colour scale range has also been set as 75-85. This was an important aspect to avoid misleading visuals https://faculty.ucmerced.edu/jvevea/classes/Spark/readings/Cairo2015_Chapter_GraphicsLiesMisleadingVisuals.pdf because keeping a 0-100 range would have indicated a positive performance overall in Europe.

The visualizations created meets very well design choices made because it provides the audience with an immediate understanding of countries' performance while addressing the audience's communication preferences and technological skills. An additional strength is that not only the question is clearly answered, but a more comprehensive picture of the performance is described with the statistics cards representing the average EU performance by indicators. This, however, represents also a weakness of this visualization. Choosing to add the average of every indicator beside the "Overall Score" on the statistic card could offer additional insights. However, it does not add much value because it cannot be compared with the individual country performance for that indicator. This is because, when hovering over the countries on the map, no scores are displayed for a specific indicator (i.e. getting credit). Thus, this visualization could be improved by adding the individual country score for each indicator to the choropleth map. This would imply that the data structure needs to be changed to ensure that we have both the individual score and overall scores as columns.

### Visualization 2 - Indicator Scatter Chart
Visualization 2 is intended as a follow-up to the previous question. Having understood what the best and worst-performing countries are, visualizations 2 now aims to help the EU Team understand countries' challenges by plotting their scores for each of the indicators. Thus, visualization 2 aims to address the following question: "Which challenges have the European countries been facing from 2016 to 2020?". While the data required to answer this question is unchanged from question 1, it was necessary to transform the dataset, storing the indicator Name as observations rather than columns.

When answering this question, the number of countries, years and indicators posed a challenge on design clarity. Indeed, plotting all these countries could result in redundant chartjunk leading to an excessive data-ink ratio https://www.darkhorseanalytics.com/blog/data-looks-better-naked. For this reason, it was necessary to keep the graphs intuitive and provide as much flexibility as possible for filtering out unwanted data. The scatter chart provided a good solution to this problem because it allowed us to differentiate in three quadrants the 4 different indicators. This can be very insightful for the EU Team because, besides comparing countries, they can compare performance across indicators and understand where on average all European countries are struggling. Moreover, the scatter plot offers the opportunity to include animations. This is a great way to make the visual more figurative and intuitive as it is a way to filter years and reduce noise. Filtering is an important aspect when answering a question requiring so many data points because the team is empowered to make the analysis as relevant as possible. The dropdown panel is an additional example of this where the EU Team can choose to focus on very few countries. To improve ease of use and address the EU Team's low familiarity with technology, the dropdown menu has been set as searchable so that the team can conveniently type to remove and add countries.

This visualization addresses the question and the target audience very well because, with one graph, it can show the countries with the worst performance for each indicator. While there are many data points, the filtering panels provide an opportunity to remove noise and analyse data flexibly. This flexibility is a strength of this visualization because it can convey light layouts despite dealing with different data and variables. One of the weaknesses, however, is that this type of chart could be even more insightful if we had more variables. At the moment, this dataset is a limitation because the only value we can plot along the axis is the score. In this scenario, the overall score of each country (across the fours indicators) has been plotted against the score of one of the four indicators. This sufficiently addresses the questions, nevertheless, this type of chart offers space for more variables especially if we consider that the size of the bubbles can be used as an additional axis. Thus, one way to improve this chart would be to identify and include in the data additional measures of every indicator. For example, for the resolving insolvency indicator, there are also measures for resolving insolvency time and quality https://databank.worldbank.org/source/doing-business. The time and quality measures of the indicator could be plotted along the y and x-axis, whereas the resolving insolvency score can be plotted using the size of the bubbles. This would improve the depth of the answer because not only, the EU Team can understand the high-level challenges, but they can also pinpoint the reasons why countries have a low performance for each indicator.

### Visualization 3 - Icicle and Interactive Bar Chart
Visualization 3 focuses on showcasing how indicators have evolved over the years. Similarly to visualization 2, it requires the same data from the World Bank, but in a slightly different format. For this reason, a third version of the prepared dataset has been developed with the Overall Score column considered as an observation rather than a variable. This visualization aims to help the EU Team address the following question: " Across the four indicators, has the performance of each country been increasing or decreasing from 2016 to 2020?".

To answer this question, the line chart has been identified as one of the most suitable graphs because it can clearly show how different indicators scores change over the years. One of the challenges, however, is that plotting the four indicators for all the countries can make the line charts very difficult to interpret. As a result, for this visualization, a combination of charts have been used: an icicle and a line chart. The icicle, ranking countries based on 5-Year Mean Performance, can be used to filter individually for every country. Indeed, as we hover over each country, the line chart will update accordingly showcasing the 4 indicators scores for every country from 2016 to 2020. Even for this visualization, this interactivity allows the target audience to achieve figuration and lightness. The visual can be defined as figurative because the users can interact with the charts in a more user-friendly and concrete way. Moreover, with this interactivity, the visualizations can become lighter, reducing the amount of data users works with. To keep the colours and style consistent with the web page, the same scale colour has been applied to the icicle. This allows the users to identify the rank of the countries. Finally, it was essential to add a title to specify the country being plotted and include relevant instructions.  As ambiguity is reduced, the visualization results are more concise and professional. This allows the visualization to better meet the target audience's preferences.

The combination of these charts meets adequately the design choices made because, with immediate filtering and intuitive line charts, the users can understand how indicators changed over the years. This ensures that data redundancy and ambiguity is prevented with a light layout and an intuitive filtering system. There are, however, some areas of improvement. Firstly, the icicle is static and provides only an insight on 5-Year mean performance. One potential improvement would be to add a dropdown selection panel to display the 5-Year performance of individual indicators (i.e. getting credit). In other words, rather than statically looking at the 5-Year Mean Score of Overall Performance (across the four indicators), it might be worth adding the 5-Year mean performance mean across the individual indicators. Secondly, the line chart does not always offer significant insights for countries because the timeframe spans only 5 years. Thus, it might be worth including all the available data from 2014. This improvement, however, could not be very significant because the time frame remains narrow and there is a considerable amount of missing data.

## References
