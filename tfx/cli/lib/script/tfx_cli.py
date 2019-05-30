# Copyright 2019 Google LLC. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""TODO(swoonna): DO NOT SUBMIT without one-line documentation for tfx_cli.

TODO(swoonna): DO NOT SUBMIT without a detailed description of tfx_cli.
"""

import click

from tfx.cli.lib.cmd import tfx_pipeline_commands


@click.group('cli')
def cli():
  pass

cli.add_command(tfx_pipeline_commands.pipeline_group)

if __name__ == '__main__':
  cli()

