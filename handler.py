import urllib3
from bs4 import BeautifulSoup
import boto3
import re
from botocore.vendored import requests

def sendEmail(event, context):
    data = event['body']
    hakusana = data['hakusana']
    source = data['source']
    destination = data['destination']
    url = 'https://api.stackexchange.com/2.2/search?order=desc&sort=votes&intitle=' + hakusana + '&site=stackoverflow'
    r = requests.get(url)
    data = r.json()

    #for d in sorted():
    #print(str(data))
    try:
        haku2 = (data['items'][0]['link'])
    except:
        haku2 = "Vittu mitä bugista paskaa. Eihän tämä saatana edes buildaa!"
    #print(haku2)

    http = urllib3.PoolManager()
    news = http.request('GET', haku2)
    soup = BeautifulSoup(news.data, 'html.parser')
    lista = []
    for s in soup.find_all(attrs={"class": "answercell post-layout--right"}):
        #print(s.text)
        lista.append(s.text)
    #print(lista[0])
    message = lista[0]

    client = boto3.client('ses' ) 
    client.send_email(
        Destination={
            'ToAddresses': [destination]
            },
        Message={
            'Body': {
                
                'Text': {
                    'Charset': 'UTF-8',
                    'Data': message,
                },
            },
            'Subject': {
                'Charset': 'UTF-8',
                'Data': "Hanki osaaminen.",
            },
        },
        Source=source,
    )

    return message

    #var = re.search(r"(text\">\n<p>)(.*)(<\/p>)", str(soup))
    #print(var.group(2))