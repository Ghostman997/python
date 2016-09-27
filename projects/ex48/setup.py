try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
        'description': 'My Projects',
        'author': 'Dima',
        'url': 'URL to get it at',
        'download_url': 'Where to download it.',
        'author_email': 'dmchernyy97@gmail.com',
        'versin': '0.1',
        'install_requires': ['nose'],
        'packages': ['lexicon'],
        'scripts': [],
        'name':'projectname'
    }

setup(**config)
