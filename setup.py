import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='changeln',
    version='0.0.1',
    author='Vitaliy Zarubin',
    author_email='keygenqt@gmail.com',
    description='Automatically generate change log from your tags',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url="https://github.com/keygenqt/skill-tkinter-snap",
    packages=setuptools.find_packages(exclude=['*tests.*', '*tests']),
    include_package_data=True,
    py_modules=['colors'],
    install_requires=[
        'click'
    ],
    python_requires='>=3.6',
    entry_points="""
        [console_scripts]
        changeln = app.__main__:cli
    """
)
