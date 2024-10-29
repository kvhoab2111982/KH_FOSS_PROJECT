from setuptools import setup, find_packages

setup(
    name="HausaMediaLab",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "moviepy",
        "pydub",
        "speech_recognition",
    ],
)
