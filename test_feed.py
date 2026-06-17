import requests
import xml.etree.ElementTree as ET

url = 'https://docs.cloud.google.com/feeds/bigquery-release-notes.xml'
try:
    response = requests.get(url)
    print("Status code:", response.status_code)
    print("Content preview:", response.text[:1000])
    
    root = ET.fromstring(response.content)
    print("Root tag:", root.tag)
    # Print namespaces
    import re
    ns = re.match(r'{.*}', root.tag)
    ns_str = ns.group(0) if ns else ''
    print("Namespace:", ns_str)
    
    # Let's see some entries
    entries = root.findall(f'{ns_str}entry')
    print("Number of entries:", len(entries))
    if entries:
        first = entries[0]
        title = first.find(f'{ns_str}title')
        updated = first.find(f'{ns_str}updated')
        content = first.find(f'{ns_str}content')
        print("First Entry Title:", title.text if title is not None else 'None')
        print("First Entry Updated:", updated.text if updated is not None else 'None')
        print("First Entry Content Preview:", content.text[:500] if content is not None and content.text else 'None')
except Exception as e:
    print("Error:", e)
