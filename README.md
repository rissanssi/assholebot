# assholebot

Alla suht hyvä tutorial simppelin Slackbotin tekemiseen. 

https://chatbotslife.com/write-a-serverless-slack-chat-bot-using-aws-e2d2432c380e

Meidän tapauksessamme Slackbotin koodissa muuttui vain se, miten chat-viestiä käsitellään.
Linkissä olevassa esimerkissä Slackbot antaa vastauksen, jossa chat-viesti on käännetty toisinpäin. Meidän proggiksessa 
käyttäjän antama viesti otetaan ns. "hakusanaksi" - elikkäs siis osaksi curlausta.

Tästä kokonaisuudesta puuttuu Slackista saatava BOT_TOKEN, joka täytyy antaa AWS:n puolella enviroment variablena. Enviroment Variable osio löytyy AWS Lambdassa heti varsinaisen "koodiosion" alapuolelta. 

Säädettiin Slackbot ja siihen liitännäinen Api Gateway AWS:n konsolista, niin kuin tuossa ohjeessakin tehdään. :( Slackbotin koodi löytyy tiedostosta perse.py. 
