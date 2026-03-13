import setuptools

import os

def package_files(directory):
    paths = []
    for (path, directories, filenames) in os.walk(directory):
        for filename in filenames:
            paths.append(os.path.join('..', path, filename))
    return paths

extra_files = package_files('hpacker')

setuptools.setup(
    name='hpacker',
    version='0.1.0',
    author='Gian Marco Visani',
    author_email='gvisan01@cs.washington.edu',
    description='Holographic Rotationally Equivariant Convolutional Neural Network for Protein Side-Chain Packing',
    long_description=open("README.md", "r").read(),
    long_description_content_type='text/markdown',
    url='https://github.com/gvisani/hpacker',
    python_requires='>=3.9',
    package_data={'': extra_files},

    # package_data={'hpacker': ['hpacker/src/preprocessing/*',
    #                           "src/pretrained_models/*",
    #                           "psrc/retrained_models/initial_guess/*",
    #                           "psrc/retrained_models/initial_guess_conditioned/*",
    #                           "src/pretrained_models/refinement/*",
    #                           "sidechain_reconstrution/*",
    #                           "sidechain_reconstrution/biopython_internal_coords/*",
    #                           "sidechain_reconstrution/biopython_internal_coords/plots/*",
    #                           "sidechain_reconstrution/manual/*",
    #                           "preprocessing/utils",
    #                           ]},

    install_requires=[
        'biopython',
        "torch",
        "tqdm",
        "progress"
        "h5py",
        "hdf5plugin",
        "sqlitedict",
        "e3nn"
    ],
    packages=setuptools.find_packages(),
)