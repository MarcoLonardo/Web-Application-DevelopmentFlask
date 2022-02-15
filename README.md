[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-f059dc9a6f8d3a56e377f745f24479a46679e63a5d9fe6f495e02850cd0d8118.svg)](https://classroom.github.com/online_ide?assignment_repo_id=6729803&assignment_repo_type=AssignmentRepo)
# COMP0034 Coursework 1 template repository

Repository Link: https://github.com/ucl-comp0035/comp0034-cw1-i-MarcoLonardo.git 

### Set-up instructions

No particular set-up instructions
All the requirements should be installed from requirements.txt.

## Explanation and evaluation of the design of the visualizations

This web application showcases the "Ease of Doing Business" across Europe and it has been developed in response to the European Commission's future investment plans. In their fight to reduce economic inequalities across Europe, a clear awareness over the ease of doing business across Europe could help the EU Commission develop more impactful and targeted investment initiatives. Thus, the main aim of this web application is to provide the EU Commission Leadership team with strategic and actionable insights regarding the current "Ease of Doing Busineess" Performance across Europe. This performance is measured focusing on the following four indicators from the last 5 years (2016 - 2020):

1. Getting Credit 
2. Resolving Insolvency
3. Starting a business
4. Trading across borders 

An additional indicator, "Overall Score" has been introduced to describe the average performance of each country throughout this timeframe. It is assumed that these 5 indicators best address the EU Team's interests and requirements. Therefore, reducing the scope to this 5 indicators has been a key factor to ensure that the visualizations are easy to interpret, insightful and relevant to the target audience. 

The web application is divided into three groups of visualization, each focused on addressing a specific question (identified in COMP0035). The required data used to answer each of the questions is from the Doing Business Database published by the World Bank https://databank.worldbank.org/source/doing-business. Nevertheless, each of the visualizations has been designed and coded in relation to the question. Therefore, it was necessary to have different versions of the cleaned and prepared dataset to answer the questions. For this reason, there are three different versions of the prepared dataset, each one with a specific data structured best addressing the three questions. 
The three questions that this web app aims to answer are:

1. Which countries have the lowest/highest Overall Score for every year and how does this compare with the European Average?
2. Which challenges have the European countries been facing from 2016 to 2020?
3. Across the four indicators, has the performance of each country been increasing or decreasing from 2016 to 2020?



The target audience of the web application is the EU Commission Leadership Team: a team of experienced leaders specialised in a particular sector (such as: legal, enviromental, economic). An example of the target aundience can be shown with the following persona: Robert Rossi, the Legislative Lead at the EU Commission. 

[Target Audience Persona - Robert Rossi.pdf](https://github.com/ucl-comp0035/coursework-1-MarcoLonardo/files/7507856/Target.Audience.Persona.-.Robert.Rossi.pdf)

As described in COMP0035 and considering the personas, we can expect the audience to be busy individuals accustomed to renown newspapers such as The Economist and the Financial Times. Moreover, it is also to consider that their familiarity with technology is unlikely to be strong. Therefore, the visualizations and the web app has been designed aiming for clarity, consiveness and intuitive filtering features. 




### Visualization 1 - Choropleth Geographic Map

The target audience of this visualization is the European Commission Leadership Team and it aims to provide an intuitive understanding of countries' individual performances. Indeed, this visualization aims to answer the following question: "Which countries have the lowest/highest Overall Score for every year and how does this compare with the European Average?". 

When answering this question, it was important to consider the trade-off in visualization using the visualization wheel https://ryanwingate.com/visualization/guidelines/visualization-wheel/
![image](https://user-images.githubusercontent.com/64501760/154100878-a3a36c32-78c1-4e3e-9a88-e45523df55b4.png). We can expect The EU Leadership Team's preferences to be far away from engineers and scientists but closer to the ones of journalists. Therefore, visualization 1 will prioritise the following three principles from the Cairo's visualization wheel: decoration, lightness and figuration. Prioritising these aspects also allowed us to ensure that data was accessible and shallow rather than too deep and complex.  https://ryanwingate.com/visualization/guidelines/visualization-wheel/.
This is an important aspect becuase deep and complex data can be overwhelming for our target audience and clarity and easy interpretation have been identified as the most convinient communication styles for our personas.
To address figuration, the chropleth has been identified as one of the most suitable chart for this target audience becuase it provides a pragmatic and intuitive physical representation of Europe's current situation. This type of chart would also adress the audience's needs for conciveness. Indeed, this type of chart does not require particular attention and the differences can be spotted quickly https://maps-for-excel.com/blog/choropleth-map-in-the-analysis-on-the-map/#:~:text=The%20advantages%20of%20a%20choropleth,picture%20in%20a%20comprehensible%20way. There were other geographical maps that would be helful in this scenario (i.e. tile maps). Nevertheless, they would require longitudinal and latutudinal coordinates in our data, whereas outline maps such as choropleth have a seamless integration with the locations variable https://plotly.com/python/plotly-express/#highlevel-features. Another important characteristic for visualization 1 was lightness, therefore it was a key priority to ensure that only the most important information is displayed. For this reason, the regional scope of the chropleth has been reduced to Europe. A statistics card has been added to improve clarity and help the team benchmark performance with the European average. Finally, a continuous and diverging color scale (BrBG) has been applied for a more intuitive narrative regarding positive and negative performance. To improve the decoration aspect, the color scale range have also been set as 75-85. This was an important aspect to avoid misleading visuals https://faculty.ucmerced.edu/jvevea/classes/Spark/readings/Cairo2015_Chapter_GraphicsLiesMisleadingVisuals.pdf becuase keeping a 0-100 range would have indicated a positive performance overall in Europe. 


The visualizations created meets very well design choices made becuase it provides the audience with an immediate understanding how countries' performance while addressing the audience's communication preferences and technological skills. An additional strenght is that not only the question is clearly answered, but a more comprehensive picture of the performance is described with the statistics cards representing the average EU performance by indicators. This, however, represents also a weakness of this visualization. Choosing to add the average of every indicator besides the "Overall Score" on the statistic card could offer additional insights. However, it does not add much value because it cannot be compared with the individual country performance for that indicator. This is becuase, when hovering over the countries on the map, no scores are displayed for a specific indicator  (i.e. getting credit). Thus, this visualization could be imporved by adding the indivual country score for each indicator to the choropleth map. This would imply that the data is structured in a different format to ensure that we have both the individal score and overall scores as variables.
      
  



### Visualization 2 - Indicator Scatter Chart

Visualization 2 is intended as a follow-up from the previous question. Having understood what the best and worst perofrming countries are, visualizations 2 now aims to help the EU Team understand countries' individual challenges by plotting their scores for each of the indicator. Thus, visualization 2 aims to address the following question:
"Which challenges have the European countries been facing from 2016 to 2020?". While the data required to answer this question is unchanched from question 1, it was necessary to transform the dataset, storing the indicator Name as observartions rather than columns. 

When answering these question, the number of countries, years and indicators posed a challenges on data clarity. Indeed, plotting all these countries could result in redundant chartjunk leading to an excessive data-ink ratio https://www.darkhorseanalytics.com/blog/data-looks-better-naked. For this reason, it was necessaey to keep the graphs intuitive and provide as much flexibility as possible for filtering out unwanted data. The scatter chart provided a good solution to this problem becuase it allowed us to differentiate in three quadrants the 4 different indicators. This can be very insightful for the EU Team, becuase besides comparing countries, they can compare performance across indicators and understand where on average all European countries are struggling. Moreover, the scatter plot offers the opportunity to include animation. This is a great way to make the visual more figurative and therefore more intuitive to the EU Team, but it can also be an additional way to filter years and reduce noice. Filtering is an importnan taspect when answeing a questions requiring so many datapoints becuase the team is empowered to make the analysis as releventant as possible. The dropdown panel is an additional example of this where the EU Team can focus on very few countries. To improve ease of use and address the Eu Team's low familiarity with technology, the dropdown mesu has been set as searchable so that the team can conviniently type to remove and add countries. 

The strenght is flexibility and customization with direct comparison of performance across indicators. 




### Visualization 3 - Icicle and Interactive Bar Chart


## References
