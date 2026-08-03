#RFC 1945 HTTP spec (May 1996)
#http uses a <major>.<minor> versioning scheme.
# http message = simple-request, simple-response, full-request, full-response
#CRLF carriage return \r line feed \n
#request-line  method SP request-URL SP http-version CRLF
#server, client, requests, and responses

#pip install requests
import requests
address = 'http://httpforever.com'
response = requests.get(address)
response.headers
response.content
dir(response)
response.request
response.request.headers

#pip install flask
#flask is a web server
#python examples/simple_server.py
#curl http://172.18.240.82:5000
#curl -X POST curl http://172.18.240.82:5000
import requests
address = 'http://172.18.240.82:5000'
response = requests.post(address)
response
response.content
#can show server log, notice IP address is different when hit it from wget or curl as opposed to other tool

#can convert any format to bytes, can represent bytes as text
#might encode into different format
#will see base64 encoding online, convert everything to bytes (2^6 = 64)
#can lookup base64 table
#can encoded character into base64 then decode it later, very inefficient every 3 bytes need 4 characters

#jupyer notebooks
#demo.ipynb

#endpoint
#required parameters
#optional parameters
#how do they handle multiple responses
#https://developer.spotify.com/documentation/web-api

# Note: You need a Spotify Premium account to use the Web API.

# Log into the dashboard using your Spotify account.
# Create an app and select "Web API" for the question asking which APIs are you planning to use. Once you have created your app, you will have access to the app credentials. These will be required for API authorization to obtain an access token.
# Use the access token in your API requests.
# You can follow the Getting started tutorial to learn how to make your first Web API call.

#https://developer.spotify.com/documentation/web-api/reference/create-playlist
# POST https://api.spotify.com/v1/me/playlists

# curl --request POST \
#   --url https://api.spotify.com/v1/me/playlists \
#   --header 'Authorization: Bearer 1POdFZRZbvb...qqillRxMr2z' \
#   --header 'Content-Type: application/json' \
#   --data '{
#     "name": "New Playlist",
#     "description": "New playlist description",
#     "public": false
# }'

# wget --quiet \
#   --method POST \
#   --header 'Content-Type: application/json' \
#   --header 'Authorization: Bearer 1POdFZRZbvb...qqillRxMr2z' \
#   --body-data '{\n    "name": "New Playlist",\n    "description": "New playlist description",\n    "public": false\n}' \
#   --output-document \
#   - https://api.spotify.com/v1/me/playlists

# echo '{
#     "name": "New Playlist",
#     "description": "New playlist description",
#     "public": false
# }' |  \
#   http POST https://api.spotify.com/v1/me/playlists \
#   Authorization:'Bearer 1POdFZRZbvb...qqillRxMr2z' \
#   Content-Type:application/json

# Request Body
# {
#     "name": "New Playlist", 
#     "description": "New playlist description", 
#     "public": false
# }
# Body aplication/json
# name str (playlist name)
# public bool

#Response Example



#API
import requests
address = 'http://172.18.240.82:5000'
response = requests.post(address)
response
response = requests.post(address, data={'my_key': 'hello'})  # Passes data in body.
#response = requests.post(address, data={'my_key': 'hello'}, headers={})  # Passes data in body and headers.
response.content