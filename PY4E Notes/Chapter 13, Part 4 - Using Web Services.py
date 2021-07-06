import xml.etree.ElementTree as ET
input = '''<stuff>
    <users>
        <user x="2">
            <id>001</id>
            <name>Chuck</name>
        </user>
        <user x="7">
            <id>009</id>
            <name>Brent</name>
        </user>
    </users>
</stuff>'''

stuff = ET.fromstring(input)  # stuff is a tree of information
lst = stuff.findall('users/user')  # searches for all the "user" tags below "users". get both tags (as trees) in a list
print('User count:', len(lst))  # prints the number of items in the list, number of users
for item in lst:  # item is the iteration variable that goes through lst
    print('Name', item.find('name').text)  # prints the text associated with the "name" child tag of the user
    print('Id', item.find('id').text)  # # prints the text associated with the "id" child tag of the user
    print('Attribute', item.get('x'))  # get the value of the attribute "x" associated with the user tag
