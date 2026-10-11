import rclpy
from rclpy.node import Node
from task_interfaces.msg import RT2String
from task_interfaces.srv import PalindromeResult


class PalindromeChecker(Node):

    def __init__(self):
        super().__init__('palindrome_checker')
        self.subscription = self.create_subscription(
            RT2String, '/rt2string', self.listener_callback, 10)
        self.client = self.create_client(PalindromeResult, '/palindrome_result')

    def listener_callback(self, msg):
        text = msg.data
        cleaned = text.replace(' ', '').lower()
        result = 1 if cleaned == cleaned[::-1] else 0
        self.get_logger().info(f'Received "{text}" -> palindrome check = {result}')
        if not self.client.service_is_ready():
            self.get_logger().warn('Node 3 is not running yet, cannot send result.')
            return
        request = PalindromeResult.Request()
        request.is_palindrome = result
        future = self.client.call_async(request)
        future.add_done_callback(
            lambda f, t=text: self.response_callback(f, t))

    def response_callback(self, future, text):
        response = future.result()
        self.get_logger().info(
            f'Is "{text}" a palindrome? Node 3 says: {response.answer}')


def main(args=None):
    rclpy.init(args=args)
    node = PalindromeChecker()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        if rclpy.ok():
            rclpy.shutdown()


if __name__ == '__main__':
    main()
