import json

input = '''[
	{ "id" : "01",
	  "x" : "72",
	  "name" : "web developer"
	},
	{ "id" : "02",
	  "x" : "7",
	  "name" : "full-stack developer"
	}
	]'''

info = json.loads(input)  ####this is the deserialize step
print "user count: ", len(info), "\n"

##print "name", info[0], "\n"
for item in info:
	print 'Name:', item["name"]
	print 'Id:',item['id']
	print 'Attribute', item["x"]
	print '\n'
