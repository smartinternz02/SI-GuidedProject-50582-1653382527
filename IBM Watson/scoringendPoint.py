import requests

# NOTE: you must manually set API_KEY below using information retrieved from your IBM Cloud account.
API_KEY = "OuLTU0cQ8yvYhGwAVCxhN7C3iTcPwRzq21sQJ--96wBI"
token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey":
 API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
mltoken = token_response.json()["access_token"]

header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

# NOTE: manually define and pass the array(s) of values to be scored in the next line
payload_scoring = {"input_data": [{ "fields" : [["f0","f1","f2","f3","f4"]], "values" : [[30,3248,73,386,2122]] }]}

response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/ml/v4/deployments/a09d8c33-f2a2-4eca-ab8b-0e6d5ae5217f/predictions?version=2022-06-01', json=payload_scoring,
 headers={'Authorization': 'Bearer ' + mltoken})
print("Scoring response")
#print(response_scoring.json())
pred = response_scoring.json()
output = pred["predictions"][0]['values'][0][0]
print(output)