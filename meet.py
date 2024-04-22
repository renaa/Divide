import bs4
import random
import requests
import sys

if len(sys.argv) != 2:
    print('Usage: python ' + sys.argv[0] + ' <group_size>')
    sys.exit(1)

try:
    group_size = int(sys.argv[1])
except ValueError:
    print("Error: group_size must be an integer.")
    sys.exit(1)

URL = 'https://www.novacare.no/menneskene'

response = requests.get(URL)
soup = bs4.BeautifulSoup(response.text, 'html.parser')
employee_tags = soup.find_all('h2', class_='employees__name')
employees = [tag.text for tag in employee_tags]    
random.shuffle(employees)

for i, employee in enumerate(employees):
    if i % group_size == 0:
        print(f'\nGruppe {int(i/group_size+1)}:')
    print(f'- {employee}')