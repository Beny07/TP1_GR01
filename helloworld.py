import requests

url = "https://covid-193.p.rapidapi.com/countries"

headers = {
	"X-RapidAPI-Key": "04e141f621mshff42f59e4293c77p1d374djsne10510899cae",
	"X-RapidAPI-Host": "covid-193.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers)

print(response.text)