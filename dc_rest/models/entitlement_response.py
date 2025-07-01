# coding: utf-8

"""
Discord HTTP API (Preview) - REST API Client
Preview of the Discord v10 HTTP API specification. See https://discord.com/developers/docs for more details.

## Metadata

- **Copyright**: Copyright (c) 2025 Qntx
- **Author**: ΣX <gitctrlx@gmail.com>
- **Version**: 10
- **Modified**: 2025-07-01T10:27:27.208780920Z[Etc/UTC]
- **Generator Version**: 7.14.0

<details>
<summary><strong>⚠️ Important Disclaimer & Limitation of Liability</strong></summary>
<br>
> **IMPORTANT**: This software is provided "as is" without any warranties, express or implied, including but not limited
> to warranties of merchantability, fitness for a particular purpose, or non-infringement. The developers, contributors,
> and licensors (collectively, "Developers") make no representations regarding the accuracy, completeness, or reliability
> of this software or its outputs.
>
> This client is not intended to provide financial, investment, tax, or legal advice. It facilitates interaction with the
> Discord HTTP API (Preview) service but does not endorse or recommend any financial actions, including the purchase, sale, or holding of
> financial instruments (e.g., stocks, bonds, derivatives, cryptocurrencies). Users must consult qualified financial or
> legal professionals before making decisions based on this software's outputs.
>
> Financial markets are inherently speculative and carry significant risks. Using this software in trading, analysis, or
> other financial activities may result in substantial losses, including total loss of capital. The Developers are not
> liable for any losses or damages arising from such use. Users assume full responsibility for validating the software's
> outputs and ensuring their suitability for intended purposes.
>
> This client may rely on third-party data or services (e.g., market feeds, APIs). The Developers do not control or verify
> the accuracy of these services and are not liable for any errors, delays, or losses resulting from their use. Users must
> comply with third-party terms and conditions.
>
> Users are solely responsible for ensuring compliance with all applicable financial, tax, and regulatory requirements in
> their jurisdiction. This includes obtaining necessary licenses or approvals for trading or investment activities. The
> Developers disclaim liability for any legal consequences arising from non-compliance.
>
> To the fullest extent permitted by law, the Developers shall not be liable for any direct, indirect, incidental,
> consequential, or punitive damages arising from the use or inability to use this software, including but not limited to
> loss of profits, data, or business opportunities.

</details>
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class EntitlementResponse(BaseModel):
    """
    EntitlementResponse
    """ # noqa: E501
    id: Annotated[str, Field(strict=True)]
    sku_id: Annotated[str, Field(strict=True)]
    application_id: Annotated[str, Field(strict=True)]
    user_id: Annotated[str, Field(strict=True)]
    guild_id: Optional[Annotated[str, Field(strict=True)]] = None
    deleted: StrictBool
    starts_at: Optional[datetime] = None
    ends_at: Optional[datetime] = None
    type: Optional[StrictInt]
    fulfilled_at: Optional[datetime] = None
    fulfillment_status: Optional[StrictInt] = None
    consumed: Optional[StrictBool] = None
    __properties: ClassVar[List[str]] = ["id", "sku_id", "application_id", "user_id", "guild_id", "deleted", "starts_at", "ends_at", "type", "fulfilled_at", "fulfillment_status", "consumed"]

    @field_validator('id')
    def id_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^(0|[1-9][0-9]*)$", value):
            raise ValueError(r"must validate the regular expression /^(0|[1-9][0-9]*)$/")
        return value

    @field_validator('sku_id')
    def sku_id_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^(0|[1-9][0-9]*)$", value):
            raise ValueError(r"must validate the regular expression /^(0|[1-9][0-9]*)$/")
        return value

    @field_validator('application_id')
    def application_id_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^(0|[1-9][0-9]*)$", value):
            raise ValueError(r"must validate the regular expression /^(0|[1-9][0-9]*)$/")
        return value

    @field_validator('user_id')
    def user_id_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^(0|[1-9][0-9]*)$", value):
            raise ValueError(r"must validate the regular expression /^(0|[1-9][0-9]*)$/")
        return value

    @field_validator('guild_id')
    def guild_id_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^(0|[1-9][0-9]*)$", value):
            raise ValueError(r"must validate the regular expression /^(0|[1-9][0-9]*)$/")
        return value

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of EntitlementResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # set to None if starts_at (nullable) is None
        # and model_fields_set contains the field
        if self.starts_at is None and "starts_at" in self.model_fields_set:
            _dict['starts_at'] = None

        # set to None if ends_at (nullable) is None
        # and model_fields_set contains the field
        if self.ends_at is None and "ends_at" in self.model_fields_set:
            _dict['ends_at'] = None

        # set to None if type (nullable) is None
        # and model_fields_set contains the field
        if self.type is None and "type" in self.model_fields_set:
            _dict['type'] = None

        # set to None if fulfilled_at (nullable) is None
        # and model_fields_set contains the field
        if self.fulfilled_at is None and "fulfilled_at" in self.model_fields_set:
            _dict['fulfilled_at'] = None

        # set to None if fulfillment_status (nullable) is None
        # and model_fields_set contains the field
        if self.fulfillment_status is None and "fulfillment_status" in self.model_fields_set:
            _dict['fulfillment_status'] = None

        # set to None if consumed (nullable) is None
        # and model_fields_set contains the field
        if self.consumed is None and "consumed" in self.model_fields_set:
            _dict['consumed'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of EntitlementResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        # raise errors for additional fields in the input
        for _key in obj.keys():
            if _key not in cls.__properties:
                raise ValueError("Error due to additional fields (not defined in EntitlementResponse) in the input: " + _key)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "sku_id": obj.get("sku_id"),
            "application_id": obj.get("application_id"),
            "user_id": obj.get("user_id"),
            "guild_id": obj.get("guild_id"),
            "deleted": obj.get("deleted"),
            "starts_at": obj.get("starts_at"),
            "ends_at": obj.get("ends_at"),
            "type": obj.get("type"),
            "fulfilled_at": obj.get("fulfilled_at"),
            "fulfillment_status": obj.get("fulfillment_status"),
            "consumed": obj.get("consumed")
        })
        return _obj


