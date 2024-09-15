from  setuptools import find_packages, setup   # setuptools is a package that provids tools to packaging python projects
from typing import List

HYPEN_E_DOT='-e.'

def get_requirements(file_path: str)->List[str]: 
    requirements=[]
    with open(file_path) as file_obj: 
        requirements=file_obj.readlines()
        requirements=[req.replace("\n", "" ) for req in requirements]
    if HYPEN_E_DOT in requirements: 
        requirements.remove(HYPEN_E_DOT)
        
    return requirements

setup(
    name='Fault Detection',  # name of project
    version='0.0.1',
    author='Pankaj',
    author_email='pankajkumawatew3004@gmail.com',
    install_requirements=get_requirements('requirements.txt'),
    packages=find_packages()
    
)