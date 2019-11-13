# CSU33012-Github-API
Assignment to visualize Github data using the Github API.

<h1>Overview</h1>
<p>
For this project I built a website using the Django Framework which allows someone to login with their Github credentials and see three graphs which shows them critical data about their performance on Github.
</p>

![Alt text](/Images/LoginPage.PNG?raw=true "Login page")

<p> 
The first page shows a bar chart which shows how connected on Github a user is by comparing their follower and following count with that of their friends. This allows the user to see if their friends are better or worse connected than they are.
</p>

![Alt text](/Images/BarChartPage.PNG?raw=true "Bar Chart")

<p> 
This page has buttons which link to the two other graphs. One of which is a Pie Chart that will show you your most used langauges telling you what percentage of code you have committed to Github is written in that language.
</p>

![Alt text](/Images/PieChartPage.PNG?raw=true "Pie Chart")

<p>
The final graph is a Scatter Plot which shows you how many commits you have made per month over the last year. This will tell the user if they have increased or decreased in productivity over the year. 
</p>

![Alt text](/Images/ScatterPlotPage.PNG?raw=true "Scatter Plot")

<h1>Install and Run</h1>
<p>
Naviagte into the SocialGraph folder where you will see a file called 'requirements.txt'.
</p>
<p>
Run <b>pip3 install -r requirements.txt</b>
</p>
<p>
When everything has installed navigate into the next SocialGraph folder where you will see a file called 'manage.py'.
</p>
<p>
Run <b>python3 manage.py runserver</b>
</p>
<p>
Once the website has fully loaded navigate to http://localhost:8000/ on your favourite browser and login with Github credentials.
</p>
