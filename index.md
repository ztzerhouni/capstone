# Predicting Stock Performance with Natural Language Processing

- [Problem Statement](#Problem-Statement)
- [Description of Data](#Description-of-Data)
- [Model Performance on Training and Test Data](#Model-Performance-on-Training-and-Test-Data)
- [Primary Findings](#Primary-Findings)
- [Next Steps](#Next-Steps)

## Problem Statement

Making a decision about buying or selling a stock often comes down to the most up to date news on the performance of a company. 
I have used natural language processing to collect online articles, vectorize the content of those articles, 
and create a criteria to buy or sell a given stock based on the content of those articles. 
In order to select the model that will be used a series of different models will be attempted using a grid search with cross validation 
and the one with the best performance at the initial stage will be selected.
