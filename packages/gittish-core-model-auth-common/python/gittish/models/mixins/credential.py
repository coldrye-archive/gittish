# TBD:LICENSE


from sqlalchemy import Column
from sqlalchemy.types import LargeBinary

from gittish.models.mixins.creatable import CreatableMixin
from gittish.models.mixins.modifyable import ModifyableMixin
from gittish.models.mixins.owned import OwnedMixin
from gittish.models.mixins.typed import TypedMixin
from gittish.models.mixins.named import NamedMixin
from gittish.models.mixins.status import StatusMixin
from gittish.models.mixins.uniquely_identified import UniquelyIdentifiedMixin


class CredentialMixin(
  CreatableMixin,
  ModifyableMixin,
  OwnedMixin,
  TypedMixin,
  StatusMixin,
  UniquelyIdentifiedMixin
):

  data = Column('data', LargeBinary, nullable = True)


class NamedCredentialMixin(
  CredentialMixin,
  NamedMixin
):

  pass


# vim: expandtab:ts=2:sw=2:
