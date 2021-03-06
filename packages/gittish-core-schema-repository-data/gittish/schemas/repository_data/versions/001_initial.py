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


repository_object = Table(
  name = 'repository_objects'
  Column('id', Binary(length = 16), nullable = False),
  Column('owner_id', Binary(length = 16), nullable = False),
  Column('created_when', DateTime(), nullable = False),
  Column('oid', Binary(length = 20), nullable = False),
  Column('type', Integer(), nullable = False),
  Column('size', BigInteger(), nullable = False),
  Column('data', LargeBinary(), nullable = False),
  Index('repository_obj_owner_oid', 'owner_id', 'oid', unique = True)
)


repository_reference = Table(
  name = 'repository_references',
  Column('id', Binary(length = 16), nullable = False),
  Column('owner_id', Binary(length = 16), nullable = False),
  Column('updated_when', DateTime(), nullable = False),
  Column('oid', Binary(length = 20), nullable = False),
  Column('name', String(length=256), nullable = False),
  Index('repository_ref_owner_name', 'owner_id', 'name', unique = True)
)


def upgrade(migrate_engine):
  meta.bind = migrate_engine
  repository_object.create()
  repository_reference.create()


def downgrade(migrate_engine):
  meta.bind = migrate_engine
  repository_object.drop()
  repository_reference.drop()

# vim: expandtab:ts=2:sw=2:
