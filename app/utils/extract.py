import requests

def yield_data(data):
    if data == None:
        return []
    for row in data:
        if "@url" in row:
            # Download the data first
            r = requests.get(row["@url"], allow_redirects=True, stream=True, timeout=6000)
            d = r.json().get("data")
            if d:
                yield from yield_data(d) 
        else:
            yield row