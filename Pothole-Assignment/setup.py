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
            'real_object_detector = pothole.real_object_detector:main',
            'mover = pothole.mover:main',
            'analysis = pothole.analysis:main',
            'test = pothole.test:main',
            'magenta_pothole = pothole.magenta_pothole:main',
            'test2 = pothole.test2:main'
            
            
        ],
    },
)
