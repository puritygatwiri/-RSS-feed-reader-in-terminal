import feedparser
print ('enter the url')
url = input()
d = feedparser.parse(url)

try:
    title = d['feed']['title']
    print(title)

except:
    print('error')
for item in d['entries']:
    print (item['title']+ "\n" + item['link']+"\n" + item['description']+"\n")
