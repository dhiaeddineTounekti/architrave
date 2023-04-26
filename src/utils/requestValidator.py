import uuid
from typing import Union


def is_valid_uuid(uuid_string: Union[str, None]) -> bool:
    try:
        uuid.UUID(uuid_string)
        return True
    except ValueError:
        return False


def is_valid_customer_id(customer_id: Union[str, None]) -> bool:
    if not customer_id or not is_valid_uuid(customer_id):
        return False
    else:
        return True
