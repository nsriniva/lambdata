import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="lambdata-nsriniva", # Replace with your own username
    version="0.0.5",
    author="Srini Nariangadu",
    author_email="srini.nariangadu@gmail.com",
    description="A small sample package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/nsriniva/lambdata",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=['pandas'],
)