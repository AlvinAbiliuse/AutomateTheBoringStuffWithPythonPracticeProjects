import webbrowser
import sys

def mapOpen():
	search = 'google.com/maps/search/' + ' '.join(sys.argv[1:])
	webbrowser.open(search)

if __name__ == "__main__":
	if len(sys.argv) > 1:
		mapOpen()
