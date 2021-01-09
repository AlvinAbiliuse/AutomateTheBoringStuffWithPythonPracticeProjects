def displayInventory(inventory):
	print('Inventory:')
	item_total = 0
	for k, v in inventory.items():
		print(str(v) + ' ' + k)
		item_total += v
	print('\nTotal number of items: ' + str(item_total))

def addToInventory(inventory, addItems):
	tech = inventory
	for i in addItems:
		if i in tech.items():
			tech[i] = tech[i] + 1
		else:
			tech[i] = 1
	print(tech)
	return tech
	
inv = {'gold coin': 42, 'rope': 1}
displayInventory(inv)
print('')
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)
