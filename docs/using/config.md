# Config Changeln

This is the default configuration file.
Using this you can define tags, groups, and specify the path to the template.
Parse your comments using the regular expression for comments format output.
And filter out tags that should be skipped when generating a reference.

```yaml
## Application configuration file Changeln
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
```
