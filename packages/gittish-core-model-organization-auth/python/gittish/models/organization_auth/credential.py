# TBD:LICENSE


from gittish.core.models.base import Base
from gittish.core.models.mixins.credential import NamedCredentialMixin 


class OrganizationCredential(Base, NamedCredentialMixin):

	__tablename__ = 'organization_credentials'


# vim: expandtab:ts=2:sw=2:
