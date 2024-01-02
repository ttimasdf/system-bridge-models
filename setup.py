"""Setup."""
from setuptools import find_packages, setup

# Get setup packages from requirements.txt
with open("requirements_setup.txt", encoding="utf-8") as f:
    requirements_setup = f.read().splitlines()

# Get packages from requirements.txt
with open("requirements.txt", encoding="utf-8") as f:
    requirements = f.read().splitlines()

with open("README.md", encoding="utf-8") as f:
    readme = f.read()

setup(
    name="systembridgemodels",
    description="System Bridge Models",
    long_description=readme,
    long_description_content_type="text/markdown",
    keywords="system-bridge",
    author="Aidan Timson (Timmo)",
    author_email="aidan@timmo.dev",
    license="Apache-2.0",
    url="https://github.com/timmo001/system-bridge-models",
    packages=find_packages(exclude=["tests", "generator"]),
    install_requires=requirements,
    setup_requires=requirements_setup,
    use_incremental=True,
)
