import urllib.request
import json

url = "https://opendata.cern.ch/api/records/?q=Jpsimumu"

try:
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    response = urllib.request.urlopen(req, timeout=10)
    data = json.loads(response.read().decode('utf-8'))
    
    for hit in data.get('hits', {}).get('hits', []):
        record_id = hit.get('id')
        print(f"Record {record_id}: {hit.get('metadata', {}).get('title', 'Unknown')}")
        
        # Check files
        files = hit.get('metadata', {}).get('_files', [])
        for f in files:
            if 'csv' in f.get('key', '').lower():
                print(f" -> Found CSV: {f.get('key')} | URL: https://opendata.cern.ch/record/{record_id}/files/{f.get('key')}")
                
except Exception as e:
    print(f"Error: {e}")
