import http.client
import json

for i in range(1, 1000):
    conn = http.client.HTTPSConnection("google.serper.dev")
    payload = json.dumps({
      "q": f"inurl:.php?id={i} site:jp",
      "gl": "id",
      "num": 100
    })
    headers = {
      'X-API-KEY': 'apimu',
      'Content-Type': 'application/json'
    }
    conn.request("POST", "/search", payload, headers)
    res = conn.getresponse()
    data = res.read()
    responseData = json.loads(data)
    organicResults = responseData.get('organic', [])
    links = [result.get('link') for result in organicResults]

    with open('result.txt', 'a', encoding='utf-8') as file:
        for link in links:
            file.write(link + '\n')

print("Done! Link yang di dapat: ", len(links))
