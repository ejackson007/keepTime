#file to make app freestanding
from setuptools import setup

APP = ['keeper.py']
DATA_FILES = []
OPTIONS = {
    'argv_emulation': True,
    'iconfile': 'clock.icns',
    'plist': {
        'LSUIElement': True,
    },
    'packages': ['rumps', 'datetime'],
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)