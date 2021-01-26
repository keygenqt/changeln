"""
Copyright 2021 Vitaliy Zarubin

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

def gen_default_template():
    return """### Changeln template example
### Template engine is Mako - https://www.makotemplates.org/
### Base template format is Markdown - https://python-markdown.github.io/

<%! from datetime import datetime %>

${"##"} Updated: ${ln_date.strftime('%d/%m/%Y %H:%M:%S %p')}

${"##"} Info

- Last tag: ${ln_last}
- Released: ${ln_released}

${"##"} Versions
% for item in ln_list_tags:
- Version: ${item.name} (${datetime.fromtimestamp(item.commit.committed_date).strftime('%d/%m/%Y')})
% endfor

% for item in ln_list_groups:

    % if item['to'] == 'HEAD':
        ${"###"} HEAD (${ln_date.strftime('%d/%m/%Y %H:%M:%S %p')})
    % else:
        ${"###"} Version: ${item['tag'].name} (${datetime.fromtimestamp(item['tag'].commit.committed_date).strftime('%d/%m/%Y')})
    % endif

    % if item['Feature'] or item['Change'] or item['Bug']:

        ${'####'} Feature

        % if not item['Feature']:
            *None*
        % endif
        % for feature in item['Feature']:
            * [${feature['optional'][0]}] ${feature['optional'][2]} (${feature['commit'].author})
        % endfor

        ${'####'} Change

        % if not item['Change']:
            *None*
        % endif
        % for change in item['Change']:
            * [${change['optional'][0]}] ${change['optional'][2]} (${change['commit'].author})
        % endfor

        ${'####'} Bug

        % if not item['Bug']:
            *None*
        % endif
        % for bug in item['Bug']:
            * [${bug['optional'][0]}] ${bug['optional'][2]} (${bug['commit'].author})
        % endfor

    % else:
        % for data in item['data']:
            %if 'update' in data.message:
                <% continue %>
            % endif
            %if '---------------------------' in data.message:
                <% continue %>
            % endif
            * ${data.message.strip()} (${data.author})
        % else:
            *None*
        % endfor
    % endif
% endfor
"""
