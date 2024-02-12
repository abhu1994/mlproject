from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'

def get_requirements(file_path:str)->List[str]:
    '''
    this is function which will return the list of requiremnts
    '''
    requirements=[]

    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace('\n',"") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    file_obj.close()
    return requirements

    



setup(
    name='mlproject',
    version='0.0.1',
    author='abha',
    author_email='ajain1188@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)