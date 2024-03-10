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
from changeln.src.support.conf import OutType
from changeln.src.support.output import echo_stdout


def group_make(ctx: {}, output: str):
    """Generate changelog."""

    echo_stdout(str(ctx.obj.get_template()))
    echo_stdout(str(ctx.obj.get_parse()))
    echo_stdout(str(ctx.obj.get_filter()))
    echo_stdout(str(ctx.obj.get_commits()))

    match OutType(output):
        case OutType.markdown:
            print(1)
        case OutType.html:
            print(2)
        case OutType.pdf:
            print(3)
