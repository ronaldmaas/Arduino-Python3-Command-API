import setuptools

with open("README.md", "r") as fh:
  long_description = fh.read()

setuptools.setup(
  name="arduino-python3",
  version="0.2",
  install_requires=['pyserial'],
  author="Morten Kals",
  author_email="morten@kals.no",
  description="A light-weight Python library that provides a serial \
  bridge for communicating with Arduino microcontroller boards. Extended to work with Python 3",
  long_description=long_description,
  long_description_content_type="text/markdown",
  url='https://github.com/mkals/Python-Arduino-Command-API',
  packages=['Arduino'],
  license='MIT',
)
