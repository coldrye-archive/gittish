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


from enum import Enum
  
from sqlalchemy import Column
from sqlalchemy.types import Binary, BigInteger, DateTime, LargeBinary

from gittish.core.models.base import Base;
from gittish.core.models.mixins.owned import OwnedMixin
from gittish.core.models.mixins.typed import TypedMixin 
from gittish.core.models.mixins.uniquely_identified import UniquelyIdentifiedMixin


__all__ =
[
  'RepositoryObject',
  'RepositoryObjectType'
]


# TBD:DOCUMENT
class RepositoryObjectType(Enum):

  # TBD:DOCUMENT
  COMMIT = 1

  # TBD:DOCUMENT
  TREE = 2

  # TBD:DOCUMENT
  BLOB = 3

  # TBD:DOCUMENT
  TAG = 4


# TBD:DOCUMENT
class RepositoryObject(
	Base,
  UniquelyIdentified,
  CreatableMixin,
	OwnedMixin,
  TypedMixin
):
  __tablename__ = 'repository_objects'

  # TBD:DOCUMENT
	oid = Column('oid', Binary(length = 20), nullable = False)

  # TBD:DOCUMENT
  created_when = Column('created_when', DateTime(), nullable = False)

  # TBD:DOCUMENT
  size = Column('size', BigInteger, nullable = False)

  # TBD:DOCUMENT
  data = Column('data', LargeBinary, nullable = False)


# vim: expandtab:ts=2:sw=2:
