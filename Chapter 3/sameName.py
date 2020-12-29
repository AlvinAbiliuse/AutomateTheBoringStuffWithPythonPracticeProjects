def spam():
	eggs = 'spam local'
	print(eggs)	# prints 'spam local'

def bacon():
	eggs = 'bacon local'
	print(eggs)	# prints 'bacon local'
	spam()
	print(eggs)	# prints 'bacon local'

egs = 'global'
bacon()
print(eggs)
