"""
def list_songs(**songs):
    print(songs)
    print("Type is ", type(songs))

#list_songs()
# {}
# Type is  <class 'dict'>

list_songs(adele_songs = ["Hello", "Someone like you"], backstreet_boys_songs = ["Larger than life", "I want it that way"])
# {'adele_songs': ['Hello', 'Someone like you'], 'backstreet_boys_songs': ['Larger than life', 'I want it that way']}
# Type is  <class 'dict'>


class Agent:
    
    def __init__(self, agent_attributes):
    	for atr_name, atr_value in agent_attributes.items():
    		setattr(self,atr_name,atr_value)
        #self.agreeableness = agent_attributes['agreeableness']

agent_attributes = {"neuroticism": -0.0739192627121713, "language": "Shona", "latitude": -19.922097800281783, "country_tld": "zw", "age": 12, "income": 333, "longitude": 29.798455535838603, "sex": "Male", "religion": "syncretic", "extraversion": 1.051833688742943, "date_of_birth": "2005-01-10", "agreeableness": 0.1441229877537559, "id_str": "LB3-3Cl", "conscientiousness": 0.2419104411765549, "internet": "false", "country_name": "Zimbabwe", "openness": -0.024607605122172617, "id": 6636726630}

first_agent = Agent(agent_attributes)
print(first_agent.agreeableness

import os
import sys
if os.path.exists("bems.py"):
	print("le fichier existe")
else:
	sys.exit("fichier absent")
"""





