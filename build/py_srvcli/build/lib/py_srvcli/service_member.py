from example_interfaces.srv import AddTwoInts
import rclpy 
from rclpy.node import Node

class Minimalservice(Node):
    def __init__(self):
        super().__init__('minimalservice')
        self.srv_ = self.create_service(AddTwoInts,'add_two_ints', self.add_two_ints_callback)


    def add_two_ints_callback(self, request, response):
        response.sum =request.a +request.b 
        self.get_logger().info('incoming request\na:%d b: %d' %(request.a, request.b))
        return response  






def main():
    rclpy.init()
    minimal_service =Minimalservice()
    rclpy.spin(minimal_service)
    rclpy.shutdown()



if __name__=='__main__':
    main()