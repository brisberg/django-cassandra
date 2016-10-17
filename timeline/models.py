from __future__ import unicode_literals


import uuid
from cassandra.cqlengine import columns

from cassandra.cqlengine.models import Model
# from django.db.models import Model


class Comment_by_Author(Model):
    id = columns.UUID(primary_key=True, default=uuid.uuid4)
    author = columns.Integer(primary_key=True)
    recipient = columns.Integer(index=True)
    message = columns.Text()


class integerModel(Model):
    num = columns.UUID(primary_key=True)
