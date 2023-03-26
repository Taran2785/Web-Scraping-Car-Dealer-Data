#!/usr/bin/env python
# coding: utf-8

# # Web Scraping Car delaer website

# Imports

# In[13]:


from bs4 import BeautifulSoup
import requests
import pandas as pd 


# 
# HTTP Request
# 

# store website in variable
# 

# In[37]:


website = "https://www.cars.com/shopping/results/?stock_type=all&makes%5B%5D=tesla&models%5B%5D=&list_price_max=&maximum_distance=all&zip="


# Get Request

# In[38]:


response = requests.get(website)


# Status Code

# In[39]:


response.status_code


# Soup Object

# In[40]:


soup = BeautifulSoup(response.content, 'html.parser')


# Results

# In[41]:


results = soup.find_all('div', {'class' : 'vehicle-card'})


# In[42]:


len(results)


# Target necessary data

# In[43]:


# Name
# Dealer Name
# Rating
# Rating Count
# Price


# Name

# In[44]:


results[0].find('h2').get_text()


# Dealer Name
# 

# In[53]:


results[0].find('div', {'class':'dealer-name'}).get_text().strip



# Rating

# In[47]:


results[0].find('span', {'class':'sds-rating__count'}).get_text()


# Review Count

# In[49]:


results[0].find('span', {'class':'sds-rating__link'}).get_text()


# Price
# 

# In[50]:


results[0].find('span', {'class':'primary-price'}).get_text()


# # Put everything together inside a For-Loop

# In[55]:


name = []
dealer_name = []
rating = []
review_count = []
price = []

for result in results:
    
    # name
    try:
        name.append(result.find('h2').get_text()) 
    except:
        name.append('n/a')
    
    # dealer_name
    try:
        dealer_name.append(result.find('div', {'class':'dealer-name'}).get_text().strip())
    except:
        dealer_name.append('n/a')
        
    # rating
    try:
        rating.append(result.find('span', {'class':'sds-rating__count'}).get_text())
    except:
        rating.append('n/a')
    
    # review_count
    try:
        review_count.append(result.find('span', {'class':'sds-rating__link'}).get_text())
    except:
        review_count.append('n/a')
    
    #price 
    try:
        price.append(result.find('span', {'class':'primary-price'}).get_text())
    except:
        price.append('n/a')


# # Create Pandas Dataframe

# In[56]:


# dictionary
car_dealer = pd.DataFrame({'Name': name, 'Dealer Name':dealer_name,
                                'Rating': rating, 'Review Count': review_count, 'Price': price})


# In[57]:


car_dealer


# Data Cleaning

# In[58]:


car_dealer['Review Count'] = car_dealer['Review Count'].apply(lambda x: x.strip('reviews)').strip('('))


# In[59]:


car_dealer


# Output in Excel

# In[60]:


car_dealer.to_excel('car_dealer_single_page.xlsx', index=False)


# Pagination

# In[61]:


name = []
mileage = []
dealer_name = []
rating = []
review_count = []
price = []

for i in range (1,11):
    
    # website in variable
    website = 'https://www.cars.com/shopping/results/?page='+ str(i) +'&page_size=20&dealer_id=&list_price_max=&list_price_min=&makes[]=mercedes_benz&maximum_distance=20&mileage_max=&sort=best_match_desc&stock_type=cpo&year_max=&year_min=&zip=' 
    
    # request to website
    response = requests.get(website)
    
    # soup object
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # results
    results = soup.find_all('div', {'class' : 'vehicle-card'})
    
    # loop through results
    for result in results:
    
        # name
        try:
            name.append(result.find('h2').get_text()) 
        except:
            name.append('n/a')

        # mileage
        try:
            mileage.append(result.find('div', {'class':'mileage'}).get_text())
        except:
            mileage.append('n/a')

        # dealer_name
        try:
            dealer_name.append(result.find('div', {'class':'dealer-name'}).get_text().strip())
        except:
            dealer_name.append('n/a')

        # rating
        try:
            rating.append(result.find('span', {'class':'sds-rating__count'}).get_text())
        except:
            rating.append('n/a')

        # review_count
        try:
            review_count.append(result.find('span', {'class':'sds-rating__link'}).get_text())
        except:
            review_count.append('n/a')

        #price 
        try:
            price.append(result.find('span', {'class':'primary-price'}).get_text())
        except:
            price.append('n/a')


# In[62]:


# dictionary
car_dealer = pd.DataFrame({'Name': name, 'Mileage':mileage, 'Dealer Name':dealer_name,
                                'Rating': rating, 'Review Count': review_count, 'Price': price})


# In[63]:


car_dealer


# In[64]:


car_dealer['Review Count'] = car_dealer['Review Count'].apply(lambda x: x.strip('reviews)').strip('('))


# In[65]:


car_dealer


# In[66]:


car_dealer.to_excel('car_dealer_single_page.xlsx', index=False)


# In[ ]:




