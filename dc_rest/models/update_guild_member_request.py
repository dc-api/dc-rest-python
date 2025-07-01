# coding: utf-8

"""
Discord HTTP API (Preview) - REST API Client
Preview of the Discord v10 HTTP API specification. See https://discord.com/developers/docs for more details.

## Metadata

- **Copyright**: Copyright (c) 2025 Qntx
- **Author**: ΣX <gitctrlx@gmail.com>
- **Version**: 10
- **Modified**: 2025-07-01T06:33:02.994204459Z[Etc/UTC]
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

class UpdateGuildMemberRequest(BaseModel):
    """
    UpdateGuildMemberRequest
    """ # noqa: E501
    nick: Optional[Annotated[str, Field(strict=True, max_length=32)]] = None
    roles: Optional[Annotated[List[Annotated[str, Field(strict=True)]], Field(max_length=1521)]] = None
    mute: Optional[StrictBool] = None
    deaf: Optional[StrictBool] = None
    channel_id: Optional[Annotated[str, Field(strict=True)]] = None
    communication_disabled_until: Optional[datetime] = None
    flags: Optional[StrictInt] = None
    __properties: ClassVar[List[str]] = ["nick", "roles", "mute", "deaf", "channel_id", "communication_disabled_until", "flags"]

    @field_validator('channel_id')
    def channel_id_validate_regular_expression(cls, value):
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
        """Create an instance of UpdateGuildMemberRequest from a JSON string"""
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
        # set to None if nick (nullable) is None
        # and model_fields_set contains the field
        if self.nick is None and "nick" in self.model_fields_set:
            _dict['nick'] = None

        # set to None if roles (nullable) is None
        # and model_fields_set contains the field
        if self.roles is None and "roles" in self.model_fields_set:
            _dict['roles'] = None

        # set to None if mute (nullable) is None
        # and model_fields_set contains the field
        if self.mute is None and "mute" in self.model_fields_set:
            _dict['mute'] = None

        # set to None if deaf (nullable) is None
        # and model_fields_set contains the field
        if self.deaf is None and "deaf" in self.model_fields_set:
            _dict['deaf'] = None

        # set to None if communication_disabled_until (nullable) is None
        # and model_fields_set contains the field
        if self.communication_disabled_until is None and "communication_disabled_until" in self.model_fields_set:
            _dict['communication_disabled_until'] = None

        # set to None if flags (nullable) is None
        # and model_fields_set contains the field
        if self.flags is None and "flags" in self.model_fields_set:
            _dict['flags'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of UpdateGuildMemberRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        # raise errors for additional fields in the input
        for _key in obj.keys():
            if _key not in cls.__properties:
                raise ValueError("Error due to additional fields (not defined in UpdateGuildMemberRequest) in the input: " + _key)

        _obj = cls.model_validate({
            "nick": obj.get("nick"),
            "roles": obj.get("roles"),
            "mute": obj.get("mute"),
            "deaf": obj.get("deaf"),
            "channel_id": obj.get("channel_id"),
            "communication_disabled_until": obj.get("communication_disabled_until"),
            "flags": obj.get("flags")
        })
        return _obj


