import requests
url = 'http://rxid-ds.us-east-2.elasticbeanstalk.com/rxdata'
data = '{ "pill_name" : "None", "imprint":"FR;8", "color": "", "shape": ""}'
response = requests.post(url, data)
print(response)
response.json()