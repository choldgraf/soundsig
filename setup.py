from distutils.core import setup

setup(
    name='soundsig',
    version='0.5',
    packages=['soundsig',],
    license='',
    long_description=open('README.md').read(),
    install_requires=['numpy',
                      'scipy',
                      'matplotlib',
                      'tables',
                      'h5py',
                      'mne',
                      'nitime',
                      'pandas',
                      # weave  PYTHON 2.7
                      # brian  PYTHON 2.7
        ]
)
