import urllib3
from bs4 import BeautifulSoup
import boto3
import re
from botocore.vendored import requests
import random

def sendEmail(event, context):
    arvonta = random.randint(1,3)
    if arvonta<3:
        data = event['body']
        hakusana = data['hakusana']
        source = data['source']
        destination = data['destination']
        url = 'https://api.stackexchange.com/2.2/search?order=desc&sort=votes&intitle=' + hakusana + '&site=stackoverflow'
        r = requests.get(url)
        data = r.json()
        message = "Vittu mita bugista paskaa. Eihan tama saatana edes buildaa!"
        #for d in sorted():
        #print(str(data))
        try:
            haku2 = (data['items'][0]['link'])
        
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
        except Exception as e:
            message = "Vittu mita bugista paskaa. Eihan tama saatana edes buildaa!"
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
    else:
        message = "Ongelmasi on niin taytta hevonpaskaa, etten jaksanut edes lukea. Nyt suihkuun ja nukkumaan. Aamulla toihin. Muuta neuvoa ei tule."
    return message + str(arvonta)

    #var = re.search(r"(text\">\n<p>)(.*)(<\/p>)", str(soup))
    #print(var.group(2))