import requests
import json
import secret
PollAPI = "https://api.strawpoll.com/v3/polls"
xapiKey = secret.XapiKey()
def makePoll(pollName, arrayOfOptions):
    listOfOptionDictionary = []
    counter = 0
    for i in arrayOfOptions:
        section = {
            "type": "text",
            "value": i
        } 
        listOfOptionDictionary.append(section)
        counter = counter + 1
        
    PollCreation = {"title": pollName.content,
    "poll_options":listOfOptionDictionary, 
    "type":"multiple_choice",
    "poll_config": {
        "is_private":True,
        "vote_type":"default",
        "allowed_comments":False,
        "allow_indeterminate":False,
        "allow_other_option": False,
		"custom_design_colors": None,
		"duplication_checking": "ip",
		"allow_vpn_users": False,
		"edit_vote_permissions": "nobody",
		"force_appearance": None,
		"hide_participants": False,
		"is_multiple_choice": False,
		"multiple_choice_min": None,
		"multiple_choice_max": None,
		"number_of_winners": 1,
    }}
#Above is the json object. Most of it is taken directly from the github of strawpoll!

    data = json.loads(json.JSONEncoder().encode(PollCreation)) 
    dataBack = requests.post(url=PollAPI,json=data,headers={'X-API-KEY': xapiKey})
    return dataBack.json()
    
