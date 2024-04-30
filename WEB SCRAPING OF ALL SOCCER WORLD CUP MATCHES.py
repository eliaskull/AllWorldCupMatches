#!/usr/bin/env python
# coding: utf-8

# # EXTRAYENDO TABLAS DE MUNDIAL QATAR 2022 USANDO READ_HTML ,BUCLES,ZIP,ALFABETO,DICCIONARIOS

# In[ ]:


#importando pandas y ascii_uppercase
import pandas as pd
from string import ascii_uppercase as alfabeto


# In[3]:


#extrayendo pagina web de mundial 2022
todas_tablas=pd.read_html('https://es.wikipedia.org/wiki/Copa_Mundial_de_F%C3%BAtbol_de_2022')


# In[6]:


#visualizando tabla
todas_tablas[15]


# In[12]:


#visualizando alfabeto en mayusculas
alfabeto


# In[4]:


#creando diccionario dict_tablas
dict_tablas={}
#bucle for y comando zip para unir tablas con la letra correspondiente a cada grupo
for letra,i in zip(alfabeto,range (8,64,7)) :
    df=todas_tablas[i]
    dict_tablas[f'Grupo {letra}']=df


# In[18]:


dict_tablas.keys()


# In[23]:


dict_tablas['Grupo H']


# # EXTRAYENDO TODOS LOS MUNDIALES USANDO BEAUTIFULSOUP

# In[5]:


#importando BeautifulSoup y requests
from bs4 import BeautifulSoup
import requests


# In[9]:


#creacion de lista de todos los mundiales jugados
years=[1930,1934,1938,1950,1954,1958,1962,1966,1970,1974,1978,1982,1986,1990,1994,1998,2002,2006,2010,2014,2018]


# In[11]:


def get_matches(year):
    web=f'https://en.wikipedia.org/wiki/{year}_FIFA_World_Cup' # cadena f permite tener variables dentro de cadena de texto  
    response=requests.get(web) #función requests permite comunicarse con la página web
    content=response.text #respuesta en formato texto
    soup=BeautifulSoup(content,'lxml') #uso de parser lxml para poder fraccionar la información
    matches=soup.find_all('div',class_='footballbox')#tags que permiten identificar los partidos jugados
    #creación de listas para crear un dataframe
    home=[]
    score=[]
    away=[]
    #bucle for para extraer los partidos y resultados de la página
    for match in matches:
        home.append(match.find('th',class_='fhome').get_text())   #en cada iteración la data se va almacenar en una lista(append)
        score.append(match.find('th',class_='fscore').get_text())
        away.append(match.find('th',class_='faway').get_text())

        dict_football={'home':home,'score':score,'away':away}
    df_football=pd.DataFrame(dict_football)
    df_football['year']=year
    return df_football

#historical data
fifa=[get_matches(year) for year in years]
df_fifa=pd.concat(fifa, ignore_index=True)
df_fifa.to_csv('fifa_worldcup_historical_data.csv', index=False)







# In[ ]:





# In[10]:





# In[16]:





# In[21]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




