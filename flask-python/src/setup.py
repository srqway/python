from setuptools import setup

setup(
    name='flask-python',
    packages=['flaskpython.view'],
    include_package_data=True,
    install_requires=[
        'flask',
    ],
)