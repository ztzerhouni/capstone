import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.pipeline import Pipeline

from sklearn.neural_network import MLPClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis
from sklearn.naive_bayes import MultinomialNB

from sklearn.metrics import confusion_matrix, plot_confusion_matrix

from sklearn.feature_extraction.text import CountVectorizer

def modeling_parameters(model):
    parameters = model.get_params()
    
    param_dict = { 'model' + '__' + key : [value]\
              for key,value in zip(parameters.keys(),parameters.values())
                 }
    return param_dict

def benchmark_model(gridsearch,X_train,X_test,y_train,y_test):
    
    print(gs.estimator)
    print()
    print(f'Baseline Score:\n{y_test.value_counts(normalize=True)}')
    print()
    print(f'GridSearch Best Score: {gridsearch.best_score_}')
    print()
    print(f'GridSearch Best Parameters:')
    print(gridsearch.best_params_)
    print()
    print(f'GridSearch Training Score: {gridsearch.score(X_train, y_train)}')
    print()
    print(f'GridSearch Testing Score: {gridsearch.score(X_test, y_test)}')

model_list= [MLPClassifier(),KNeighborsClassifier(),DecisionTreeClassifier(),RandomForestClassifier(),AdaBoostClassifier(),MultinomialNB()]    

df = pd.read_csv('data/modeling_aapl.csv')
df.set_index('Unnamed: 0',inplace=True)
df.index.rename('adjusted_date',inplace=True)
df['target'] = [0 if i <= 0 else 1 for i in df['Close']] 
X = df['text']
y = df['target']

X_train, X_test, y_train, y_test = train_test_split(X,y,stratify=y,random_state=1)

for test_model in model_list:
    
    model = test_model

    pipe = Pipeline([
        ('cvec', CountVectorizer()),
        ('model', model)
    ])

    pipe_params = {
        'cvec__max_features': [2_000, 3_000, 4_000, 5_000],
        'cvec__min_df': [2, 3],
        'cvec__max_df': [.9, .95],
        'cvec__ngram_range': [(1,1), (1,2)],
    }

    gs = GridSearchCV(pipe, # what object are we optimizing?
                      param_grid=pipe_params, # what parameters values are we searching?
                      cv=5,
                     n_jobs=2,
                     verbose=0) # 5-fold cross-validation.
    gs.fit(X_train, y_train);
    benchmark_model(gs,X_train,X_test,y_train,y_test)