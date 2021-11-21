
from distutils.core import setup

setup(name='pimage',
      version='0.1',
      description='Create and manage Raspberry PI images',
      author='Antonio Serrano Hernandez',
      author_email='toni.serranoh@gmail.com',
      scripts=['src/pimage'],
      data_files=[('share/pimage/qemu',
            ['files/qemu/qemu-arm'])],
     )

