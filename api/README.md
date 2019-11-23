This module contains the API for this webapp. After you've git cloned this repo, you're able to use it getting into the teams folder and then using the follow command:

python -m api.v1.app

The following routes are enabled at this moment:

/api/v1/people/<username> :Returns a personalized JSON using an existent public_Id on Torre's API

/api/v1/people/<username>/connections: Returns a list of connections for the given public_Id with their personal info. It's possible to use q= and limit= on the route, like this way:

/api/v1/people/<username>/connections?q=<random_name>&limit=<int number>

/api/v1/people/<username>/buildateam?skill=<any_skill>

This is the main route. You provide an username (public_Id) and the skills you prefer and a dictionary of skills and the person on the username connections with the highest weight on that skill will be the value.
