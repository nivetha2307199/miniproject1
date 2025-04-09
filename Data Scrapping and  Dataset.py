#!/usr/bin/env python
# coding: utf-8

# In[13]:


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import pandas as pd
import time
def func(m,d,r,v):
    max_len = max(len(m), len(d), len(r), len(v))
    m.extend([None] * (max_len - len(m)))
    d.extend([None] * (max_len - len(d)))
    r.extend([None] * (max_len - len(r)))
    v.extend([None] * (max_len - len(v)))
    try:
        dataset = pd.DataFrame({'Title': m,'Duration': d,'Rating': r,'Voting': v})
        csv= dataset.to_csv()
        dataset.to_csv(r'C:\Users\NIVI\OneDrive\Documents\AIML Course\documentary.csv',index=False)
        print("Successfully created the dataset and converted into CSV file")
    except ValueError:
        print("Value Error")
driver=webdriver.Chrome()
driver.get('https://www.imdb.com/search/title/?title_type=feature&release_date=2024-01-01,2024-12-31&genres=documentary')
driver.maximize_window()
driver.execute_script("""var ads = document.querySelectorAll('iframe, .adsbygoogle, .ad-banner');
        ads.forEach(ad => ad.style.display = 'none');""")
page=1
scrolling=True
while scrolling:
    old_page=driver.page_source
    body=driver.find_element(By.TAG_NAME,"body" )
    body.send_keys(Keys.PAGE_DOWN)
    new_page=driver.page_source
    action= ActionChains(driver)
    time.sleep(2)
    action.move_to_element(driver.find_element(By.XPATH, "//div[@class='sc-619d2eab-0 dxnOGI']/div/span/button")).click()
    action.perform()
    if new_page==old_page and page>=2:
        scrolling=False 
    page+=1
movie = driver.find_elements(By.XPATH,'//*[@id="__next"]/main/div[2]/div[3]/section/section/div/section/section/div[2]/div/section/div[2]/div[2]/ul/li/div/div/div/div[1]/div[2]/div[1]/a/h3')
duration = driver.find_elements(By.XPATH, '//*[@id="__next"]/main/div[2]/div[3]/section/section/div/section/section/div[2]/div/section/div[2]/div[2]/ul/li/div/div/div/div[1]/div[2]/div[2]/span[2]')
rating = driver.find_elements(By.XPATH, '//*[@id="__next"]/main/div[2]/div[3]/section/section/div/section/section/div[2]/div/section/div[2]/div[2]/ul/li/div/div/div/div[1]/div[2]/span/div/span/span[1]')
voting = driver.find_elements(By.XPATH, '//*[@id="__next"]/main/div[2]/div[3]/section/section/div/section/section/div[2]/div/section/div[2]/div[2]/ul/li/div/div/div/div[1]/div[2]/span/div/span/span[2]')
m=[]
d=[]
r=[]
v=[]
for i in movie:
    s=i.text
    st=""
    for j in range(len(s)):
        if(((s[j]>='0'and s[j]<='9') and j>=0 and j<=2)or s[j]=='.' ):
            continue
        elif((s[j]>='0'and s[j]<='9')):
            st=st+s[j]
        else:
            st=st+s[j]
    m.append(st)
for j in duration:
    d.append(j.text)
val=1
for k in rating:
    rat=k.text
    r.append(rat)
    val+=1
    
val=1
for o in voting:
    cc=-1
    s=o.text
    s=s[2:len(s)-1]
    s1=""
    decimal=0.0
    for i in range(len(s)):
        if(s[i]=='K' or s[i]=='k'):
            decimal=float(s1)
            cc=1
            decimal=decimal*1000
        else:
            s1=s1+s[i]
    if(cc==1):
        v.append(decimal)
    else:
        decimal=float(s1)*1000
        v.append(decimal)
    val+=1  
func(m,d,r,v)


# In[21]:


import pandas as pd
import os
csv_files=[r'C:\Users\NIVI\OneDrive\Documents\AIML Course\action.csv',
           r'C:\Users\NIVI\OneDrive\Documents\AIML Course\comedy.csv',
          r'C:\Users\NIVI\OneDrive\Documents\AIML Course\drama.csv',
          r'C:\Users\NIVI\OneDrive\Documents\AIML Course\romance.csv',
          r'C:\Users\NIVI\OneDrive\Documents\AIML Course\documentary.csv']
dataset = []
for file in csv_files:
    genre_data = pd.read_csv(file)
    genre_name = os.path.basename(file).split('_')[0].capitalize()
    genre_data['Genre'] = genre_name.replace(".csv", "")
    dataset.append(genre_data)
combined_dataset = pd.concat(dataset, ignore_index=False)
combined_dataset = combined_dataset[['Title', 'Duration', 'Rating', 'Voting', 'Genre']]

combined_dataset.to_csv(r'C:\Users\NIVI\OneDrive\Documents\AIML Course\finaldataset.csv')
print("CSV files combined successfully!")


# In[ ]:




