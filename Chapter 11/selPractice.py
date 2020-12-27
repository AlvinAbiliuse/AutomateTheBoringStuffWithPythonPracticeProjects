from selenium import webdriver

browser = webdriver.Firefox(executable_path = './geckodriver')
browser.get('http://inventwithpython.com')
linkElem = browser.find_element_by_link_text('Available in November 2020, but you can use discount code PREORDER for 25% off.')
linkElem.click()



#try:
#	elem = browser.find_element_by_class_name('bookcover')
#	print(f'Found {elem.tag_name} element with that class name!')
#except:
#	print('Was not able to find an element with that name.')
