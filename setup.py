#from distutils.core import setup
import setuptools

setuptools.setup(
        name = 'p5250',
        packages = ['p5250'],
        version = '0.1.0',
        description = 'Python library to communicate with IBM i hosts, based on the 5250 protocol. For example AS400.',
        author = 'Simon Faltum',
        url = 'https://github.com/simonfaltum/p5250',
        long_description = '''
    A Python library that provides an interface to communicate with IBM hosts: send commands and text, receive output (screens). 
    The library is built on a 3270 emulator, but adapted for the 5250 protocol used by AS400 and IBM i.

    The library is highly customizable and is built with simplicity in mind.
    It is written in Python 3, runs on Linux and Unix-like Operating Systems, and relies on the `s3270` utility. So it is required to have the `s3270` installed on your system and available on your PATH.

    The library allows you to open a telnet connection to an IBM host, and execute a set of instructions as you specified them in your python program.
    ''',
        keywords = 'IBM AS400 IBMi TN5250 Mainframe ',
        classifiers = [
            'Intended Audience :: Developers',
            'Programming Language :: Python',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3 :: Only',
            'Operating System :: Unix',
            'Operating System :: POSIX :: Linux',
            'Topic :: Software Development :: Testing',
            'Topic :: Software Development :: Libraries :: Python Modules',
            'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
            'Development Status :: 4 - Beta'
        ]
)
