#!/usr/bin/env python3 

# newMessage() is called by a Client object when a new message is received from its associated IMClient
# updateConnected() will broadcast messages stored inside the messageQueue to the list of
# connectedClients when a new entry in ther queue is detected
from Client import Client
class ChatRoom:
	
	def __init__(self):
		self.name = ""
		self.clientsConnected = []
		self.messageQueue = []

	def newClient(self, newClient):
		self.clientsConnected.append(newClient)
		raise NotImplementedError

	def newMessage(self, messageIn, clientName);
		self.messageQueue.append(messageIn)
		return 
	
	def updateConnectedClients(self, messageIn):
		for client in clientsConnected:
			client.sendMessageUpdate(messageIn)
		return
	
	def mainLoop():
		raise NotImplementedError