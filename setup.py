from src.VERSION import VERSION as version
from setuptools  import setup




with open('README.md') as f:
    a = f.read()

# with open('VERSION.txt') as f:
#     version = f.read()

with open('requirements.txt') as f:
    requirements = f.read().split('\n')
    requirements = [i for i in requirements if i]


# This section remove the video, because its not supported in PyPi
text      = '<br>\n\nhttps://user-images.githubusercontent.com/79649185/182558272-255becc8-1dcc-45b5-99ef-22e0596cf490.mp4'
long_desc = a.replace(text, '')





setup(
    name = 'markify',
    version = version,
    description = 'Markify is a command line application written in python which scrapes data from your social media(s) (ie reddit, discord, and twitter for now) and generates new setences based on them using markov chains. For more information, please visit https://github.com/msr8/markify',
    # py_modules=['mvp_msr8'],
    long_description = long_desc,
    long_description_content_type = 'text/markdown',
    platforms = ["Windows", "Linux", "Solaris", "Mac OS-X", "Unix"],
    install_requires = requirements,
    package_dir = {'': 'src'},
    entry_points = {
        'console_scripts': [
            'markify = markify:init_main',
        ]
    },
    project_urls={
        'Bug Tracker': 'https://github.com/msr8/markify/issues',
        'Source Code': 'https://github.com/msr8/markify',
    },
    classifiers = [
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Operating System :: Unix',
        'Operating System :: MacOS'
    ]
)








'''
name:        what you will pip install, not import
py_modules:  what they will import

!! NAME OF THE MAIN FILE IN THE src DIR SHOULD BE SAME AS PACKAGE NAME
'''


