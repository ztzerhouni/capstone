# Natural Language Processing

- [Problem Statement](#Problem-Statement)
- [Description of Data](#Description-of-Data)
- [Model Performance on Training and Test Data](#Model-Performance-on-Training-and-Test-Data)
- [Primary Findings](#Primary-Findings)
- [Next Steps](#Next-Steps)

## Problem Statement

Making a decision about buying or selling a stock often comes down to the most up to date news on the performance of a company. I have used natural language processing to collect online articles, vectorize the content of those articles, and create a criteria to buy or sell a given stock based on the content of those articles. In order to select the model that will be used a series of different models will be attempted using a grid search with cross validation and the one with the best performance at the initial stage will be selected.

## Description of Data

The data was aquired using the Selenium web driver from [Seeking Alpha](https://seekingalpha.com/). For any given stocker ticker, 100 articles are pulled from the website. Stock values were pulled from [Yahoo Finance](https://finance.yahoo.com/) using the [yfinance API](https://pypi.org/project/yfinance/).

Once the data was pulled into a dataframe it was discovered that advertisetment articles without any useful data were saved as well. As these had no text data in them, these rows were dropped during data cleaning.

The target column was created by taking the difference of the aggregated values of the following week of stock values. If the average percent difference was positive then a value of 1 was assigned to the target. Otherwise a vlaue of 1 was assigned. 

A count vectorizer was used to process the text data. 


# Model Performance on Training and Test Data

The first thing determined to benchmark our model performance was the baseline accuracy. The baseline accuracy of the test set was 0.59

Our data was trained on 5 different models using 2 different vectorizers to process the text of the titles. The Training and Testing Scores of each model are shown below. 

|Model|Training Score|Testing Score|
|---|---|---|
|MLP Classifier|1.0|0.68|
|K Neighbors Classifier|0.67|0.59|
|Decision Tree Classifier|1.0|0.45|
|Random Forest Classifier|1.0|0.59|
|AdaBoost Classifier|1.0|0.54|
|Multinomial Naive Bayes|1.0|0.72|

The following count vectorizer was used:

- [Count Vectorizer](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.CountVectorizer.html)

Multinomial Naive Bayes provided the best performance with an accuracy of 0.72.

The Multi-layer Perceptron Neural Network was second best with an accuracy of 0.68.

Hyper parameter tuning took place, as well as attempts to substitute the Natural Language Processing. These resulted in long grid searches and new implementations, but no marked increase in performance.


## Primary Findings

The best performance was found with [Multinomial Naive Bayes](https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.MultinomialNB.html) with a testing score of 0.72. This shows that with a basic approach to Natural Language Processing we can get a prediction above the baseline,

Attempting to add additional data in the form of the volume of stock traded resulted in a worse score.

Now that we can use an individual article to predict if there will be a growth in the stock the next week we can hedge our bets by aggregating a series of articles and only making a decision to buy or sell a stock if a certain percentage of the articles indicate that the stock will grow or decrease in value.

The results of predicting even with limited data show that a prediction can be made for the next week.

Going forward, in order to make a decision, all the articles in a week can be collected. Then choose a threshold of confidence to buy a stock if the value is anticipated to increase in the next week, or sell a stock if the value is anticipated to decrease. 

For n articles, if there are k successes, our ratio will be k/n.

## Next Steps

The biggest weakness of the model most likely comes from a lack of data. For any given stock only 100 articles would be collected. A new method that could aggregate thousands of articles would help to build a better vocabulary and provide better counts for predictions. The best method for this would be to collect data over a longer period and build a more robust data set for training our model.

Currently, historical stock data did not improve the predictions. Looking for other metrics that could correlate to growth could assist in better predictions.

In the future the following methods can be attempted:

- Use the articles of multiple stocks and finding the common words between these sets.
- Updating the target to look for a certain level of growth. For example, if the percent difference of growth isn’t over 1.5%, then we do not count that article as a success.
- Investigate articles that do not provide the correct prediction and look for trends to update the vocabulary of our model.

There is also the potential to look into the following problems:

- Attempting new time intervals. Are predictions better for shorter intervals? Worse for longer intervals?
- What is the maximum time into the future a collection of articles can predict?
