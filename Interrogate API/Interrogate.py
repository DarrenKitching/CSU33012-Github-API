import sys
import requests

def displayDetails():
	api = 'https://api.github.com/users/'
	user = input('Please enter the username to display data on: ')
	fullUrl = api+user
	response = (requests.get(fullUrl)).json()
	print('Name: ' + str(response['name']))
	print('id: ' + str(response['id']))
	print('Location: ' + str(response['location']))
	print('Bio: ' + str(response['bio']))
	print('Followers: ' + str(response['followers']))
	print('Following: ' + str(response['following']))
	#print(response['followers'])

def main():
	displayDetails()
	
if __name__ == '__main__':
    main()
