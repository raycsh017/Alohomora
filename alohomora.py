import re, sys, webbrowser, subprocess

if __name__ == "__main__":
	command = 'open http://google.com'
	subprocess.call(command.split())

	# Open the file with URLs
	srcFolder = 'src/'
	fileExt = '.txt'
	filename = srcFolder + str(sys.argv[1]) + fileExt
	f = open(filename, 'r')

	for link in f:
		# Use chrome browser
		chrome = webbrowser.get('chrome')

		# Check if protocol is specified for each link
		linkProtocol = re.search(r'(http://)|(https://)', link)
		if not linkProtocol:
			chrome.open('http://' + link)
		else:
			chrome.open(link)
