#Importing important libraries.
from bs4 import BeautifulSoup   # BS4 for Scrapping data from site.
import requests                 # Request to get the url
import pandas as pd 
# link contains Reviews only 
url = "https://www.urbancompany.com/reviews"  
s = requests.get(url)                         
soup = BeautifulSoup(s.content)  
com = soup.find("div", class_ = "ReviewCollectionParent__reviewActualPane--1dQI4")
names = []
dates = []
rates = []
comments = []

for i in range(1, 11): #Loop for multiple pages.
    
    urls = f"https://www.urbancompany.com/reviews?p={i}" 
    ct = requests.get(urls)
    soup = BeautifulSoup(ct.content)


    coms = soup.find_all("div", class_ ="ReviewPageReview__topInfo--3ibra")


    for com in coms:
        name = com.find("span", class_ = "ellipsis").text 
        date = com.find("span", class_ = "ReviewPageReview__reviewDate--3tC00").text    
        ratings = com.find("div", class_ = "StarRatingSEO__ratingBox--3MqzX StarRatingSEO__ratingBoxSmall--4Nhn8").text
        reviews = com.find("div", class_ = "ReviewPageReview__seoLinkDiv--2RnCy")
        if reviews is None:
            comments.append("None")
        else:
            comments.append(reviews.text)
            

        names.append(name)
        dates.append(date)
        rates.append(ratings)
print(len(names))
print(len(dates))
print(len(rates))
print(len(comments))
Services = []
Places = []

for i in comments:
    
    if i != "None":
        services,place=i.split(" in ")
        Services.append(services)
        Places.append(place)
        
    elif i == "None":
        Services.append("None")
        Places.append("None")
print(len(Services))
print(len(Places))

Country = []
City = []
for i in Places:
    
    if i == "None":
        City.append("None")
        Country.append("None")
        
    elif i != "None":
        city,country=i.split(", ")
        Country.append(country)
        City.append(city)

df = pd.DataFrame()
df["Dates"] = dates
df["Names"] = names
df["Ratings"] = rates
df["Services"] = Services
df["City"] = City
df["Counrty"] = Country
df["Comments"] = comments
df.to_excel("noclause.xlsx") 