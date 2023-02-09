import feedparser

print ('enter the url')
url = input()
try:
    title = d['feed']['title']
    print(title)

except:
    print('error')
for item in d['entries']:
    print (item['title']+ "\n" + item['link']+"\n" + item['description']+"\n")
