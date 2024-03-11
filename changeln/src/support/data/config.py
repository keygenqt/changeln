"""
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
"""

CHANGELOG_CONF = r'''## Application configuration file Changeln
## Version config: 0.0.2

## Comment tags by which they will be searched
## and groups by which they will be analyzed.
commits:
  Bug: '[bug]'
  Change: '[change]'
  Feature: '[feature]'

## Path to mako template
template: ./changeln.mako

## Regular expression to break the comment into groups
## to format the comment output in the changelog in the 
## "regex" variable.
##
## The empty value is not used.
parse: ''

## Filter tags using regular expressions
##
## The empty value is not used.
filter: ''
'''
