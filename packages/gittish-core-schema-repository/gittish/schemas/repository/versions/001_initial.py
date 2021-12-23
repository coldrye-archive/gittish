# Copyright 2017 Carsten Klein
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from sqlalchemy import *
#from migrate import *


meta = MetaData()


repository = Table(
  name = 'repositories'
  Column('id', Binary(length = 16), primary_key = True),
  Column('organization_id', Binary(length = 16), nullable = False),
  Column('name', String(length=256), nullable = False),
  Index('repository_org_name', 'organization_id', 'name', unique = True)
)


def upgrade(migrate_engine):
  meta.bind = migrate_engine
  repository.create()


def downgrade(migrate_engine):
  meta.bind = migrate_engine
  repository.drop()

# vim: expandtab:ts=2:sw=2:
