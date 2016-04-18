import json
import urllib2


url = 'http://localhost:9200/topbeat-*/_search?pretty'
response = urllib2.urlopen(url)
html = response.read()

rObj = json.loads(html)

ProcessObjs = rObj["hits"]["hits"]

print "The various processes are - \n "

count = 0

for ProcessObj in ProcessObjs:
	infoObj = ProcessObj["_source"]["proc"]
	name=infoObj["name"]
	pid=infoObj["pid"]
	state=infoObj["state"]
	user_p=infoObj["cpu"]["user_p"]*100
	resident_set_size=infoObj["mem"]["rss"]
	total_memory_size=infoObj["mem"]["size"]

	count+=1

	print str(count) + ". "+ name + " with process id " + str(pid) + " currently " + state + "."
	print "Percentage CPU time - " + str(user_p)
	print "Resident Set Size - " + str(resident_set_size)
	print "Total virtual memory taken - " + str(total_memory_size) 

