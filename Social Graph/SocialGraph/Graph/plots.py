from plotly.offline import plot
import plotly.graph_objs as go
import pandas as pd
from datetime import datetime
import requests
	
def getBarChartData(name):
	api = 'https://api.github.com/users/'
	fullUrl = api+name
	response = (requests.get(fullUrl)).json()
	names = [str(response['name'])]
	followers = [str(response['followers'])]
	following = [str(response['following'])]
	followingURL = fullUrl + '/following'
	followingResponse = (requests.get(followingURL)).json()
	for x in followingResponse:
		user = (requests.get(api + str(x['login'])).json())
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
	fig.update_layout(barmode='group')
	plot_div = plot(fig, output_type='div', include_plotlyjs=False)
	return plot_div

def getPieChartData(name):
	api = 'https://api.github.com/users/'
	fullUrl = api+name
	response = (requests.get(fullUrl)).json()
	labels = []
	values = []
	
	fig = go.Figure(data=[go.Pie(labels=labels, values=values)])
	fig.show()
	plot_div = plot(fig, output_type='div', include_plotlyjs=False)
	return plot_div