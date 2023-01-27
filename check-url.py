import requests
import datetime
import traceback

protocol = input('Введите протокол http или https:')
url = input('Введите адрес сайта:')

try:
    response = requests.get(protocol + '://' + url, timeout=(1.0000, 3.0000))
    if response.status_code in range(100,200):
        message = 'Informational:'
    elif response.status_code in range(200,300):
        message = 'Successful:'
    elif response.status_code in range(300,400):
        message = 'Redirects:'
    elif response.status_code in range(400,500):
        message = 'Client errors:'
    else:
        message = 'Server errors:'

    print(datetime.datetime.now(), message, response.status_code)

except:
    print('Что-то пошло не так. Подробности смотри в trace.txt')
    with open('trace.txt', 'w') as fp:
        traceback.print_exc(file=fp)
