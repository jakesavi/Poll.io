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
    "type":"ranked_choice",
    "poll_config": {
        "is_private":False,
        "vote_type":"default",
        "allowed_comments":False,
        "allow_indeterminate":False,
        "allow_other_option": False,
		"custom_design_colors": None,
		"deadline_at": None,
		"duplication_checking": "ip",
		"allow_vpn_users": False,
		"edit_vote_permissions": "nobody",
		"force_appearance": None,
		"hide_participants": False,
		"is_multiple_choice": False,
		"multiple_choice_min": None,
		"multiple_choice_max": None,
		"number_of_winners": 1,
		"randomize_options": False,
		"require_voter_names": False,
		"results_visibility": "always",
		"use_custom_design": False
    }}
#Above is the json object. Most of it is taken directly from the github of strawpoll!

    
    dataBack = requests.post(url=PollAPI,json=makePoll,headers={'X-API-KEY': xapiKey})
    print(dataBack.json)
    