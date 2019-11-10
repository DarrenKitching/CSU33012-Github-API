from plotly.offline import plot
import plotly.graph_objs as go
import pandas as pd
from datetime import datetime
import requests
	
def getBarChartData(name, password):
	api = 'https://api.github.com/users/'
	fullUrl = api+name
	response = (requests.get(fullUrl, auth=(name, password))).json()
	names = [str(response['name'])]
	followers = [str(response['followers'])]
	following = [str(response['following'])]
	followingURL = fullUrl + '/following'
	followingResponse = (requests.get(followingURL, auth=(name, password))).json()
	for x in followingResponse:
		user = (requests.get(api + str(x['login']), auth=(name, password)).json())
		usersName = str(user['name'])
		if usersName != 'None':
			names.append(usersName)
		else:
			names.append(user['login'])
		followers.append(str(user['followers']))
		following.append(str(user['following']))

	animals=[str(response['name']), 'orangutans', 'monkeys']
	fig = go.Figure(data=[
		go.Bar(name='Followers', x=names, y=followers),
		go.Bar(name='Following', x=names, y=following)
	])
	fig.update_layout(
		barmode='group',
		title='How connected are you compared to your friends?'
	)
	plot_div = plot(fig, output_type='div', include_plotlyjs=False)
	return plot_div

def getPieChartData(name, password):
	api = 'https://api.github.com/users/'
	fullUrl = api+name+'/repos'
	response = (requests.get(fullUrl, auth=(name, password))).json()
	labels = []
	values = []
	for x in response:
		languageURL = (requests.get(str(x['languages_url']), auth=(name, password))).json()
		for key, value in languageURL.items():
			updated = False
			for i in range(len(labels)):
				if str(key) == labels[i]:
					values[i] += int(value)
					updated = True
			if updated == False:
				labels.append(str(key))
				values.append(int(value))
	fig = go.Figure(data=[go.Pie(labels=labels, values=values)])
	fig.update_layout(
    	title = 'What are your favourite languages?'
	)
	plot_div = plot(fig, output_type='div', include_plotlyjs=False)
	return plot_div