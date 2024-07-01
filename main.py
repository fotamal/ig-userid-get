import requests
from bs4 import BeautifulSoup

# ig = container_id / twitter(X) = identifier

site = 0
url = input('instg url: ')

if url.find('instagram.com') != -1: #instagram.com
    site = 1
elif url.find('x.com') != -1:       #x.com
    site = 2

r = requests.get(url)

if site == 1:
    soup = BeautifulSoup(r.text, "html.parser")
    scripts = soup.find_all('script')
    title = soup.find('title')

    with open("response.txt", "w", encoding='utf-8') as f:
        f.write(soup.prettify())

    with open('scr.txt', 'w+', encoding='utf-8') as f:
        for i in scripts:
            f.write(i.prettify() + '\n')

    temp = ''

    #find container_id from html source
    for i in scripts:
        n = i.prettify().find('container_id')
        if n != -1:
            for x in range(n, n+50):
                temp = temp + i.prettify()[x]

    #extract usrID num from str found above
    usr_id = ''.join(list(filter(lambda x: x.isdigit() != 0, temp)))

print(usr_id)
print(title)

