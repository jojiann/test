from setuptools import setup, find_packages

setup(
    name="nexa",  # Replace with your package name
    version="0.1.0",  # Initial version
    author="Muhannad Marwan",
    author_email="marwan.hashmi@onsor.om",
    description="A package as a workflow for EDF files to be transformed to STFT or wavelets, build a Keras model then quantize it then convert it to an Akida model",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(include=["nexa", "nexa.*"]),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.9",
    install_requires=[
        "numpy",
        "pandas",
        "scipy",
        "PyWavelets",
        "mne",
        "tensorflow",
        "keras",
        "matplotlib",
        "scikit-learn",  # sklearn's package name for pip is scikit-learn
        "seaborn",
        "cnn2snn",
    ],
    extras_require={
        # Add optional dependencies here if needed
    },
    entry_points={
        'console_scripts': [
            'main-script=main:main',  # Makes `main-script` command run main.py
            'train-script=main_training:main',  # Makes `train-script` command run main_training.py
        ],
    },
    include_package_data=True,  # Include non-code files specified in MANIFEST.in
)