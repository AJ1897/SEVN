from setuptools import setup

setup(
    name='hyrule_gym',
    version='1.0',
    install_requires=[
        'gym>=0.2.3', 'pybullet>=1.9.4', 'torch', 'scipy', "tqdm", "matplotlib", "numpy", "networkx"
    ])
