# Parsing XML
import xml.etree.ElementTree as ET  # required import statement, "as" declares "ET" as an alias

data = '''<person>
    <name>Chuck</name>
    <phone type="intl">
        +1 734 303 4456
    </phone>
    <email hide="yes"/>
</person>'''  # triple quoted string. string on multiple lines. newlines at the end of each line are part of the string.

tree = ET.fromstring(data)  # fromstring turns the text into a tree-like memory structure, assigned to the tree variable
print('Name:', tree.find('name').text)  # finds the tag 'name' within the XML data, .text finds the actual string name
print('Attr:', tree.find('email').get('hide'))  # finds email node. Gets the attribute named hide, returns "yes"
