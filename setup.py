from setuptools import setup, find_packages
from typing import List

HYPHEN_E_DOT='-e .'

def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]

    with open(file_path, "r") as file:
        for line in file:
            line = line.strip()

            # ignore empty lines and comments
            if not line or line.startswith("#"):
                continue

            # ignore editable install (-e .)
            if line.startswith("-e"):
                continue

            requirements.append(line)

    return requirements




setup(
    name='mlproject',
    version='0.0.1',
    author='Shreya',
    author_email='shreyajain7078@gmail.com',
    packages=find_packages(),
    #find packages search for the __init__.py and see where all it is present and consider that folder as a package such as src
    #internal folder behaves like a package
    install_requires=get_requirements('requirements.txt')
)