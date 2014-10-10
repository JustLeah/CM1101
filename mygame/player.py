from items import *
from map import rooms

inventory = []
equipped = {}
equipped = {
	"head": "none", 
	"chest": "none", 
	"shield": "none", 
	"weapon": "none"
}

current_mass = 0

# Start game at the reception
current_room = rooms["Dark Cabin"]
