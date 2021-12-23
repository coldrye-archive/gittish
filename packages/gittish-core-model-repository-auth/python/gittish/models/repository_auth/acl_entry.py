# TBD:LICENSE


from gittish.core.models.base import Base
from gittish.core.models.mixins.acl_entry import AclEntryMixin


class RepositoryAclEntry(Base, AclEntryMixin):

	__tablename__ = 'repository_acl_entries'


# vim: expandtab:ts=2:sw=2:
