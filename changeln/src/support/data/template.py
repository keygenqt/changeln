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

CHANGELOG_TEMPLATE = r'''### Changeln template example
### Template engine is Mako - https://www.makotemplates.org/
### Base template format is Markdown - https://python-markdown.github.io/
###
### Show all values: 
### ${context.keys()}
### ${context.__dict__}
###
### Structure:
### ln_date: datetime
### ln_last: str
### ln_list_tags: [TagReference]
### ln_count_tags: int
### ln_group_commits: [
###     name: str, 
###     date: datetime,
###     commits: [Commit],
###     group: [
###             {
###                 name: str, 
###                 commits: [
###                     {
###                         commit: Commit, 
###                         regex: [], 
###                         clean: str
###                     }
###                 ]
###             }
###          ]
###     ]

<%! from datetime import datetime %>

${"##"} Updated: ${ln_date.strftime('%m/%d/%Y %H:%M:%S %p')}

${"##"} Info

- Last tag: ${ln_last}
- Released: ${ln_count_tags}

${"##"} Versions

% for item in ln_list_tags:
- Version: ${item.name} (${datetime.fromtimestamp(item.commit.committed_date).strftime('%d/%m/%Y')})
% endfor

% for tag in ln_group_commits:

    % if tag['commits']:
        % if tag['name'] == 'HEAD':
            ${"###"} HEAD (${ln_date.strftime('%d/%m/%Y')})
        % else:
            ${"###"} Version: ${tag['name']} (${datetime.fromtimestamp(tag['date']).strftime('%d/%m/%Y')})
        % endif
    % endif

    % for group in tag['group']:

        % if group['commits']:
            ${"####"} ${group['name']}

            % for commit in group['commits']:
                - ${commit['clean']} (${commit['commit'].author})
            % endfor
        % endif

    % endfor
% endfor
'''
