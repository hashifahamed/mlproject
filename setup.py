from setuptools import find_packages, setup

setup(
    name='mlproject',
    version='0.0.1',
    author='Hashif',
    author_email='hashifahamed6@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')

)