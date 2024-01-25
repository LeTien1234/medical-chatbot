from setuptools import find_packages ,setup

setup(
    name = 'medicalChatbot',
    version='0.0.1',
    author='TienLe1234',
    author_email='tle38413@gmail.com',
    install_requires = ['ctransformers==0.2.5' , 'sentence-transformers==2.2.2','pinecone-client','langchain==0.0.225','flask','pypdf','python-dotenv'],
    packages= find_packages()
)