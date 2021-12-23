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


from sqlalchemy import Column
from sqlalchemy.types import Binary, DateTime

from gittish.core.models.base import Base;
from gittish.core.models.mixins.named import NamedMixin
from gittish.core.models.mixins.owned import OwnedMixin
from gittish.core.models.mixins.uniquely_identified import UniquelyIdentifiedMixin


__all__ =
[
  'RepositoryReference'
]


# TBD:DOCUMENT
class RepositoryReference(
	Base,
  UniquelyIdentifiedMixin,
	NamedMixin,
  CreatableMixin,
  ModifyableMixin,
	OwnedMixin
):
  __tablename__ = 'repository_references'

  # TBD:DOCUMENT
  updated_when = Column('updated_when', DateTime(), nullable = False)

  # TBD:DOCUMENT
	oid = Column('oid', Binary(length = 20), nullable = False)


# vim: expandtab:ts=2:sw=2:
