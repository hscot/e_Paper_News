from newsapi import NewsApiClient
import json
import requests

api = NewsApiClient(api_key='your-API-key-here')

source = 'die-zeit' #You can change this in accordiance with any of the sources compatable with NewsAPI
top_headlines = api.get_top_headlines(sources=source, language='de')

#If you would like to see the entire JSON text that the API pulls, you can uncomment this code here
#print(json.dumps(top_headlines, indent=4))

y = json.dumps(top_headlines)
x = json.loads(y)


#This is a remnant of some code I tested in order to make this work on the final display program. All this does is pull the source name from the dump.
source_name = x['articles'][0]['source']['name'] 
print(source_name)

#This will output the top 5 articles from the JSON file

articles = top_headlines['articles']

results = []

for ar in articles:
  results.append(ar['title'])

for i in range(0, 5):
  print(i + 1, results[i])
  
