from setuptools import find_packages, setup

package_name = 'pothole'

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
    maintainer='arunabh',
    maintainer_email='arunabh@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'object_detector = pothole.object_detector:main',
            'mover = pothole.mover:main',
            'test = pothole.test:main',
            'mover2 = pothole.mover2:main',
            'test00 = pothole.test00:main',
            'grid = pothole.grid:main',
            'yolo = pothole.yolo:main',
            'movnav = pothole.movnav:main'
        ],
    },
)
