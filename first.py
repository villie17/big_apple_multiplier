import requests
import json

resp = requests.get('https://api.nytimes.com/svc/archive/v1/2019/11.json?api-key=')

if resp.status_code != 200:
    # This means something went wrong.
    raise ApiError('GET  {}'.format(resp.status_code))

js = resp.json();
hits = js["response"]["meta"]["hits"]
print ("Number of hits: ", hits)
print ("Response:",  hits)
docs = js["response"]["docs"]
for d in docs:
    print(d["abstract"])