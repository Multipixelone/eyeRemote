#!/usr/bin/python
import requests
import json
from time import sleep
from LocalVariables import key

LOCALE = 'en-US'
LANGUAGE = 'en-US'
URL = 'http://api.cloudsightapi.com/image_responses/'

global header
header = {
'Authorization' : 'CloudSight %s' % key
}

imageFile = {'image_request[image]': ('image.jpg', open('image.jpg', 'rb'), 'image/jpg')}

def postRequest():
        global URL
        print("Uploading")
        print(imageFile)

postData = {
    	'image_request[locale]': LOCALE,
    	'image_request[language]': LANGUAGE
}

def UploadPicture():
        print('Uploading Picture...')
	rPost = requests.post("https://api.cloudsightapi.com/image_requests", headers=header, data=postData, files=imageFile)
        sleep(1)
        print(rPost)
	parsed_json = json.loads(rPost.text)
	token = parsed_json['token']
	print("Parsed Token:")
        print(token)
        request = URL + token
        sPost = requests.get(request, headers=header)
        parsed_json = json.loads(sPost.text)
        status = parsed_json['status']
        while status != 'completed':
                sPost = requests.get(request, headers=header)
                status = parsed_json['status']
		print(status)
        final_json = json.loads(sPost.text)
        print(final_json['name'])
	global item
	item = final_json['name']
