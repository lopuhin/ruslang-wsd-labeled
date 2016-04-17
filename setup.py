from setuptools import setup


setup(
    name='rl_wsd_labeled',
    packages=['rl_wsd_labeled'],
    zip_safe=False,
    package_data={
        'rl_wsd_labeled': [
            'verbs/*/*.txt',
            'nouns/*/*.txt',
        ],
    },
)
