from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='mapsynth',
    version='0.0.1',
    description='MAPLab sound synthesizer',
    author='Loonan Chauvette',
    author_email='loonan.chauvette@gmail.com',
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='MIT License',
    py_modules=['hello'],
    package_dir={'': 'mapsynth'},
    install_requires=[
        'numpy',
        'matplotlib',
    ],
    extras_require={
        "dev": ["pytest>=7"]
    },
    classifiers=["License :: OSI Approved :: MIT License",
                 "Operating System :: OS Independent",
                 "Programming Language :: Python :: 3",
                 "Programming Language :: Python :: 3.10",
                 "Topic :: Multimedia :: Sound/Audio :: Sound Synthesis",
                 "Development Status :: 1 - Planning",
                 "Intended Audience :: Science/Research",
                 "Natural Language :: English"]
)
