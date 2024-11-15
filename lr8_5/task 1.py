userquery = 'как стать бэкенд-разработчиком'
userquery = userquery.replace(' ', '%20') 
url = 'https://yandex.ru/search/?text=' + userquery

print(url) 