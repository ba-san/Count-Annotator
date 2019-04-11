import cv2

class mouseParam:
	def __init__(self, input_img_name):
		#parameters for inputting
		self.mouseEvent = {"X":None, "y":None, "event":None, "flags":None}
		#setting for input
		cv2.setMouseCallback(input_img_name, self.__CallBackFunc, None)
		
		
	def __CallBackFunc(self, eventType, x, y, flags, userdata):
		
		self.mouseEvent["x"]= x 
		self.mouseEvent["y"] = y
		self.mouseEvent["event"] = eventType    
		self.mouseEvent["flags"] = flags
		     
	def getData(self):
		return self.mouseEvent
		
	def getEvent(self):
		return self.mouseEvent["event"]
		
	def getFlags(self):
		return self.mouseEvent["flags"]
		
	def getX(self):
		return self.mouseEvent["x"]
			
	def getY(self):
		return self.mouseEvent["y"]
		
	def getPos(self):
		return (self.mouseEvent["x"], self.mouseEvent["y"])
				
