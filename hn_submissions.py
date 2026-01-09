from operator import itemgetter
import json 
import requests

# cria uma chamada de api e verifica a resposta 

url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(f'Status Code: {r.status_code}')
submissions_id = r.json()

submissions_dicts = []

for sub_ids in submissions_id[:5]:
    # cria uma nova chamada de api para cada contribuicao do artigo 
    url = f'https://hacker-news.firebaseio.com/v0/item/{sub_ids}.json'
    r = requests.get(url)
    print(f'id: {sub_ids}\tStatus : {r.status_code}')
    response_dict  = r.json()
    # Cria um dicionario para cada artigo
    submissions_dict = {
        'Title':response_dict['title'],
        'hn_link': f'https://news.ycombinator.com/item?id={sub_ids}',
        'comments': response_dict['descendants']
    }
    submissions_dicts.append(submissions_dict)
    
submissions_dicts = sorted(submissions_dicts, key=itemgetter('comments'), reverse=True)

for sub_dict in submissions_dicts:
    print(f'\nTitle: {sub_dict['Title']} ')
    print(f'\nDiscussion Link: {sub_dict['hn_link']} ')
    print(f'\nComments: {sub_dict['comments']} ')


