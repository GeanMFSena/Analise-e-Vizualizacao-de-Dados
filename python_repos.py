import requests

# cria uma chamada de API e verifica resposta

url = 'https://api.github.com/search/repositories'
url += '?q=language:python+sort:stars:>10000'

header = {'accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=header)
print(f'status code: {r.status_code}')

# converte o objeto de resposta em um dicionario 

reponse_dict = r.json()

# processa os resultados 
print(reponse_dict.keys())
print(f'Total Repositories: {reponse_dict['total_count']}')
print(f'complete results: {not reponse_dict['incomplete_results']}')

# explora informacoes sobre so repositorios 

repo_dicts = reponse_dict['items']
print(f'repositories returned: {len(repo_dicts)}')

# examina o primeiro repositorio 

repo_dict = repo_dicts[0]

print(f'\nkeys: {len(repo_dict)}')
for key in sorted(repo_dict.keys()):
    ...
    print(key)
    
print()

for repo_dict in repo_dicts:
    print(f'\nSelected information about first repository')
    print(f'Name: {repo_dict['name']}')
    print(f'Owner: {repo_dict['owner']['login']}')
    print(f'Stars: {repo_dict['stargazers_count']}')
    print(f'Created: {repo_dict['created_at']}')
    print(f'Updated: {repo_dict['updated_at']}')
    print(f'Descripition: {repo_dict['description']}')

