import cloudsight
import picamera

camera = picamera.PiCamera()
auth = cloudsight.SimpleAuth('your-api-key')
api = cloudsight.API(auth)

camera.capture('image.jpg')

with open('image.jpg', 'rb') as f:
    response = api.image_request(f, 'image.jpg', {
        'image_request[locale]': 'en-US',
    })
    
status = api.image_response(response['token'])
if status['status'] != cloudsight.STATUS_NOT_COMPLETED:
    # Done!
    pass
