def gen_default_conf():
    return """### Changeln Configuration Settings

# Template engine is Mako - https://www.makotemplates.org/
# Base template format is Markdown - https://python-markdown.github.io/
---

### List projects for generate changelog
projects:
  - /home/keygenqt/projects/test1
  - /home/keygenqt/projects/test2
  - /home/keygenqt/projects/test3

### Group commits
groups:
  Bug: '^[(Bug)]\s(.+)$'
  Added: '^[(Added)]\s(.+)$'
  Fixed: '^[(Fixed)]\s(.+)$'
"""
