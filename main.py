# Gemaakt om data te versturen via python voor SimpleCMS
# Output logs zijn netjes gemaakt voor errors.
# Gemaakt door Milan

import requests

# Welk methode wil je aan hebben?

# True = Aan
# False = Uit

login = False
register = True

# Willen we de post in een loop zetten?
looping = False

# Url naar de controller.
url = "https://habnet.nl/Data/DataController"

# Post Request Data voor Login.
if login:

    data = {
        'action': 'Login',
        'controller': 'Auth',
        'username': 'nonetype1234',
        'password': 'nonetype1234',
    }

# Post Request Data voor Registratie.
if register:

    data = {
        'action': 'RegisterJson',
        'controller': 'Auth',
        'username': 'nonetype123456',
        'password': 'nonetype123456',
        'retypedPassword': 'nonetype123456',
        'email': 'nonetype2@gmail.com',
        'look': 'hr-155-1028.hd-180-1.ch-3015-1426.lg-275-110.sh-290-1408.fa-3296-61.ca-1814-61.wa-2001-61&gender=M',
    }

# Defineer de dataChecken Variable.
dataChecken = requests.post(url, data=data).text

# Error handling en output.
if login != True:
    if dataChecken == '{"valid":true,"field":"none","response":"Je account is succesvol aangemaakt! redirecting..."}':
        print('Gebruiker Succesvol aangemaakt met de data: \n '
              'username: '
              + data['username'] +
              '\n email: '
              + data['email'] +
              '\n password: '
              + data['password'])
    else:
        print('Gebruiker is niet geregistreerd. \n'
              + 'javascript_response_error_Log: ' + dataChecken)

if register != True:
    if dataChecken == '{"valid":true,"message":"Login succesvol redirecting..."}':
        print('Gebruiker Succesvol ingelogd.')
    else:
        print('Gebruiker is niet ingelogd. \n'
              + 'javascript_response_error_Log: ' + dataChecken)
            
