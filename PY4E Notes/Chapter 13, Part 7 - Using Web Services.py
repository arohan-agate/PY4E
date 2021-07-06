# Using GeoJSON API
import urllib.request, urllib.parse, urllib.error  # imports urllib
import json  # imports json

serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'  # contains the url as a string

while True:
    address = input('Enter location: ')  # address holds the inputted string address
    if len(address) < 1:
        break

    url = serviceurl + urllib.parse.urlencode({'address' : address})  # make a URL by concatenating the url with the
    # parameters

    print('Retrieving', url)
    uh = urllib.request.urlopen(url)  # urlopen returns a handle
    data = uh.read().decode()  # .read() pulls also the data and text, need to decode the data
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)  # parses the data from Google. Returns a Dictionary
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':  # checks to see if you got good data
        print('==== Failure to Retrieve ====')
        print(data)
        continue

    lat = js["results"][0]["geometry"]["location"]["lat"]  # extracts the actual data for the latitude
    lng = js["results"][0]["geometry"]["location"]["lng"]  # extracts the actual data for the longitude
    print('lat', lat, 'lng', lng)
    location = js['results'][0]['formatted_address']
    print(location)
