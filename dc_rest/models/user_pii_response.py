# coding: utf-8

"""
Discord HTTP API (Preview) - REST API Client
Preview of the Discord v10 HTTP API specification. See https://discord.com/developers/docs for more details.

## Metadata

- **Copyright**: Copyright (c) 2025 Qntx
- **Author**: ΣX <gitctrlx@gmail.com>
- **Version**: 10
- **Modified**: 2025-07-05T02:42:22.742560433Z[Etc/UTC]
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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from dc_rest.models.user_avatar_decoration_response import UserAvatarDecorationResponse
from dc_rest.models.user_collectibles_response import UserCollectiblesResponse
from dc_rest.models.user_primary_guild_response import UserPrimaryGuildResponse
from typing import Optional, Set
from typing_extensions import Self

class UserPIIResponse(BaseModel):
    """
    UserPIIResponse
    """ # noqa: E501
    id: Annotated[str, Field(strict=True)]
    username: StrictStr
    avatar: Optional[StrictStr] = None
    discriminator: StrictStr
    public_flags: StrictInt
    flags: Annotated[int, Field(le=9007199254740991, strict=True, ge=-9007199254740991)]
    bot: Optional[StrictBool] = None
    system: Optional[StrictBool] = None
    banner: Optional[StrictStr] = None
    accent_color: Optional[StrictInt] = None
    global_name: Optional[StrictStr] = None
    avatar_decoration_data: Optional[UserAvatarDecorationResponse] = None
    collectibles: Optional[UserCollectiblesResponse] = None
    primary_guild: Optional[UserPrimaryGuildResponse] = None
    mfa_enabled: StrictBool
    locale: StrictStr
    premium_type: Optional[StrictInt] = None
    email: Optional[StrictStr] = None
    verified: Optional[StrictBool] = None
    __properties: ClassVar[List[str]] = ["id", "username", "avatar", "discriminator", "public_flags", "flags", "bot", "system", "banner", "accent_color", "global_name", "avatar_decoration_data", "collectibles", "primary_guild", "mfa_enabled", "locale", "premium_type", "email", "verified"]

    @field_validator('id')
    def id_validate_regular_expression(cls, value):
        """Validates the regular expression"""
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
        """Create an instance of UserPIIResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of collectibles
        if self.collectibles:
            _dict['collectibles'] = self.collectibles.to_dict()
        # override the default output from pydantic by calling `to_dict()` of primary_guild
        if self.primary_guild:
            _dict['primary_guild'] = self.primary_guild.to_dict()
        # set to None if avatar (nullable) is None
        # and model_fields_set contains the field
        if self.avatar is None and "avatar" in self.model_fields_set:
            _dict['avatar'] = None

        # set to None if bot (nullable) is None
        # and model_fields_set contains the field
        if self.bot is None and "bot" in self.model_fields_set:
            _dict['bot'] = None

        # set to None if system (nullable) is None
        # and model_fields_set contains the field
        if self.system is None and "system" in self.model_fields_set:
            _dict['system'] = None

        # set to None if banner (nullable) is None
        # and model_fields_set contains the field
        if self.banner is None and "banner" in self.model_fields_set:
            _dict['banner'] = None

        # set to None if accent_color (nullable) is None
        # and model_fields_set contains the field
        if self.accent_color is None and "accent_color" in self.model_fields_set:
            _dict['accent_color'] = None

        # set to None if global_name (nullable) is None
        # and model_fields_set contains the field
        if self.global_name is None and "global_name" in self.model_fields_set:
            _dict['global_name'] = None

        # set to None if avatar_decoration_data (nullable) is None
        # and model_fields_set contains the field
        if self.avatar_decoration_data is None and "avatar_decoration_data" in self.model_fields_set:
            _dict['avatar_decoration_data'] = None

        # set to None if collectibles (nullable) is None
        # and model_fields_set contains the field
        if self.collectibles is None and "collectibles" in self.model_fields_set:
            _dict['collectibles'] = None

        # set to None if primary_guild (nullable) is None
        # and model_fields_set contains the field
        if self.primary_guild is None and "primary_guild" in self.model_fields_set:
            _dict['primary_guild'] = None

        # set to None if email (nullable) is None
        # and model_fields_set contains the field
        if self.email is None and "email" in self.model_fields_set:
            _dict['email'] = None

        # set to None if verified (nullable) is None
        # and model_fields_set contains the field
        if self.verified is None and "verified" in self.model_fields_set:
            _dict['verified'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of UserPIIResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        # raise errors for additional fields in the input
        for _key in obj.keys():
            if _key not in cls.__properties:
                raise ValueError("Error due to additional fields (not defined in UserPIIResponse) in the input: " + _key)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "username": obj.get("username"),
            "avatar": obj.get("avatar"),
            "discriminator": obj.get("discriminator"),
            "public_flags": obj.get("public_flags"),
            "flags": obj.get("flags"),
            "bot": obj.get("bot"),
            "system": obj.get("system"),
            "banner": obj.get("banner"),
            "accent_color": obj.get("accent_color"),
            "global_name": obj.get("global_name"),
            "avatar_decoration_data": UserAvatarDecorationResponse.from_dict(obj["avatar_decoration_data"]) if obj.get("avatar_decoration_data") is not None else None,
            "collectibles": UserCollectiblesResponse.from_dict(obj["collectibles"]) if obj.get("collectibles") is not None else None,
            "primary_guild": UserPrimaryGuildResponse.from_dict(obj["primary_guild"]) if obj.get("primary_guild") is not None else None,
            "mfa_enabled": obj.get("mfa_enabled"),
            "locale": obj.get("locale"),
            "premium_type": obj.get("premium_type"),
            "email": obj.get("email"),
            "verified": obj.get("verified")
        })
        return _obj


