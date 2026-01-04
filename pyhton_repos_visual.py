import requests
import plotly.express as px 

url = 'https://api.github.com/search/repositories?q=language:python+sort:stars+stars:>10000'
url += ''

header = {'accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=header)
print(f'Status Code: {r.status_code}')

response_dicts = r.json()

print(f'Complete results: {not response_dicts['incomplete_results']}')

repo_dicts = response_dicts['items']

repo_names, stars, hover_texts = [],[],[]

for dicts in repo_dicts:
    repo_names.append(dicts['name'])
    stars.append(dicts['stargazers_count'])
    
    # cria textos flutuantes 
    owner = dicts['owner']['login']
    description = dicts['description']
    hover_text = f'{owner}<br />{description}'
    hover_texts.append(hover_text)


    
fig = px.bar(x=repo_names,y= stars, labels={'x':'Repository', 'y':'Stars'}, title='Most Starred Python Projects on GitHub',hover_name=hover_texts )

fig.update_layout(title_font_size=28, xaxis_title_font_size=20, yaxis_title_font_size=20)

fig.show()
    