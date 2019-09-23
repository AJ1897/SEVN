from setuptools import setup

setup(
    name='SEVN_gym',
    version='1.0',
    install_requires=[
        'gym>=0.2.3', 'pybullet>=1.9.4', 'scipy', 'pandas', 'tqdm',
        'matplotlib', 'numpy', 'networkx', 'pygame', 'h5py', 'tables',
        'dask[complete]', 'academictorrents', 'enum34', 'comet_ml'
    ])
