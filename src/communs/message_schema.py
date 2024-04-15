"""Message schema module."""

from communs.base_model_schema import BaseModelSchema


class MessageSchema(BaseModelSchema):
    """Message schema class."""

    type: str
    sumary: str
    message: str
