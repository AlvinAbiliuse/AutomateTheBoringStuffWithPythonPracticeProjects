
stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory(inventory):
	print('Inventory:')
	item_total = 0
	for k, v in inventory.items():
		print(str(v) + ' ' + k)
		item_total += v
		print('Total number of items: ' + str(item_total))

def addToInventory(inventory, addItems):
	for i in addItems:
		if i in inventory.items():
			inventory[i] = inventory[i] + 1
	
displayInventory(stuff)
print('')
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(stuff, dragonLoot)
displayInventory(inv)
