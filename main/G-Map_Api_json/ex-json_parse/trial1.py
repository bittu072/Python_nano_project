import json

data = '''{
	"name" : "web developer",
	"phone" : {
		"type" : "international",
		"number" : "1234567890"
		},
	"email" : {
		"hide" : "yes"
		}
	}'''

info = json.loads(data)  ####this is the deserialize step
print 'Name:', info["name"]
print 'Hide:',info["email"]["hide"]
