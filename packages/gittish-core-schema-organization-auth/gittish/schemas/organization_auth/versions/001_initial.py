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


organization_credential = Table(
  name = 'organization_credentials',
  Column('id', Binary(length = 16), primary_key = True),
  Column('organization_id', Binary(length = 16), nullable = False),
  # TBD:name and organization_id are unique
  Column('name', String(length = 256), nullable = False),
  Column('data', Binary(length = 8192), nullable = False),
  # TBD:one of the available organization credential types, PUBLIC_KEY, ...
  Column('type', Integer, nullable = False)
)


organization_acl_entry = Table(
  name = 'organization_acl_entries',
  Column('id', Binary(length = 16), primary_key = True),
  Column('organization_id', Binary(length = 16), nullable = False),
  # actor_id is either the id of a group or of an organization that is an individual
  Column('actor_id', Binary(length = 16), nullable = False),
  Column('permission', String(length = 256), nullable = False),
  # grant/deny
  Column('type', Integer, nullable = False)
)


def upgrade(migrate_engine):
  meta.bind = migrate_engine
  organization_credential.create()
  organization_acl_entry.create()


def downgrade(migrate_engine):
  meta.bind = migrate_engine
  organization_credential.drop()
  organization_acl_entry.drop()

# vim: expandtab:ts=2:sw=2:
