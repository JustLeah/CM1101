from items import *
from map import rooms
inventory = []
equipped = {
	"head": "none", 
	"chest": "none", 
	"shield": "none", 
	"weapon": "none"
}

stats = {
	"health": 10,
	"attack": 0,
	"armor": 0
}

#Start game at the reception
current_room = rooms["Dark Cabin"]
