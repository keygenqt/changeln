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
import os
import re
from datetime import datetime
from pathlib import Path

import markdown as mark
from mako.template import Template
from weasyprint import HTML

from changeln.src.support.conf import OutType
from changeln.src.support.output import echo_stdout
from changeln.src.support.parse_git import ParseGit
from changeln.src.support.texts import AppTexts


# Generate html from template mako
def _gen_changelog(ctx) -> str:
    """Common gen changelog."""
    parser = ParseGit(
        commits=ctx.obj.get_commits(),
        parse_commit=ctx.obj.get_parse(),
        filter_tags=ctx.obj.get_filter(),
    )

    ln_date = datetime.now()
    ln_last = parser.get_last_tag()
    ln_list_tags = parser.get_tags()
    ln_count_tags = parser.get_count_tags()
    ln_group_commits = parser.get_group_commits()

    out = Template(ctx.obj.get_template()).render(
        ln_date=ln_date,
        ln_last=ln_last,
        ln_list_tags=ln_list_tags,
        ln_count_tags=ln_count_tags,
        ln_group_commits=ln_group_commits,
    ).strip()

    return '\n'.join([line.strip() for line in re.sub(r'\n\n+', '\n\n', out).split('\n')])


def group_make(ctx: {}, output: str):
    """Generate changelog."""

    try:
        out_md = _gen_changelog(ctx)
    except Exception as e:
        echo_stdout(AppTexts.error_template_parse(e))
        exit(1)

    out_path = ctx.obj.get_path_out()

    match OutType(output):
        case OutType.markdown:
            out_path = out_path / 'CHANGELOG.md'
            with open(out_path, 'w') as file:
                print(out_md, file=file)
        case OutType.html:
            out_path = out_path / 'CHANGELOG.html'
            out_html = mark.markdown(out_md)
            with open(out_path, 'w') as file:
                print(out_html, file=file)
        case OutType.pdf:
            out_path = out_path / 'CHANGELOG.pdf'
            out_html = mark.markdown(out_md)
            HTML(string=out_html).write_pdf(out_path)

    echo_stdout(AppTexts.success_save_changelog(str(out_path)))
