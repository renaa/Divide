import bs4
import random
import requests
import bs4

GROUP_SIZE = 3

url = 'https://www.novacare.no/menneskene'
response = requests.get(url)
soup = bs4.BeautifulSoup(response.text, 'html.parser')
employee_tags = soup.find_all('h2', class_='employees__name')
employees = [tag.text for tag in employee_tags]
    
random.shuffle(employees)

for i, person in enumerate(employees):
    if i % GROUP_SIZE == 0:
        print(f'\nGruppe {int(i/3+1)}:')
    print(f'- {person}')