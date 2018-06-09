#!usr/bin/env python
import rospy
#type of message to publish
from std_msgs.msg import Int16
#message to subscribe
from project1.msg import TwoInts

result=0;

def callback(msg):
	num1 = msg.a
	num2 = msg.b
	result = num1 + num2

	#now lets publish
	resultFromSum = Int16()
	resultFromSum.data = result
	publisher.publish

def main():
	#initialize the node
	rospy.init_node('two_ints_publisher_node')

	#create a publisher
	#the topic, the message type, queue
	publisher = rospy.Publisher('sum', Int16, queue_size=0)

	#create a subscriber
	#topic
	subscriber = rospy.Subscriber('two_ints', TwoInts, callback)

	#let it rip
	rospy.spin()

if __name__ == '__main__':
	try:
		main()

	except Exception as e:
		pass
	finally:
		print("Something went wrong")
