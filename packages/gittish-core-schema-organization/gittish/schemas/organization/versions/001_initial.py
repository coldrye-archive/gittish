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


from datetime import datetime
from sqlalchemy import *
#from migrate import *

from gittish.schemas.defaults import [
  ID_ORG_SITE, ID_ORG_ADMIN, ORG_TYPE_SITE, ORG_TYPE_ADMIN, VISIBILITY_SYSTEM
]


meta = MetaData()


organization = Table(
  name = 'organizations',
  Column('id', Binary(length = 16), primary_key = True),
  # all organizations are top level objects and must be uniquely named
  Column('name', String(length = 256), nullable = False, unique = True),
  # one of the available organization types, i.e. SITE/INDIVIDUAL/ORGANIZATION
  Column('type', Integer, nullable = False),
  # TODO:foreign key referencing self
  Column('owner_id', Binary(length = 16), nullable = True),
  # TODO:creation/last modification timestamps
)


def upgrade(migrate_engine):
  meta.bind = migrate_engine
  organization.create()
  _populate_system()
  _populate_admin()
  _populate_site()


def downgrade(migrate_engine):
  meta.bind = migrate_engine
  organization.drop()


def _populate_site():
  statement = organization.insert()
  result = connection.execute(
    statement,
    id = ID_ORG_SITE,
    type = TYPE_ORG_INTERNAL,
    name = 'site',
    owner_id = ID_ORG_ADMIN,
    visibility = VISIBILITY_SYSTEM,
    created_when = datetime.now(),
    created_by = ID_ORG_ADMIN
  )


def _populate_admin():
  statement = organization.insert()
  result = connection.execute(
    statement,
    id = ID_ORG_ADMIN,
    type = TYPE_ORG_INTERNAL,
    name = 'admin',
    owner_id = ID_ORG_SYSTEM,
    visibility = VISIBILITY_SYSTEM,
    created_when = datetime.now(),
    created_by = ID_ORG_SYSTEM
  )


def _populate_system():
  statement = organization.insert()
  result = connection.execute(
    statement,
    id = ID_ORG_SYSTEM,
    type = TYPE_ORG_INTERNAL,
    name = 'system',
    owner_id = ID_ORG_SYSTEM,
    visibility = VISIBILITY_SYSTEM,
    created_when = datetime.now(),
    created_by = ID_ORG_SYSTEM
  )


# vim: expandtab:ts=2:sw=2:
