# -*- coding: utf-8 -*-
from setuptools import setup

setup(
    name='pyzk',
    version='0.9.3.5',
    description='an unofficial library of zksoftware fingerprint device for python 3.5',
    url='https://github.com/fananimi/pyzk',
    author='Mahmoud Abdel Latif',
    author_email='mah008@me.com',
    license='LICENSE.txt',
    packages=['zk'],
    keywords=[
        'zk',
        'pyzk',
        'zksoftware',
        'attendance machine',
        'fingerprint',
        'biometrics',
        'security'
    ],
    install_requires=['future'],
    zip_safe=False
)
