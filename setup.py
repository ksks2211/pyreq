import setuptools


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


setuptools.setup(
    name="pyreq",
    version="0.0.1",
    author="pyy",
    author_email="rival15@naver.com",
    description="personal python clients",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kkll22/pyreq",
    project_urls={"Bug Tracker": "https://github.com/kkll22/pyreq/issues"},
    license="MIT",
    packages=["pyreq", "pyreq.fetcher", "pyreq.downloader", "pyreq.htmlcollector"],
    install_requires=["requests", "multimethod", "lxml", "cssselect"],
)
