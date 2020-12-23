from selenium import webdriver

browser = webdriver.Firefox(executable_path = '/home/alvin/Downloads/geckodriver')
browser.get('http://inventwithpython.com')
try:
	elem = browser.find_element_by_class_name('bookcover')
	print(f'Found {elem.tag_name} element with that class name!')
except:
	print('Was not able to find an element with that name.')
