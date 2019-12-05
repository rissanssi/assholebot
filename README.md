# assholebot

Alla hyvä tutorial Slackbotin tekemiseen. 

https://chatbotslife.com/write-a-serverless-slack-chat-bot-using-aws-e2d2432c380e

Meidän tapauksessamme koodissa muuttui vain se, miten chattiin annettua viestiä käsitellään.
Linkissä olevassa esimerkissä Slackbot antaa vastauksen, jossa chat-viesti on käännetty toisinpäin. Meidän proggiksessa 
käyttäjän antama viesti otetaan ns. "hakusanaksi" - elikkäs siis osaksi curlausta.

Koodista puuttuu BOT_TOKEN, joka annetaan AWS:ssä enviroment variablena. Enviroment Variable osio löytyy AWS Lambdassa
heti varsinaisen "koodiosion" alapuolelta. 

Säädettiin Slackbot ja siihen liitännäinen Api Gateway AWS:n konsolista, niin kuin tuossa ohjeessakin tehdään.
 :( Slackbotin koodi löytyy tiedostosta perse.py. 
