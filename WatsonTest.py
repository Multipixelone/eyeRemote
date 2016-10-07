from tts_watson.TtsWatson import TtsWatson

ttsWatson = TtsWatson('watson_user', 'watson_password', 'en-US_AllisonVoice') # en-US_AllisonVoice is a voice from watson you can found more to: https://www.ibm.com/smarterplanet/us/en/ibmwatson/developercloud/doc/text-to-speech/using.shtml#voices
ttsWatson.play("Welcome to the Remote! Press the big button to take a picture, and press the smaller button for more information") 
