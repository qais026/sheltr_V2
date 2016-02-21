## Helper file to geocode address using Google Geocoder

import urllib, urllib.request
import json
import requests
from django.utils.encoding import smart_str

def get_lat_lng(location):
    
    # Reference: http://djangosnippets.org/snippets/293/
    
    location = urllib.parse.quote_plus(smart_str(location))
    url = 'http://maps.googleapis.com/maps/api/geocode/json?address=%s&sensor=false' % location
    response = urllib.request.urlopen(url).read() 
    result = json.loads(response.decode("utf-8"))
    if result['status'] == 'OK':
       lat = str(result['results'][0]['geometry']['location']['lat'])
       lng = str(result['results'][0]['geometry']['location']['lng'])
       return {'lat': lat, 'lng': lng}
    else:
        return ''

def get_lng_lat(location):
    
    # Reference: http://djangosnippets.org/snippets/293/
    
    location = urllib.parse.quote_plus(smart_str(location))
    url = 'http://maps.googleapis.com/maps/api/geocode/json?address=%s&sensor=false' % location
    response = urllib.request.urlopen(url).read() 
    result = json.loads(response.decode("utf-8"))
    if result['status'] == 'OK':
       lat = str(result['results'][0]['geometry']['location']['lat'])
       lng = str(result['results'][0]['geometry']['location']['lng'])

       return '%s,%s' % (lng, lat)
    else:
        return ''

def get_lat(location):
    location = urllib.parse.quote_plus(smart_str(location))
    url = 'http://maps.googleapis.com/maps/api/geocode/json?address=%s&sensor=false' % location
    response = requests.get(url)
    print(response.status_code)
    result = response.json()

    if result['status'] == 'OK':
       return str(result['results'][0]['geometry']['location']['lat'])
    else:
       print("Error loading json"  + result['status'])
       return '0'

def get_lng(location):
    location = urllib.parse.quote_plus(smart_str(location))
    url = 'http://maps.googleapis.com/maps/api/geocode/json?address=%s&sensor=false' % location
    response = requests.get(url)
    print(response.status_code)
    result = response.json()

    if result['status'] == 'OK':
       return str(result['results'][0]['geometry']['location']['lng'])
    else:
       print("Error loading json: " + result['status'])
       return '0'
