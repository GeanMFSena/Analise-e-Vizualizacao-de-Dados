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

repo_names, stars, hover_texts,repo_links = [],[],[],[]

for dicts in repo_dicts:
    name = dicts['name']
    repo_names.append(name)
    stars.append(dicts['stargazers_count'])
    
    # pega o link de cada projeto
    link = dicts['html_url']
    repo_link = f'<a href="{link}">{name}</a> '
    repo_links.append(repo_link)
    
    # cria textos flutuantes 
    owner = dicts['owner']['login']
    
    description = dicts['description']
    hover_text = f'{owner}<br />{description}'
    hover_texts.append(hover_text)


    
fig = px.bar(x=repo_links,y= stars, labels={'x':'Repository', 'y':'Stars'}, title='Most Starred Python Projects on GitHub',hover_name=hover_texts )

fig.update_layout(title_font_size=28, xaxis_title_font_size=20, yaxis_title_font_size=20)
fig.update_traces(marker_color='SteelBlue', marker_opacity=0.6)


fig.show()
