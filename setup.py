from setuptools import setup ,find_packages


def get_requirements(file_path):
    requirements = []

    with open(file_path,'r') as f:
        requirements = f.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
    return requirements



setup(

name = "project pipeline",
version = '0.0.1',
author='hira mariam',
author_email='hiramariam@neduet.edu.pk',
packages=find_packages(),
install_requires = get_requirements('requirements.txt')

)