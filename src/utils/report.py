def save(data):
	file = open("report.html", "a")
	file.write('<h2>' + data + '</h2>')
	file.close()
