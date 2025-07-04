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

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from dc_rest.models.invite_application_response import InviteApplicationResponse
from dc_rest.models.invite_channel_response import InviteChannelResponse
from dc_rest.models.invite_guild_response import InviteGuildResponse
from dc_rest.models.scheduled_event_response import ScheduledEventResponse
from dc_rest.models.user_response import UserResponse
from typing import Optional, Set
from typing_extensions import Self

class GuildInviteResponse(BaseModel):
    """
    GuildInviteResponse
    """ # noqa: E501
    type: Optional[StrictInt] = None
    code: StrictStr
    inviter: Optional[UserResponse] = None
    max_age: Optional[StrictInt] = None
    created_at: Optional[datetime] = None
    expires_at: Optional[datetime] = None
    is_contact: Optional[StrictBool] = None
    flags: Optional[StrictInt] = None
    guild: Optional[InviteGuildResponse] = None
    guild_id: Optional[Annotated[str, Field(strict=True)]] = None
    channel: Optional[InviteChannelResponse] = None
    target_type: Optional[StrictInt] = None
    target_user: Optional[UserResponse] = None
    target_application: Optional[InviteApplicationResponse] = None
    guild_scheduled_event: Optional[ScheduledEventResponse] = None
    uses: Optional[StrictInt] = None
    max_uses: Optional[StrictInt] = None
    temporary: Optional[StrictBool] = None
    approximate_member_count: Optional[StrictInt] = None
    approximate_presence_count: Optional[StrictInt] = None
    is_nickname_changeable: Optional[StrictBool] = None
    __properties: ClassVar[List[str]] = ["type", "code", "inviter", "max_age", "created_at", "expires_at", "is_contact", "flags", "guild", "guild_id", "channel", "target_type", "target_user", "target_application", "guild_scheduled_event", "uses", "max_uses", "temporary", "approximate_member_count", "approximate_presence_count", "is_nickname_changeable"]

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
        """Create an instance of GuildInviteResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of inviter
        if self.inviter:
            _dict['inviter'] = self.inviter.to_dict()
        # override the default output from pydantic by calling `to_dict()` of guild
        if self.guild:
            _dict['guild'] = self.guild.to_dict()
        # override the default output from pydantic by calling `to_dict()` of channel
        if self.channel:
            _dict['channel'] = self.channel.to_dict()
        # override the default output from pydantic by calling `to_dict()` of target_user
        if self.target_user:
            _dict['target_user'] = self.target_user.to_dict()
        # override the default output from pydantic by calling `to_dict()` of target_application
        if self.target_application:
            _dict['target_application'] = self.target_application.to_dict()
        # override the default output from pydantic by calling `to_dict()` of guild_scheduled_event
        if self.guild_scheduled_event:
            _dict['guild_scheduled_event'] = self.guild_scheduled_event.to_dict()
        # set to None if type (nullable) is None
        # and model_fields_set contains the field
        if self.type is None and "type" in self.model_fields_set:
            _dict['type'] = None

        # set to None if inviter (nullable) is None
        # and model_fields_set contains the field
        if self.inviter is None and "inviter" in self.model_fields_set:
            _dict['inviter'] = None

        # set to None if max_age (nullable) is None
        # and model_fields_set contains the field
        if self.max_age is None and "max_age" in self.model_fields_set:
            _dict['max_age'] = None

        # set to None if created_at (nullable) is None
        # and model_fields_set contains the field
        if self.created_at is None and "created_at" in self.model_fields_set:
            _dict['created_at'] = None

        # set to None if expires_at (nullable) is None
        # and model_fields_set contains the field
        if self.expires_at is None and "expires_at" in self.model_fields_set:
            _dict['expires_at'] = None

        # set to None if is_contact (nullable) is None
        # and model_fields_set contains the field
        if self.is_contact is None and "is_contact" in self.model_fields_set:
            _dict['is_contact'] = None

        # set to None if flags (nullable) is None
        # and model_fields_set contains the field
        if self.flags is None and "flags" in self.model_fields_set:
            _dict['flags'] = None

        # set to None if guild (nullable) is None
        # and model_fields_set contains the field
        if self.guild is None and "guild" in self.model_fields_set:
            _dict['guild'] = None

        # set to None if channel (nullable) is None
        # and model_fields_set contains the field
        if self.channel is None and "channel" in self.model_fields_set:
            _dict['channel'] = None

        # set to None if target_type (nullable) is None
        # and model_fields_set contains the field
        if self.target_type is None and "target_type" in self.model_fields_set:
            _dict['target_type'] = None

        # set to None if target_user (nullable) is None
        # and model_fields_set contains the field
        if self.target_user is None and "target_user" in self.model_fields_set:
            _dict['target_user'] = None

        # set to None if target_application (nullable) is None
        # and model_fields_set contains the field
        if self.target_application is None and "target_application" in self.model_fields_set:
            _dict['target_application'] = None

        # set to None if guild_scheduled_event (nullable) is None
        # and model_fields_set contains the field
        if self.guild_scheduled_event is None and "guild_scheduled_event" in self.model_fields_set:
            _dict['guild_scheduled_event'] = None

        # set to None if uses (nullable) is None
        # and model_fields_set contains the field
        if self.uses is None and "uses" in self.model_fields_set:
            _dict['uses'] = None

        # set to None if max_uses (nullable) is None
        # and model_fields_set contains the field
        if self.max_uses is None and "max_uses" in self.model_fields_set:
            _dict['max_uses'] = None

        # set to None if temporary (nullable) is None
        # and model_fields_set contains the field
        if self.temporary is None and "temporary" in self.model_fields_set:
            _dict['temporary'] = None

        # set to None if approximate_member_count (nullable) is None
        # and model_fields_set contains the field
        if self.approximate_member_count is None and "approximate_member_count" in self.model_fields_set:
            _dict['approximate_member_count'] = None

        # set to None if approximate_presence_count (nullable) is None
        # and model_fields_set contains the field
        if self.approximate_presence_count is None and "approximate_presence_count" in self.model_fields_set:
            _dict['approximate_presence_count'] = None

        # set to None if is_nickname_changeable (nullable) is None
        # and model_fields_set contains the field
        if self.is_nickname_changeable is None and "is_nickname_changeable" in self.model_fields_set:
            _dict['is_nickname_changeable'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GuildInviteResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        # raise errors for additional fields in the input
        for _key in obj.keys():
            if _key not in cls.__properties:
                raise ValueError("Error due to additional fields (not defined in GuildInviteResponse) in the input: " + _key)

        _obj = cls.model_validate({
            "type": obj.get("type"),
            "code": obj.get("code"),
            "inviter": UserResponse.from_dict(obj["inviter"]) if obj.get("inviter") is not None else None,
            "max_age": obj.get("max_age"),
            "created_at": obj.get("created_at"),
            "expires_at": obj.get("expires_at"),
            "is_contact": obj.get("is_contact"),
            "flags": obj.get("flags"),
            "guild": InviteGuildResponse.from_dict(obj["guild"]) if obj.get("guild") is not None else None,
            "guild_id": obj.get("guild_id"),
            "channel": InviteChannelResponse.from_dict(obj["channel"]) if obj.get("channel") is not None else None,
            "target_type": obj.get("target_type"),
            "target_user": UserResponse.from_dict(obj["target_user"]) if obj.get("target_user") is not None else None,
            "target_application": InviteApplicationResponse.from_dict(obj["target_application"]) if obj.get("target_application") is not None else None,
            "guild_scheduled_event": ScheduledEventResponse.from_dict(obj["guild_scheduled_event"]) if obj.get("guild_scheduled_event") is not None else None,
            "uses": obj.get("uses"),
            "max_uses": obj.get("max_uses"),
            "temporary": obj.get("temporary"),
            "approximate_member_count": obj.get("approximate_member_count"),
            "approximate_presence_count": obj.get("approximate_presence_count"),
            "is_nickname_changeable": obj.get("is_nickname_changeable")
        })
        return _obj


