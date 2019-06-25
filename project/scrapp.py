
from plotly.offline import plot
from plotly.graph_objs import Scatter
import plotly.graph_objs as go
from bs4 import BeautifulSoup
import requests
def users(name1,name2):
    temp = requests.get('https://twitter.com/'+name1)
    bs = BeautifulSoup(temp.text,'lxml')
    try:
    #    follow_box = bs.find('li',{'class':'ProfileNav-item ProfileNav-item--followers'})
    #    followers = follow_box.find('a').find('span',{'class':'ProfileNav-value'})
        all_tabs = bs.find_all("li",class_="ProfileNav-item")
        
        feature_dict = {}
        feature_req = ["Followers","Following","Tweets"]
        feature_dict = feature_dict.fromkeys(feature_req,0)
        
        
        for item in all_tabs:
            label = item.find("span",class_="ProfileNav-label")
            value = item.find("span",class_="ProfileNav-value")
            
            if label and value:
                label = str(label.text.strip())
                value = str(value.text.strip())
                if label in feature_req:
                    feature_dict[label] = value
        
        xx=feature_dict
        import re
        images1 = list(bs.find_all('img', {'src':re.compile('.jpg')}))
        url1=images1[0]['src']
        
    except:
        print('Account name not found...')
        
     
    temp = requests.get('https://twitter.com/'+name2)
    bs = BeautifulSoup(temp.text,'lxml')
    try:
    #    follow_box = bs.find('li',{'class':'ProfileNav-item ProfileNav-item--followers'})
    #    followers = follow_box.find('a').find('span',{'class':'ProfileNav-value'})
        all_tabs = bs.find_all("li",class_="ProfileNav-item")
        
        feature_dict1 = {}
        
        feature_dict1 = feature_dict1.fromkeys(feature_req,0)
        
        for item in all_tabs:
            label = item.find("span",class_="ProfileNav-label")
            value = item.find("span",class_="ProfileNav-value")
            
            if label and value:
                label = str(label.text.strip())
                value = str(value.text.strip())
                if label in feature_req:
                    feature_dict1[label] = value
        yy=feature_dict1
        import re
        images2 = list(bs.find_all('img', {'src':re.compile('.jpg')}))
        url2=images2[0]['src']
        
    except:
        print('Account name not found...')
       
    import re
    for key,value in feature_dict.items():
        
        if(re.search(r'[,]',str(value))):
            value=value.replace(",","")
            
             
     
                
        if(re.search(r'M$',str(value))):
            value=float(value.replace("M",""))
            value=int(value*1000000)
        
        elif(re.search(r'K$',str(value))):
            value=float(value.replace("K",""))
            value=int(value*1000)
        feature_dict[key]=int(value)
                
    for key,value in feature_dict1.items():
        if(re.search(r'[,]',str(value))):
            value=value.replace(",","")
                         
        if(re.search(r'M$',str(value))):
            value=float(value.replace("M",""))
            value=int(value*1000000)
        
        if(re.search(r'K$',str(value))):
            value=float(value.replace("K",""))
            value=int(value*1000)
        feature_dict1[key]=int(value)
    
            
        
    
    list1=[feature_dict["Followers"],feature_dict["Following"],feature_dict["Tweets"],feature_dict1["Followers"],feature_dict1["Following"],feature_dict1["Tweets"]]
    
    import pickle
    with open("pick_pickle",'rb') as fp:
        classifier=pickle.load(fp)    
    
    
    with open("pick_pickle1",'rb') as fp1:
        sc=pickle.load(fp1)

        
    import numpy as np
    list2=np.array(list1)
    list2=list2.reshape(1,-1)
    
    list2=sc.transform(list2)
    
    
    x=classifier.predict(list2)
    
    #plotting the bar graph in which we compare the different features of both user
    trace1 = go.Bar(
    x=feature_req,
    y=list(feature_dict.values()),
    name=name1
    )
    trace2 = go.Bar(
    x=feature_req,
    y=list(feature_dict1.values()),
    name=name2
    )

    data = [trace1, trace2]
    layout = go.Layout(barmode='group')

    fig = go.Figure(data=data, layout=layout)
    figs=plot(fig, filename='grouped-bar',output_type='div')



    if x==1:
        return (xx,yy,name1,url1,url2,figs)
    else:
        return (xx,yy,name2,url1,url2,figs)