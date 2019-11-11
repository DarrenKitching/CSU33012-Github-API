from plotly.offline import plot
import plotly.graph_objs as go
import pandas as pd
import datetime
import requests

def switch(monthNum):
    switcher = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December"
    }
    return switcher.get(monthNum, "Invalid month")

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
	fig.update_traces(marker=dict(line=dict(color='#000000', width=1)))
	plot_div = plot(fig, output_type='div', include_plotlyjs=False)
	return plot_div

def getScatterPlotData(name, password):
	today = datetime.date.today()
	month = today.month
	year = today.year
	api = 'https://api.github.com/users/'
	repoAPI = 'https://api.github.com/repos/'
	fullUrl = api+name+'/repos'
	response = (requests.get(fullUrl, auth=(name, password))).json()
	commitDates = []
	for repos in response:
		commits = (requests.get(repoAPI + str(repos['full_name'] + '/commits'), auth=(name, password))).json()
		for commit in commits:
			if str(commit['author']['login']) == name:
				fullDateAndTime = commit['commit']['author']['date']
				commitDates.append(datetime.date(int(fullDateAndTime[0:4]), int(fullDateAndTime[5:7]), int(fullDateAndTime[8:10])))
	
	lastYear = int(year) - 1
	monthLastYear = int(month)
	dayLastYear = 1 # always start from beginning of month

	dateYearAgo = datetime.date(lastYear, monthLastYear, dayLastYear)
	monthAndYears = []
	monthCopy = monthLastYear
	yearCopy = lastYear
	for i in range(13):
		if monthCopy > 12:
			monthCopy = 1
			yearCopy = yearCopy + 1
		monthAndYears.append(str(switch(monthCopy))+ ' ' + str(yearCopy))
		monthCopy += 1
	monthCommitCount = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
	for entry in commitDates:
		if entry > dateYearAgo:
			commitMonth = entry.month
			commitYear = entry.year
			dateString = str(switch(commitMonth)+ ' ' + str(commitYear))
			for i in range(len(monthAndYears)):
				if monthAndYears[i] == dateString:
					monthCommitCount[i] += 1

	fig = go.Figure()
	fig.add_trace(go.Scatter(x=monthAndYears, y=monthCommitCount, mode='lines+markers', name='lines+markers'))
	fig.update_layout(
    	title = 'Number of commits per month in the last year'
	)
	plot_div = plot(fig, output_type='div', include_plotlyjs=False)
	return plot_div