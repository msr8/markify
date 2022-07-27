from src.VERSION import VERSION as version
from setuptools import setup




with open('README.md') as f:
    long_desc = f.read()

# with open('VERSION.txt') as f:
#     version = f.read()

with open('requirements.txt') as f:
    requirements = f.read().split('\n')
    requirements = [i for i in requirements if i]

setup(
    name = 'markify',
    version = version,
    description = 'Markify is a command line application written in python which scrapes data from your social media(s) (ie reddit, discord, and twitter for now) and generates new setences based on them using markov chains. For more information, please visit https://github.com/msr8/markify',
    # py_modules=['mvp_msr8'],
    long_description=long_desc,
    long_description_content_type='text/markdown',
    install_requires = requirements,
    package_dir = {'': 'src'},
    entry_points = {
        'console_scripts': [
            'markify = markify:init_main',
        ]
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent'
    ]
)








'''
name:        what you will pip install, not import
py_modules:  what they will import

!! NAME OF THE MAIN FILE IN THE src DIR SHOULD BE SAME AS PACKAGE NAME
'''


