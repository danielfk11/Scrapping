from bs4 import BeautifulSoup
import requests

url = "" # url que deseja buscar (EX: https://google.com)

r = requests.get(url)
rhtml = r.content

soup = BeautifulSoup(rhtml, 'html.parser')

locate = soup.find(class_='') ## class do html
locate_id = soup.find(id='')  ## id do html

locate_Text = locate.text
locate_id_Text = locate_id.text

print(locate_Text)
print(locate_id_Text)
