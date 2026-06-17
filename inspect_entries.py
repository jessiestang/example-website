import requests
import xml.etree.ElementTree as ET

url = 'https://docs.cloud.google.com/feeds/bigquery-release-notes.xml'
response = requests.get(url)
root = ET.fromstring(response.content)
ns = "{http://www.w3.org/2005/Atom}"

for entry in root.findall(f'{ns}entry')[:5]:
    title = entry.find(f'{ns}title').text
    content = entry.find(f'{ns}content').text
    print("--- Entry Title:", title)
    print("Content:")
    print(content)
    print("\n" + "="*40 + "\n")
