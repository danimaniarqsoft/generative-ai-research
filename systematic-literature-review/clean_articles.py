import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from IPython.display import display
from matplotlib import style 
import os

#plt.style.use('ggplot') 
plt.style.use('seaborn-v0_8') 

BASE_DIR = os.getcwd() + '/systematic-literature-review/'

ARTICLES_FILE = os.path.join(BASE_DIR, 'data/articles.csv')
CITES_FILE = os.path.join(BASE_DIR, 'data/cites.csv')

articles = pd.read_csv(ARTICLES_FILE)
cites = pd.read_csv(CITES_FILE)
articles = pd.merge(articles, cites, on='Title', how='left', validate="many_to_many")
#articles.plot.bar(x="Title", y="cited", alpha=0.5,log=True)

if 'File Attachments' in articles:
    articles = articles.drop(columns=['File Attachments'])
if 'Date Added' in articles:
    articles = articles.drop(columns=['Date Added'])
if 'Date Modified' in articles:
    articles = articles.drop(columns=['Date Modified'])
if 'Access Date' in articles:
    articles = articles.drop(columns=['Access Date'])
    
    
articles = articles.drop(articles[articles.Key == 'YFVDG49E'].index)
articles = articles.drop(articles[articles.Key == '6H6GPAC3'].index)
articles.to_csv(ARTICLES_FILE)




