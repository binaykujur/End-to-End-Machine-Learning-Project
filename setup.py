from setuptools import setup, find_packages
from typing import List
HYPHEN_E_DOT = "-e ."
def get_requirements(file_path:str)->List[str]:
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            lines = [line.strip() for line in lines]
            if HYPHEN_E_DOT in lines:
                lines.remove(HYPHEN_E_DOT)
            return lines
    except FileNotFoundError:
        print(f"the file {file_path} was not fount")
        return []
    except Exception as e:
        print(f"An error occured: {e}")
        return []

setup(
name = 'ml_project',
version = '0.0.1',
author = 'Binay Kujur',
author_email = 'binaykujur59@gmail.com',
packages = find_packages(),
install_requires = get_requirements('requirements.txt')

)