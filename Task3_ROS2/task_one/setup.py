from setuptools import find_packages, setup

package_name = 'task_one'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='tanmayee000',
    maintainer_email='tanmayee000@todo.todo',
    description='TODO: Package description',
    license='Apache-2.0',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'wheel_publisher = task_one.wheel_publisher:main',
            'speed_subscriber = task_one.speed_subscriber:main',
        ],
    },
)
