import requests

url = "https://stroccoli-futbol-science-v1.p.rapidapi.com/s1/results/2017-01-01/2017-01-05"

querystring = {"tournament_name":"English Premier League"}

headers = {
    'x-rapidapi-host': "stroccoli-futbol-science-v1.p.rapidapi.com",
    'x-rapidapi-key': "472e13f6d7msh84492a2444096d4p1edbffjsn3ff4c1075778"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
