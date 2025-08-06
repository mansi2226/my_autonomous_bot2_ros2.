import rclpy 
from rclpy.node import Node
from std_msgs.msg import String


class Minimalpublisher(Node):

    def __init__(self):
        super().__init__('minimal_publisher')
        self.pub_ =self.create_publisher(String ,'topic', 10)
        self.time =self.create_timer(0.5, self.call_back)
        self.i=0

    def call_back(self):
        msg=  String()
        msg.data= 'hello_world:%d' %self.i
        self.pub_.publish(msg)
        self.get_logger().info('publishig:%s''' % msg.data) 
        self.i += 1 



def main(args =None):
    rclpy.init(args =args) 
    minimal_publisher =Minimalpublisher()
    rclpy.spin(minimal_publisher)
    minimal_publisher.destroy_node() 
    rclpy.shutdown()



if __name__ =='__main__':
    main()         