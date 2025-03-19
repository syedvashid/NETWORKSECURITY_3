'''
The setup.py file is an essentiial part of packaging and 
distributin Python project it is Used by setuptools
(or distuitls in order Python versions) to define the configration 
of your project , such as its metadata ,dependences,and more
'''

from setuptools import find_packages, setup
from typing import List

def get_requirements() -> List[str]:
    """
    This function will return a list of requirements.
    """
    requirement_lst: List[str] = []
    try:
        with open('requirements.txt', 'r') as file:
            # read all lines from the file
            lines = file.readlines()
            # process each line
            for line in lines:
                requirement = line.strip()
                # ignore empty lines and '-e .'
                if requirement and requirement != '-e .':
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found")
    
    return requirement_lst

setup(
    name="NetworkSecurity",
    version="0.0.1",
    author="SYED VASHID ALI",
    author_email="akshan09061999@gmial.com",
    packages=find_packages(),
    install_requires = get_requirements(),
    )