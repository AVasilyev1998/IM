import requests
import bs4
import fake_useragent

response = requests.get('https://animestars.org/topanime.html',\
                        headers={'User-Agent': fake_useragent.UserAgent().random})

# print(response.text)
soup = bs4.BeautifulSoup(response.text, 'html5lib')

results = soup.find_all('a', {'class': 'short-t'})

with open('films', 'w') as writer:
    for name in results:
        writer.write(f'{name.text}\n')
