#THIS CODE IS FOR REFRESHING THE ACCESS TOKEN NEEDED FOR WEB API

import json
import requests
from SpotipySecrets import refresh_token, base_64

class Refresh:

    # initialize class variables
    def __init__(self):
        self.refresh_token = "AQDr060RMsTXy0T2hLbhQ_60u6Qdl58P5JCH1n0WXcX4LFgNHaV7RSUTKPSVpBa7qHXdvkc-OZC6eanTZQxaKDbTy6BN8cIdo1o9cw6qF1El9CRGnIZ7EJl2oRy_MKmU5rk" 
        self.base_64 = "NDA2ZGJlNzI2NDIzNGU1OTgyNGY5MWFhM2ZkZWJiYjg6MjlhOGNmYTU2Njc2NDgxNGExOTI5Y2RkYWUyNjJhODA="   # base 64 (client id:client secret)

    # refreshes token
    def refresh(self):

        query = "https://accounts.spotify.com/api/token"
        data = {"grant_type": "refresh_token", "refresh_token": self.refresh_token}
        response = requests.post(query, data, headers = {"Authorization": "Basic " + self.base_64})

        response_json = response.json()
        #print(response_json)

        return response_json["access_token"]    # return the new access_token accquired from refresh

