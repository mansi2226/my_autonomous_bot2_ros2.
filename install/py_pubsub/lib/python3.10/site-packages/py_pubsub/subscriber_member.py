import rclpy
from rclpy.node import Node 
from std_msgs.msg import String

class Minimalsuscriber(Node):
    def __init__(self):
        super().__init__('minimal_subsriber')
        self.sub_ = self.create_subscription(String, 'topic', self.call_lishner,10)
        

    def call_lishner(self, msg):
        self.get_logger().info('i heard:"%s"' % msg.data)




def main(args =None):
    rclpy.init(args=args)
    minimal_suscriber =Minimalsuscriber()
    rclpy.spin(minimal_suscriber)
    rclpy.shutdown()


if __name__ =='__main__' :
   main()   