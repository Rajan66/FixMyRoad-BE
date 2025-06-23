from base.models._timestamp import Timestamps
from base.models._uuid import UUIDPrimaryKey


class AbstractBaseModel(UUIDPrimaryKey, Timestamps):
    class Meta(UUIDPrimaryKey.Meta, Timestamps.Meta):
        abstract = True
