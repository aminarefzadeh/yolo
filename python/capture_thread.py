from  threading import Thread
from threading import Lock
import pyrealsense2 as rs
import numpy as np
import cv2
import sys 


class Capture(Thread) :
	def __init__ (self) :
		Thread.__init__(self)
		self.depth_image = None
		self.color_image = None
		self.lock = True 
		self.pipeline = rs.pipeline()
		self.config = rs.config()
		self.config.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)
		self.config.enable_stream(rs.stream.depth, 640, 360, rs.format.z16, 30)



	def run(self):
		profile = self.pipeline.start(self.config)

		depth_sensor = profile.get_device().first_depth_sensor()
		depth_scale = depth_sensor.get_depth_scale()
		# print ("Depth Scale is: " , depth_scale)

		# clipping_distance_in_meters = 1 #1 meter
		# clipping_distance = clipping_distance_in_meters / depth_scale

		align_to = rs.stream.color
		align = rs.align(align_to)

		try:
			while True:
				frames = self.pipeline.wait_for_frames()
				
				#aligned_frames = align.process(frames)
				
				#aligned_depth_frame = aligned_frames.get_depth_frame()
				#color_frame = aligned_frames.get_color_frame()
				
				# Validate that both frames are valid
				#if not aligned_depth_frame or not color_frame:
					#continue
				color_frame = frames.get_color_frame()
				self.lock = True
				self.color_image = np.asanyarray(color_frame.get_data())
				#self.depth_image = np.asanyarray(aligned_depth_frame.get_data())
				self.lock = False
# 				cv2.imshow('Align Example', self.color_image)
# 				cv2.imshow('Align Example2', self.depth_image)

# 				cv2.waitKey(1)
				
		except:
			pass
				
	def stop(self):
		self.run = False
		self.pipeline.stop()

	def get_frame(self) :
		if (self.lock == True) :
			return False , None
		else :
			return True , self.color_image

# Capturet = Capture()
# Capturet.start()
# Capturet.join()





