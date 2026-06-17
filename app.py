import re
import requests
import xml.etree.ElementTree as ET
from flask import Flask, jsonify, render_template

app = Flask(__name__)

FEED_URL = 'https://docs.cloud.google.com/feeds/bigquery-release-notes.xml'

def parse_content(html_content):
    if not html_content:
        return []
    
    # Split by h3 tags (case insensitive just in case, though standard is <h3>)
    parts = re.split(r'<h3>(.*?)</h3>', html_content, flags=re.DOTALL)
    
    updates = []
    # If there is text before the first <h3>
    first_part = parts[0].strip()
    if first_part:
        updates.append({
            "type": "General",
            "html": first_part
        })
        
    for i in range(1, len(parts), 2):
        if i + 1 < len(parts):
            up_type = parts[i].strip()
            up_html = parts[i+1].strip()
            updates.append({
                "type": up_type,
                "html": up_html
            })
    return updates

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/release-notes')
def get_release_notes():
    try:
        response = requests.get(FEED_URL, timeout=10)
        response.raise_for_status()
        
        root = ET.fromstring(response.content)
        
        # Determine namespace
        ns_match = re.match(r'{.*}', root.tag)
        ns = ns_match.group(0) if ns_match else ''
        
        feed_updated = root.find(f'{ns}updated')
        feed_updated_val = feed_updated.text if feed_updated is not None else ''
        
        entries_data = []
        for entry in root.findall(f'{ns}entry'):
            title = entry.find(f'{ns}title')
            title_text = title.text if title is not None else ''
            
            entry_id = entry.find(f'{ns}id')
            id_text = entry_id.text if entry_id is not None else ''
            
            updated = entry.find(f'{ns}updated')
            updated_text = updated.text if updated is not None else ''
            
            # Extract alternate link
            link_href = ''
            for link in entry.findall(f'{ns}link'):
                if link.get('rel') == 'alternate' or not link.get('rel'):
                    link_href = link.get('href')
                    break
            
            content = entry.find(f'{ns}content')
            content_html = content.text if content is not None else ''
            
            updates = parse_content(content_html)
            
            entries_data.append({
                "date": title_text,
                "id": id_text,
                "updated": updated_text,
                "link": link_href,
                "updates": updates
            })
            
        return jsonify({
            "success": True,
            "updated": feed_updated_val,
            "entries": entries_data
        })
        
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
