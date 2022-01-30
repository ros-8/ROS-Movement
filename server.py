import rospy
from std_msgs.msg import String
from pynput import keyboard
from pynput.keyboard import Listener


#defined pressed keynumbers
#keyCodeNum = [87,65,83,68,49,50,51,52,53,75] #w,a,s,d,1,2,3,4,5,k(kill the connection between client and server)
keyCodeNum = {87: 'w', 65: 'a', 83: 's', 68: 'd'}

global pub
global rate
def talkera():
	global pub
	global rate
	pub = rospy.Publisher('chatter', String, queue_size = 10)
	rospy.init_node('talker', anonymous = True)
	rate = rospy.Rate(10)

def talker(pressed_key):
	while not rospy.is_shutdown():
		hello_str = "hello world %s" % rospy.get_time()
		#rospy.loginfo(hello_str)
		passed = "Key pressed: " + str(pressed_key)
		#pub.publish(hello_str)
		pub.publish(passed)
		a()
		rate.sleep()

def on_press(key):
	pressed_key = key.char    #get the pressed key int value
	talker(pressed_key)
    
def a():
	with Listener(on_press=on_press) as listener: 
    		listener.join()

if __name__ == '__main__':
	try:
		talkera()
		a()
	except rospy.ROSInterruptException:
		print("error")
		pass