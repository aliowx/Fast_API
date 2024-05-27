import requests

proxies = {
    "http": None,
    "https": None,
}


response = requests.get('https://www.translated.net/hts/?f=quote&s=en-GB&t=bg-BG&w=100&cid=htsdemo&p=htsdemo5&of=json', proxies=proxies)



print(response.json)






