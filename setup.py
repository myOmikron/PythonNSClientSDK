import setuptools

with open("README.md") as f:
    long_description = f.read()

setuptools.setup(
    name="nsclient-sdk",
    version="0.0.1",
    author="Niklas Pfister",
    author_email="contact@omikron.pw",
    description="A SDK for python to communicate with the NSClient",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/myOmikron/PythonNSClientSDK",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        "wheel",
        "requests"
    ]
)
