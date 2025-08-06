import sys 
from example_interfaces.srv import AddTwoInts
import rclpy 
from rclpy.node import Node

class Minimalclient(Node):
    def __init__(self):
        super().__init__('minimal_clinet')
        self.cli_ =self.create_client(AddTwoInts,'add_two_ints')
        while not self.cli_.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('sevice not available')
        self.req = AddTwoInts.Request()

    def send_request(self,a,b):
        self.req.a =a
        self.req.b =b
        self.future =self.cli_.call_async(self.req)
        rclpy.spin_until_future_complete(self ,self.future)
        return self.future.result()





def main():
    rclpy.init()
    minimal_client= Minimalclient()
    response =minimal_client.send_request(int(sys.argv[1]), int(sys.argv[2]))
    minimal_client.get_logger().info('result Of two_adds :for %d + %d = %d' %(int(sys.argv[1]), int(sys.argv[2]), response.sum))
    minimal_client.destroy_node()
    rclpy.shutdown()



if __name__=='__main__':
    main()