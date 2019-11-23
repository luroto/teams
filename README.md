# Torre-teams

This is an API that consumes another API. On this case, it will feed from Torre's API and its purpose is create teams. 

## How to install it:

  Make a git clone from this repository:
  
  ``` git clone https://github.com/luroto/teams.git```
  
  ```cd``` into ```teams``` folder and after that you can give this command:
  
  ```pip install -r requirements.txt```
  
  Then, you can run this command:
  
  ```python3 -m app```
### How it works:

Inside your shell you can try this endpoints:

```curl -X GET http://0.0.0.0:5000/api/v1/people/<public_Id>```

This create a dictionary condensed from the Torre API with the essential info.

```curl -X GET http://0.0.0.0:5000/api/v1/people/<public_Id>/connections```

This create a dictionary for the people connected to that public_Id. It accepts degree (1 or 2) as query string.

```curl -X GET http://0.0.0.0:5000/api/v1/people/<public_Id>/buildateam?skill=<skillname>```


This endpoint receives skills, queries (q) and limit into its URL. Given a skill or a set of skills this endpoint returns a dictionary of skills and its value will be the person from the connections of the given public_Id who has the highest weight attribute for that skill. 

### Development (Log)
I've worked in this project since some days ago. At first, this API was designed to rely on Python functions: consuming an API doesn't require a database. Or that was the initial assumption. Given the time response of this API on deployment environment it is necessary to think about a database schema for making queries faster to avoid timeout on server response.
For this project were designed a couple of classes for handling resulting data (models directory) and a set of functions. For request petitions the requests Python package was chosen and for the web app was chosen Flask. Through the days the API design was reordered a couple of times and it was necessary to rewrite it. Blueprint objects were chosen for handling the views for this API. For some reason the CORS policy doesn't allow to test the API and the another web app on the same machine, even if the origins was set to "*". The other questions are the difference about behavior if gunicorn or python3 are chosen to use this API. 

