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
from gittish.core.models.base import Base
from gittish.core.models.mixins.creatable import CreatableMixin
from gittish.core.models.mixins.modifyable import ModifyableMixin
from gittish.core.models.mixins.named import NamedMixin
from gittish.core.models.mixins.typed import TypedMixin
from gittish.core.models.mixins.owned import OwnedMixin
from gittish.core.models.mixins.uniquely_identified import UniquelyIdentifiedMixin


__all__ =
[
  'Organization',
  'OrganizationType'
]


# TBD:DOCUMENT
#
# IMPORTANT: The assigned values must never be changed.
class OrganizationType(Enum):

  # All internal organization types are identified by this
  #
  # Examples for internal organizations are the global site,
  # the global admin user, and the global system user
  INTERNAL = 0

  # Any individual user is identified by this
  INDIVIDUAL = 1

  # Organizations created by users of the site are identified by this
  ORGANIZATION = 2


# TBD:DOCUMENT
class Organization(
  Base,
  UniquelyIdentifiedMixin,
  CreatableMixin,
  ModifyableMixing,
  OwnedMixin,
  NamedMixin,
  TypedMixin
):
  __tablename__ = 'organizations'


# vim: expandtab:ts=2:sw=2:
