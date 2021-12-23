# TBD:LICENSE


from gittish.core.models.base import Base
from gittish.core.models.mixins.acl_entry import AclEntryMixin


class OrganizationAclEntry(Base, AclEntryMixin):

	__tablename__ = 'organization_acl_entries'


# vim: expandtab:ts=2:sw=2:
