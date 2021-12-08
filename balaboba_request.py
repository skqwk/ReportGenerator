import json
import urllib.request 


headers = {
    'Content-Type': 'application/json',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_4) AppleWebKit/605.1.15 '
                  '(KHTML, like Gecko) Version/14.1.1 Safari/605.1.15',
    'Origin': 'https://yandex.ru',
    'Referer': 'https://yandex.ru/',
}


queries = {
    "Вывод" : ["В ходе выполнения практической работы по теме ", " мы изучили "],
    "Введение" : ["В данной практической работе по теме ", " рассматривается "],
}


API_URL = 'https://zeapi.yandex.net/lab/api/yalm/text3'
def generateDescription(topic, style):
    query =  f"{queries[style][0]} «{topic}» {queries[style][1]}"
    payload = {"query": query, "intro": 0, "filter": 1}
    params = json.dumps(payload).encode('utf8')
    req = urllib.request.Request(API_URL, data=params, headers=headers)
    response = urllib.request.urlopen(req)

    data = json.loads(response.read().decode('utf8'))
    
    return query + data["text"]