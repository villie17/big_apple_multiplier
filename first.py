import requests
import json

KEY = ''

def monthly_summary():
    resp = requests.get('https://api.nytimes.com/svc/archive/v1/2019/11.json?api-key=' + KEY)

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

def semantic_api():
    resp = requests.get("http://api.nytimes.com/svc/semantic/v2/concept/search.json?query=Pakistan&concept_type=nytd_geo&api-key="
 + KEY)

    if resp.status_code != 200:
            # This means something went wrong.
            print("Error: {}".format(resp.status_code))
    js = resp.json();
    print ("Response: ", js)

if __name__ == "__main__":
    semantic_api()

