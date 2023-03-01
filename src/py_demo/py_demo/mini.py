import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class MyNode(Node):
    def __init__(self):
        node_name="minimal"
        super().__init__(node_name)
        self.pub = self.create_publisher(String, "/my_topic", 10)
        self.create_timer(1, self.__timer_handler)
        self.get_logger().info("Hello ROS2")

    def __timer_handler(self):
        msg = String()
        msg.data = "hello"
        self.get_logger().info("publish")
        self.pub.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = MyNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()