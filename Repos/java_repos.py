import requests


url = 'https://api.github.com/search/repositories?q=language:java+sort:stars+stars:>10000'
r = requests.get(url)
header = {'accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=header)

print(f'Status Code: {r.status_code}')

response_dict = r.json()

print(response_dict.keys())
print(f'Repositorios Totais: {response_dict['total_count']}')
print(not response_dict['incomplete_results'] )

repo_dict_items = response_dict['items']

print(f'Repositorios Retornados: {len(repo_dict_items)}')

repo_dict = repo_dict_items[0]

print(f'\nKeys em cada dicionario: {len(repo_dict)}')

for key in sorted(repo_dict):
    print(key)
    
for key in repo_dict_items:
    print(f'\nSelected information about first repository')
    print(f'Name: {key['name']}')
    print(f'Owner: {key['owner']['login']}')
    print(f'Stars: {key['stargazers_count']}')
    print(f'Created: {key['created_at']}')
    print(f'Updated: {key['updated_at']}')
    print(f'Descripition: {key['description']}')


