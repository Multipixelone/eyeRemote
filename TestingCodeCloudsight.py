import requests

LOCALE = 'en-US'
LANGUAGE = 'en-US'
URL = 'http://api.cloudsightapi.com/image_responses/'

header = {
'Authorization' : 'CloudSight API KEY HERE'
}

imageFile = {'image_request[image]': ('image.jpg', open('image.jpg', 'rb'), 'image/jpg')}

def postRequest():
global URL
print("Uploading")
print(imageFile)

postData = {
    #'image_request[remote_image_url]': 'https://www.google.co.uk/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png',
    'image_request[locale]': LOCALE,
    'image_request[language]': LANGUAGE
}

rPost = requests.post("https://api.cloudsightapi.com/image_requests", headers=header, data=postData, files=imageFile)
print(rPost.status_code)
print(rPost.text)`
