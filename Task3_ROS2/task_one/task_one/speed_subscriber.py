import rclpy
from rclpy.node import Node
from task_interfaces.msg import TaskOne


class SpeedSubscriber(Node):

    def __init__(self):
        super().__init__('speed_subscriber')
        self.subscription = self.create_subscription(
            TaskOne, '/taskone', self.listener_callback, 10)

    def listener_callback(self, msg):
        speed = msg.ang_vel * msg.radius
        self.get_logger().info(
            f'Received w = {msg.ang_vel} rad/s, r = {msg.radius} m '
            f'-> longitudinal speed v = w x r = {speed:.3f} m/s')


def main(args=None):
    rclpy.init(args=args)
    node = SpeedSubscriber()
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
