import webbrowser
import sys
import pyperclip

def mapOpen():
	if len(sys.argv) > 1:
		address = ' '.join(sys.argv[1:])
	else:
		address = pyperclip.paste()
	webbrowser.open('google.com/maps/search/' + str(address))

if __name__ == "__main__":
	mapOpen()
