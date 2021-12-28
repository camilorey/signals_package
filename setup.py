import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="signal-creator-pkg-CAMILO-REY",
    version="0.0.1",
    author="Camilo Rey-Torres",
    author_email="camilorey@gmail.com",
    description="A simple signals package to create and distort harmonic signals",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/camilorey/signals_package",
    project_urls={
        "Bug Tracker": "https://github.com/camilorey/signals_package/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "signals"},
    packages=setuptools.find_packages(where="signals"),
    python_requires=">=3.6",
)