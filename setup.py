import setuptools

with open("README.md", "r", encoding="utf-8") as fr:
    long_description = fr.read()

__version__ = "0.0.0"

repo_name = "Facial-emotion-detection"
account_name = "YashAmin0"
src_repo = "Facial-emotion-detection"
account_email = "yashamin024@gmail.com"

setuptools.setup(
    name=src_repo,
    version=__version__,
    author=account_name,
    author_email=account_email,
    description="A small python package for CNN app",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{account_name}/{repo_name}",
    project_urls={
        "Bug Tracker": f"https://github.com/{account_name}/{repo_name}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)