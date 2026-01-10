import requests
import plotly.express as px 



url = 'https://api.github.com/search/repositories?q=language:java+sort:stars+stars:>10000'
r = requests.get(url)
header = {'accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=header)

print(f'Status Code: {r.status_code}')

response_dict = r.json()

items = response_dict['items']

names, stars_count, links, hover_names = [],[],[],[]



for key in items:
    link = key['html_url']
    name = key['name']
    name_links = f'<a href="{link}">{name}</a> '
    stars = key['stargazers_count']
    
    names.append(name_links)
    stars_count.append(stars)
    login = key['owner']['login']
    descripition = key['description']
    hover_name = f'Login:{login}<br />Descricao:{descripition}"'       
    hover_names.append(hover_name)
    
    
    # links.append(link)
    
    
    
    
fig = px.bar(x=names,y=stars_count, labels={'x':'Nomes dos repositorios', 'y':'Estrelas'},hover_name=hover_names, title='Projetos mais famosos de Java no Github')
fig.show()

