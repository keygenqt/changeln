# Template Changeln

This is the default template based on which the changelog will be generated.
Templates engine - [Mako](https://www.makotemplates.org/).

```mako
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
```

You can add all the data to the template:

```mako
${context.keys()}
${context.__dict__}
```

The application outputs data to a template, its structure is as follows:

```json
// Date now
ln_date: datetime

// Last tag
ln_last: str

// All find tags
ln_list_tags: [TagReference]

// Count tags
ln_count_tags: int

// Goups commits by tags
ln_group_commits: [
    // Name TAG/HEAD
    name: str, 
    // Date create tag
    date: datetime,
    // All commits
    commits: [Commit],
    // Commits by group
    group: [
            {
                // Name group from config
                name: str, 
                // Commits group
                commits: [
                    {
                        // Commit
                        commit: Commit,
                        // Groups regex from config if not empty value
                        regex: [],
                        // Message commit without [tag]
                        clean: str
                    }
                ]
            }
         ]
    ]
```
