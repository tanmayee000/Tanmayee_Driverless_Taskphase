import rclpy
from rclpy.node import Node
from task_interfaces.srv import PalindromeResult


class PalindromeResponder(Node):

    def __init__(self):
        super().__init__('palindrome_responder')
        self.service = self.create_service(
            PalindromeResult, '/palindrome_result', self.handle_request)
        self.get_logger().info('Ready: waiting for results from Node 2...')

    def handle_request(self, request, response):
        response.answer = 'Yes' if request.is_palindrome == 1 else 'No'
        self.get_logger().info(
            f'Received {request.is_palindrome} -> replying "{response.answer}"')
        return response


def main(args=None):
    rclpy.init(args=args)
    node = PalindromeResponder()
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
