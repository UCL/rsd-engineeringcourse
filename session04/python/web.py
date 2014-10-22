### "URL"

import requests
ucl=requests.get(
    'http://en.wikipedia.org/wiki/University_College_London'
)
map_here=requests.get('http://maps.googleapis.com/maps/api/staticmap',
        params={'center':"51.5, -0.1", 'size':"400x400", 'zoom':10})
print ucl.url
print map_here.url

### "download"
print "Beginning of HTML file", ucl.text.split()[0:2]
with open('map.png','w') as map_image:
    map_image.write(map_here.content)

### "parse"
# pip install beautifulsoup4
from bs4 import BeautifulSoup
import re # Python regular expression library
wikipage=BeautifulSoup(ucl.text)
# HTML looks like <span class="latitude">value</span>
motto=wikipage.find(text=re.compile("Motto"))

#print 'Coordinates:', latitude, longitude
