#SECURITY NOTE: anything in here can be created simply by sending the 
# class name over the network.  This is a potential vulnerability
# I wouldn't suggest letting any of these classes DO anything, especially
# things like file system access, or allocating huge amounts of memory

class Event:
	"""this is a superclass for any events that might be generated by an
	object and sent to the EventManager"""
	def __init__(self):
		self.name = "Generic Event"

class TickEvent(Event):
	def __init__(self):
		self.name = "CPU Tick Event"

class QuitEvent(Event):
	def __init__(self):
		self.name = "Program Quit Event"

class MapBuiltEvent(Event):
	def __init__(self, map):
		self.name = "Map Finished Building Event"
		self.map = map

class GameStartRequest(Event):
	def __init__(self):
		self.name = "Game Start Request"

class GameStartedEvent(Event):
	def __init__(self, game):
		self.name = "Game Started Event"
		self.game = game

class CharactorMoveRequest(Event):
	def __init__(self, direction):
		self.name = "Charactor Move Request"
		self.direction = direction

class CharactorMoveEvent(Event):
	def __init__(self, charactor):
		self.name = "Charactor Move Event"
		self.charactor = charactor

class CharactorPlaceEvent(Event):
	"""this event occurs when a Charactor is *placed* in a sector, 
	ie it doesn't move there from an adjacent sector."""
	def __init__(self, charactor):
		self.name = "Charactor Placement Event"
		self.charactor = charactor

class ServerConnectEvent(Event):
	"""the client generates this when it detects that it has successfully
	connected to the server"""
	def __init__(self, serverReference):
		self.name = "Network Server Connection Event"
		self.server = serverReference

class ClientConnectEvent(Event):
	"""this event is generated by the Server whenever a client connects
	to it"""
	def __init__(self, client):
		self.name = "Network Client Connection Event"
		self.client = client

class MenuMultiPlayerEvent(Event):
	def __init__(self):
		self.name = "Multi Player Selected From Menu"

class RequestServerConnectEvent(Event):
	def __init__(self):
		self.name = "Connect to Remote Server"

class BothSidesConnectedEvent(Event):
	def __init__(self):
		self.name = "Controller and View Connected to Remote Server"

class ConnectFail(Event):
	def __init__(self, host):
		self.name = "Controller or View Failed Connected to Host"
		self.host = host
