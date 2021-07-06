import urllib.request, urllib.parse, urllib.error  # uses urllib
import twurl  # library that augments URLs and deals with authorization
import json  # uses json

TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'  # URL from documentation, where you go to get friends list

while True:
    print('')
    acct = input('Enter Twitter Account: ')  # asks for Twitter account
    if len(acct) < 1:
        break  # skips out if nothing is inputted
    url = twurl.augment(TWITTER_URL,
                        {'screen_name' : acct, 'count' : '5'})
    print('Retrieving', url)
    connection = urllib.request.urlopen(url)  # opens the URL
    data = connection.read().decode()  # reads the connection and decodes the data, turns it into a string
    headers = dict(connection.getheaders())  # gets the headers back as a dictionary
    print('Remaining', headers['x-rate-limit-remaining'])
    js = json.loads(data)  # parses the data
    print(json.dumps((js, indent=4)))  # prints out the json in a structured way

    for u in js['users']:  # u loops through the array, js['users']
        print(u['screen_name'])  # prints out the user screen name
        s = u['status']['text']  # stores the text within the status of each user
        print('   ', s[:50]) # prints out the text within the status of each user (first 50 characters)