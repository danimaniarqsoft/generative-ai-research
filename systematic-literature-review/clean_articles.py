import pycountry
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os


BASE_DIR = os.getcwd() + '/systematic-literature-review/'

ARTICLES_FILE = os.path.join(BASE_DIR, 'data/articles.csv')
CITES_FILE = os.path.join(BASE_DIR, 'data/cites.csv')
ARTICLES_WITH_CITES_FILE = os.path.join(BASE_DIR, 'data/articles_with_cites.csv')


articles = pd.read_csv(ARTICLES_FILE, index_col=False)
articles = articles[["Key","Item Type","Publication Year","Author","Title","Publication Title","DOI","Url","Abstract Note","Date","Publisher","Place","Manual Tags","Automatic Tags","Conference Name"]]

articles = articles.loc[(articles['Key'] != 'YFVDG49E')]
articles = articles.loc[(articles['Key'] != '6H6GPAC3')]
    
articles.to_csv(ARTICLES_FILE, index=False)
cites = pd.read_csv(CITES_FILE, index_col=False)
articles_with_cites = pd.merge(articles, cites, on='Title', how='left', validate="many_to_many")
articles_with_cites.to_csv(ARTICLES_WITH_CITES_FILE, index=False)




