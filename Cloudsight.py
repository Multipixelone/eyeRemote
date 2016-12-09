#!/usr/bin/python
from time import sleep
from LocalVariables import key
from LocalVariables import secret
import cloudsight

auth = cloudsight.OAuth('%s' % key, '%s' % secret)
api = cloudsight.API(auth)

def UploadPicture():
    with open('image.jpg', 'rb') as f:
        response = api.image_request(f, 'image.jpg', {
            'image_request[locale]': 'en-US',
        })

    status = api.wait(response['token'], timeout=30)
    status = api.image_response(response['token'])
    print(status['status'])
    if status['status'] != cloudsight.STATUS_NOT_COMPLETED:
        print(status['name'])
	global item
	item = status['name']
    else:
        print("Not Completed")
