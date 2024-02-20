import bs4
import random
import requests

GROUP_SIZE = 3
URL = 'https://www.novacare.no/menneskene'

response = requests.get(URL)
soup = bs4.BeautifulSoup(response.text, 'html.parser')
employee_tags = soup.find_all('h2', class_='employees__name')
employees = [tag.text for tag in employee_tags]    
random.shuffle(employees)

for i, employee in enumerate(employees):
    if i % GROUP_SIZE == 0:
        print(f'\nGruppe {int(i/3+1)}:')
    print(f'- {employee}')