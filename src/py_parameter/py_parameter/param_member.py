import rclpy
from rclpy.node import Node

class Minimalparameter(rclpy.node.Node):
    def __init__(self):
        super().__init__('minimal_parameter_node')
        self.declare_parameter('my_parameter','world')
        self.timer =self.create_timer(1.0, self.call_back)


    def call_back(self):
        my_param= self.get_parameter('my_parameter').get_parameter_value().string_value
        self.get_logger().info('hello %s|' %my_param)
        my_new_param =rclpy.parameter.Parameter('my_parameter',rclpy.Parameter.Type.STRING,'world')
        all_new_parameters= [my_new_param]
        self.set_parameters(all_new_parameters)




def main():
    rclpy.init()
    node = Minimalparameter()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__=='__main__':
    main()            
