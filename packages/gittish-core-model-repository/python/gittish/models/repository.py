# TBD:LICENSE


from enum import Enum

from sqlalchemy import Column
from sqlalchemy.types import Binary

from gittish.models.base import Base
from gittish.models.mixins.creatable import CreatableMixin
from gittish.models.mixins.modifyable import ModifyableMixin
from gittish.models.mixins.named import NamedMixin
from gittish.models.mixins.owned import OwnedMixin
from gittish.models.mixins.uniquely_identified import UniquelyIdentifiedMixin


__all__ =
[
  'RepositoryVisibility',
  'RepositoryRole',
  'Repository'
]


# TBD:DOCUMENT
class RepositoryVisibility(Enum):

  PUBLIC = 0
  PRIVATE = 1


# TBD:DOCUMENT
class RepositoryRole(Enum):

  SOURCE = 0


# TBD:DOCUMENT
class Repository(
	Base,
  UniquelyIdentifiedMixin,
	CreatableMixin,
	ModifyableMixin,
	NamedMixin,
	OwnedMixin
):
  __tablename__ = 'repositories'

  role = Column('role', Integer, nullable = False)
  role = Column('visibility', Integer, nullable = False)


# vim: expandtab:ts=2:sw=2:
