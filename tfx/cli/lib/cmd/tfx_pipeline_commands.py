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

"""Commands for pipeline group."""


import click


class PipelineContext(object):

  def __init__(self):
    self.flags_dict = {}

pass_context = click.make_pass_decorator(PipelineContext, ensure=True)


@click.group('pipeline')
def pipeline_group():
  click.echo('CLI')


@pipeline_group.command('create')
@pass_context
@click.option('--engine', 'engine', default='auto', type=str)
@click.option('--path', 'pipeline_path', required=True, type=str)
def create_pipeline(ctx, engine, pipeline_path):
  ctx.flags_dict['engine'] = engine
  ctx.flags_dict['pipeline_path'] = pipeline_path


@pipeline_group.command('delete')
@click.pass_context
@click.option('--engine', 'engine', default='auto', type=str)
@click.option('--name', 'pipeline_name', required=True, type=str)
def delete_pipeline(ctx, pipeline_name, engine):
  ctx.flags_dict['engine'] = engine
  ctx.flags_dict['pipeline_name'] = pipeline_name


@pipeline_group.command('update')
@click.pass_context
@click.option('--engine', 'engine', default='auto', type=str)
@click.option('--path', 'pipeline_path', required=True, type=str)
def update_pipeline(ctx, pipeline_path, engine):
  ctx.flags_dict['engine'] = engine
  ctx.flags_dict['pipeline_path'] = pipeline_path


@pipeline_group.command('run')
@click.pass_context
@click.option('--engine', 'engine', default='auto', type=str)
@click.option('--name', 'pipeline_name', required=True, type=str)
def run_pipeline(ctx, pipeline_name, engine):
  ctx.flags_dict['engine'] = engine
  ctx.flags_dict['pipeline_name'] = pipeline_name
