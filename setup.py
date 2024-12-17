from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path: str) -> List[str]:
    requirements = []
    with open(file_path, 'r') as f:
        requirements = f.readlines()
        requirements = [req.strip() for req in requirements if req.strip() and req.strip() != "-e ."]
    return requirements

setup(
    name="ML_AWS_project",
    version="0.0.1",
    author="rao_abhinandan",
    author_email="raoabhi90@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
    python_requires='>=3.8',
)


print(get_requirements('requirements.txt'))
