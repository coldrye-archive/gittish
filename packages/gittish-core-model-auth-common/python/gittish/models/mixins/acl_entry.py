# TBD:LICENSE

from sqlalchemy import Column
from sqlalchemy.types import String

from gittish.models.mixins.creatable import CreatableMixin
from gittish.models.mixins.owned import OwnedMixin
from gittish.models.mixins.typed import TypedMixin
from gittish.models.mixins.uniquely_identified import UniquelyIdentifiedMixin


class AclEntryMixin(
  CreatableMixin,
  OwnedMixin,
  TypedMixin,
  UniquelyIdentifiedMixin
):

  permission = Column('permission', String(length = 512), nullable = False)


# vim: expandtab:ts=2:sw=2:
