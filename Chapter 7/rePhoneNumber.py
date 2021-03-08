import re

phoneNumRegex = re.compile(r'\d{3}-\d{3}-\d{3}')
text = '415-555-4242'

result = phoneNumRegex.search(text)
print(f'Phone Number Found: {result.group()}')
