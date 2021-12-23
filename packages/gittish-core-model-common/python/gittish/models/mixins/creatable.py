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
from sqlalchemy.types import DateTime, Binary


__all__ =
[
  'CreatableMixin'
]


class CreatableMixin:

  created_when = Column('created_when', DateTime(), nullable = False)

  created_by = Column('created_by', Binary(length = 16), nullable = True)


# vim: expandtab:ts=2:sw=2:
