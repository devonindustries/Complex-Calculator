import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="complex-calculator-devonindustries",
    version="1.0.1",
    author="Joshua Baker",
    author_email="jd.baker01@hotmail.co.nz",
    description="Framework for performing complex arithmetic",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/devonindustries/complex_calculator",
    project_urls={
        "Bug Tracker": "https://github.com/devonindustries/complex_calculator/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
)