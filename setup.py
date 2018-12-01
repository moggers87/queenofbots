from setuptools import setup, find_packages
import versioneer


with open("README.rst", "r") as f:
    long_desc = f.read()

setup(
    name="queenofbots",
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    author="Matt Molyneaux",
    author_email="moggers87+git@moggers87.co.uk",
    description="Mastodon ebooks bot manager",
    long_description=long_desc,
    url="https://github.com/moggers87/queenofbots",
    download_url="https://pypi.org/project/queenofbots/",
    packages=find_packages(),
    test_suite="exhibition.tests",
    license="AGPLv3",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: GNU Affero General Public License v3 or later (GPLv3+)",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: Internet",
    ],
    install_requires=[
        "Flask-WTF",
        "Mastodon.py",
        "beautifulsoup4",
        "flask",
        "markovify",
        "rq",
    ],
    extras_require={
        "docs": [
            "sphinx",
            "sphinx_rtd_theme",
            "sphinx-click",
        ],
    },
)
