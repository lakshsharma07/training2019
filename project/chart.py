# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 23:51:35 2019

@author: Lakshay
"""
import pandas as pd
from plotly.offline import plot
from plotly.graph_objs import Scatter
import plotly.plotly as py
import plotly.graph_objs as go
from sklearn.ensemble import ExtraTreesClassifier



def fig():
    data=pd.read_csv("train.csv")
    features=data.iloc[:,1:]
    labels=data.iloc[:,0:1]
    model = ExtraTreesClassifier()
    model.fit(features,labels)
    print(model.feature_importances_) #use inbuilt class feature_importances of tree based classifiers
    #plot graph of feature importances for better visualization
    feat_importances = pd.Series(model.feature_importances_, index=features.columns)
    feat_importances=feat_importances.nlargest(10)
    data= [go.Bar(x=list(feat_importances.values),y=list(feat_importances.index),orientation = 'h')]
    x=plot(data, filename='horizontal-bar',output_type='div')
    
    return x
    
    
"""    
    trace1 = go.Bar(
    x=['giraffes', 'orangutans', 'monkeys'],
    y=[20, 14, 23],
    name='SF Zoo'
    )
    trace2 = go.Bar(
    x=['giraffes', 'orangutans', 'monkeys'],
    y=[12, 18, 29],
    name='LA Zoo'
    )
    
    data = [trace1, trace2]
    layout = go.Layout(barmode='group')
    
    fig = go.Figure(data=data, layout=layout)
    x=plot(fig, filename='grouped-bar',output_type='div')
    
    
    my_plot_div = py.iplot([Scatter(x=[1, 2, 3], y=[3, 1, 6])], output_type='div')
    
    dict1={}
    dict1['x']="123"
    y=list(dict1.values())
"""