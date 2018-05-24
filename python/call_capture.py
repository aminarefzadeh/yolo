from capture_thread import Capture
import cv2
import time
import numpy as np

CaptureThread = Capture()


if __name__ == '__main__':
	try :
			if not CaptureThread.isAlive() :
				CaptureThread.start()
				time.sleep(1)

			while(True):
				valid , color_image = CaptureThread.get_frame()
				if valid :
					cv2.imshow('Align Example', color_image)
					#cv2.imshow('depth_image ' , depth_image)
					cv2.waitKey(1)
				else :
					print("not valid ")
			CaptureThread.stop()
				
	except KeyboardInterrupt:
		CaptureThread.stop()

	except :
		pass


CaptureThread.join()


