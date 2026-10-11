import rclpy
from rclpy.node import Node
from task_interfaces.msg import TaskOne


class WheelPublisher(Node):

    def __init__(self):
        super().__init__('wheel_publisher')
        self.publisher_ = self.create_publisher(TaskOne, '/taskone', 10)

    def publish_wheel_data(self, ang_vel, radius):
        msg = TaskOne()
        msg.ang_vel = ang_vel
        msg.radius = radius
        self.publisher_.publish(msg)
        self.get_logger().info(
            f'Published: angular velocity = {ang_vel} rad/s, radius = {radius} m')


def main(args=None):
    rclpy.init(args=args)
    node = WheelPublisher()
    try:
        while rclpy.ok():
            try:
                ang_vel = float(input('Enter angular velocity (rad/s): '))
                radius = float(input('Enter wheel radius (m): '))
            except ValueError:
                print('Please enter numbers only.')
                continue
            if radius < 0:
                print('Radius cannot be negative.')
                continue
            node.publish_wheel_data(ang_vel, radius)
    except (KeyboardInterrupt, EOFError):
        pass
    finally:
        node.destroy_node()
        if rclpy.ok():
            rclpy.shutdown()


if __name__ == '__main__':
    main()
