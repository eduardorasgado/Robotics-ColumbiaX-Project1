#!usr/bin/env python
import rospy
from std_msgs.msg import String
from TwoInts.msg import 

def publisherRospy():
	publisher1 = rospy.Publisher('two_ints', String,queue_Size=0)
	rospy.init_node('publisher', anonymous=True)

	sleepness = rospy.Rate(1)

	while not rospy.is_shutdown():
		publisher1.publish()
		sleepness.sleep()

#For the subscriber we need a callback
def rospyCallback():
	pass
def subscriberRospy():
	rospy.init_node('subscriber',String, callback)
	rospy.Subscriber('two_ints')
	rospy.spin()

if __name__ == '__main__':
	try:
		subscriberRospy()

	except Exception as e:
		pass
	finally:
		print("Something went wrong")
