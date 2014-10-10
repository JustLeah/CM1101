#Item stats are in this order ARMOR, ATTACK, HEALTH
item_rusty_sword = {
    "id": "rusty sword",
    "name": "Rusty Sword",
    "equipable" : True,
    "stats": [0, 2, 0],  
    "slot" : "weapon",
    "description":
    """This rusty sword would struggle to cut through cheese, even warm cheese"""
}

item_rusty_axe = {
    "id": "rusty axe",
    "name": "Rusty Axe",
    "equipable" : True,
    "stats": [0, 2, 0],  
    "slot" : "weapon",
    "description":
    """This axe is rusty and hits like a wet noodle."""
}

item_wooden_shield = {
    "id": "wooden shield",
    "name": "Wooden Shield",
    "equipable" : True,
    "stats": [2, 0, 0],  
    "slot" : "shield",
    "description":
    "It has seen better days. At least it has a WiFi card!"
}


#Adding a dictionary for all the items 
all_items = {
    "rusty sword": item_rusty_sword,
    "rusty axe": item_rusty_axe,
    "wooden shield": item_wooden_shield
}
