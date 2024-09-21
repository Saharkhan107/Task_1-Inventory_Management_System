#Course: CIS 103
#Instructor: Md Ali
#Student: Sahar Iqbal
#Date: 09/20/2024

# Task: 01 Inventory Management System:

# Creates a list called `inventory` with specified items
inventory = ['sword', 'shield', 'potion', 'bow', 'arrow', 'helmet'] 
print(inventory)

# The player finds a `'magic ring'`. Now we add it to the inventory list
inventory.append('magic ring')

# During battle, the `'potion'` is consumed. Now we remove it from the inventory
inventory.remove('potion')

# The player upgrades their `'bow'` to a `'crossbow'`. We need to replace `'bow'` with `'crossbow'` in the list
inventory[inventory.index('bow')] = 'crossbow'

# Print the updated inventory list
print("Updated inventory:", inventory)

#The player wants to sort their inventory alphabetically. we need to sort the list.
inventory.sort()
print("Sorted Inventory_list:", inventory)

# The player is now carrying too much and wants to discard the first item on the list.
# Remove the first item on the list
inventory.pop(0)
print("After removing first item:", inventory)



