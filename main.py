## the main project entrance

import cv2 
import threading 
import time 
import queue as Q 


# Section 1. Image acquisition from laptop camera (id=0), typical I/O, typical thread issue

class Camera(threading.Thread):
	def __init__(self, video, resize_factor=1.0):
		self.video = video 
		self.frame = None
		self.resize_factor = resize_factor 
		super(Camera, self).__init__() 

	def get_image(self):
		if self.video.isOpened():
			ret, frame = video.read()
			if ret is True:
				self.frame = cv2.resize(frame, None, fx=self.resize_factor, fy=self.resize_factor, interpolation=cv2.INTER_AREA) 
				self.run()

	def run(self):
		self.get_image()
	
	def get_frame(self):
		return self.frame 

video = cv2.VideoCapture(0,)
cam = Camera(video, 0.5)
cam.start()

while True:
	frame = cam.get_frame()
	if frame is not None:
		cv2.imshow('F', frame)

	if cv2.waitKey(20) & 0xFF == ord('q'):
		break

video.release()
cv2.destroyAllWindows()







# Section 2. Object recognition, CPU intensitive.



# Section 3. Image edit and display. CPU intensitive.