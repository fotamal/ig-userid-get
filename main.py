import requests
from bs4 import BeautifulSoup

# ig = container_id / twitter(X) = identifier

r = requests.get(input('instg url: '))

soup = BeautifulSoup(r.text, "html.parser")
scripts = soup.find_all('script')

"""with open('scr.txt', 'w+', encoding='utf-8') as f:
    for i in a:
        f.write(i.prettify() + '\n')"""

"""for i in a:
    print(i.find('require'))"""

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

"""with open("response.txt", "w", encoding='utf-8') as f:
    f.write(soup.prettify())"""
