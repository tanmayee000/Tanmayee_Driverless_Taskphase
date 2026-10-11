import rclpy
from rclpy.node import Node
from task_interfaces.msg import RT2String


class StringPublisher(Node):

    def __init__(self):
        super().__init__('string_publisher')
        self.publisher_ = self.create_publisher(RT2String, '/rt2string', 10)

    def publish_string(self, text):
        msg = RT2String()
        msg.data = text
        self.publisher_.publish(msg)
        self.get_logger().info(f'Published: "{text}"')


def main(args=None):
    rclpy.init(args=args)
    node = StringPublisher()
    try:
        while rclpy.ok():
            text = input('Enter a string: ').strip()
            if not text:
                print('Please type something.')
                continue
            node.publish_string(text)
    except (KeyboardInterrupt, EOFError):
        pass
    finally:
        node.destroy_node()
        if rclpy.ok():
            rclpy.shutdown()


if __name__ == '__main__':
    main()
