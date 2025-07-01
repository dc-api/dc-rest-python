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
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from dc_rest.models.user_avatar_decoration_response import UserAvatarDecorationResponse
from dc_rest.models.user_response import UserResponse
from typing import Optional, Set
from typing_extensions import Self

class GuildMemberResponse(BaseModel):
    """
    GuildMemberResponse
    """ # noqa: E501
    avatar: Optional[StrictStr] = None
    avatar_decoration_data: Optional[UserAvatarDecorationResponse] = None
    banner: Optional[StrictStr] = None
    communication_disabled_until: Optional[datetime] = None
    flags: StrictInt
    joined_at: datetime
    nick: Optional[StrictStr] = None
    pending: StrictBool
    premium_since: Optional[datetime] = None
    roles: List[Annotated[str, Field(strict=True)]]
    user: UserResponse
    mute: StrictBool
    deaf: StrictBool
    __properties: ClassVar[List[str]] = ["avatar", "avatar_decoration_data", "banner", "communication_disabled_until", "flags", "joined_at", "nick", "pending", "premium_since", "roles", "user", "mute", "deaf"]

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
        """Create an instance of GuildMemberResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of avatar_decoration_data
        if self.avatar_decoration_data:
            _dict['avatar_decoration_data'] = self.avatar_decoration_data.to_dict()
        # override the default output from pydantic by calling `to_dict()` of user
        if self.user:
            _dict['user'] = self.user.to_dict()
        # set to None if avatar (nullable) is None
        # and model_fields_set contains the field
        if self.avatar is None and "avatar" in self.model_fields_set:
            _dict['avatar'] = None

        # set to None if avatar_decoration_data (nullable) is None
        # and model_fields_set contains the field
        if self.avatar_decoration_data is None and "avatar_decoration_data" in self.model_fields_set:
            _dict['avatar_decoration_data'] = None

        # set to None if banner (nullable) is None
        # and model_fields_set contains the field
        if self.banner is None and "banner" in self.model_fields_set:
            _dict['banner'] = None

        # set to None if communication_disabled_until (nullable) is None
        # and model_fields_set contains the field
        if self.communication_disabled_until is None and "communication_disabled_until" in self.model_fields_set:
            _dict['communication_disabled_until'] = None

        # set to None if nick (nullable) is None
        # and model_fields_set contains the field
        if self.nick is None and "nick" in self.model_fields_set:
            _dict['nick'] = None

        # set to None if premium_since (nullable) is None
        # and model_fields_set contains the field
        if self.premium_since is None and "premium_since" in self.model_fields_set:
            _dict['premium_since'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GuildMemberResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        # raise errors for additional fields in the input
        for _key in obj.keys():
            if _key not in cls.__properties:
                raise ValueError("Error due to additional fields (not defined in GuildMemberResponse) in the input: " + _key)

        _obj = cls.model_validate({
            "avatar": obj.get("avatar"),
            "avatar_decoration_data": UserAvatarDecorationResponse.from_dict(obj["avatar_decoration_data"]) if obj.get("avatar_decoration_data") is not None else None,
            "banner": obj.get("banner"),
            "communication_disabled_until": obj.get("communication_disabled_until"),
            "flags": obj.get("flags"),
            "joined_at": obj.get("joined_at"),
            "nick": obj.get("nick"),
            "pending": obj.get("pending"),
            "premium_since": obj.get("premium_since"),
            "roles": obj.get("roles"),
            "user": UserResponse.from_dict(obj["user"]) if obj.get("user") is not None else None,
            "mute": obj.get("mute"),
            "deaf": obj.get("deaf")
        })
        return _obj


