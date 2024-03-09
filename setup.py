import setuptools

long_description = """
![picture](https://github.com/keygenqt/changeln/blob/dev/data/banners/banner_round.png?raw=true)

The application allows you to generate CHANGELOG files based on Git tags.

[More...](https://keygenqt.github.io/changeln)

### License

```
Copyright 2021-2024 Vitaliy Zarubin

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```
"""

setuptools.setup(
    name='changeln',
    version='1.0.6',
    author='Vitaliy Zarubin',
    author_email='keygenqt@gmail.com',
    description='Automatically generate change log from your tags',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url="https://github.com/keygenqt/changeln",
    packages=setuptools.find_packages(exclude=['*tests.*', '*tests']),
    include_package_data=True,
    py_modules=['colors'],
    install_requires=[
        'cffi',
        'pillow',
        'click',
        'Mako',
        'pyYaml',
        'gitpython',
        'natsort',
        'Markdown',
        'WeasyPrint',
        'setuptools',
    ],
    python_requires='>=3.6.9',
    entry_points="""
        [console_scripts]
        changeln = changeln.__main__:cli
    """
)
