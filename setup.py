from distutils.core import setup

setup(
    name = 'neospatial',
    py_modules = ['neospatial'],
    version = '0.1.0',
    description = 'Python Wrapper for Neo4j Spatial Plugin',
    author = 'Gianluca Tiepolo',
    author_email = 'tiepolo.gian@gmail.com',
    long_description=open('README.md').read(),
    url = 'https://github.com/tiepologian/neospatial-py',
    keywords = ['neo4j', 'spatial', 'plugin'],
    classifiers = [],
    install_requires=[
"requests >= 2.2.1",
    ],
)
