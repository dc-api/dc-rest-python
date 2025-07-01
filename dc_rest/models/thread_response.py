# coding: utf-8

"""
Discord HTTP API (Preview) - REST API Client
Preview of the Discord v10 HTTP API specification. See https://discord.com/developers/docs for more details.

## Metadata

- **Copyright**: Copyright (c) 2025 Qntx
- **Author**: ΣX <gitctrlx@gmail.com>
- **Version**: 10
- **Modified**: 2025-07-01T10:17:20.817322704Z[Etc/UTC]
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
from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from dc_rest.models.thread_member_response import ThreadMemberResponse
from dc_rest.models.thread_metadata_response import ThreadMetadataResponse
from typing import Optional, Set
from typing_extensions import Self

class ThreadResponse(BaseModel):
    """
    ThreadResponse
    """ # noqa: E501
    id: Annotated[str, Field(strict=True)]
    type: StrictInt
    last_message_id: Optional[Annotated[str, Field(strict=True)]] = None
    flags: StrictInt
    last_pin_timestamp: Optional[datetime] = None
    guild_id: Annotated[str, Field(strict=True)]
    name: StrictStr
    parent_id: Optional[Annotated[str, Field(strict=True)]] = None
    rate_limit_per_user: Optional[StrictInt] = None
    bitrate: Optional[StrictInt] = None
    user_limit: Optional[StrictInt] = None
    rtc_region: Optional[StrictStr] = None
    video_quality_mode: Optional[StrictInt] = None
    permissions: Optional[StrictStr] = None
    owner_id: Annotated[str, Field(strict=True)]
    thread_metadata: Optional[ThreadMetadataResponse] = None
    message_count: StrictInt
    member_count: StrictInt
    total_message_sent: StrictInt
    applied_tags: Optional[List[Annotated[str, Field(strict=True)]]] = None
    member: Optional[ThreadMemberResponse] = None
    __properties: ClassVar[List[str]] = ["id", "type", "last_message_id", "flags", "last_pin_timestamp", "guild_id", "name", "parent_id", "rate_limit_per_user", "bitrate", "user_limit", "rtc_region", "video_quality_mode", "permissions", "owner_id", "thread_metadata", "message_count", "member_count", "total_message_sent", "applied_tags", "member"]

    @field_validator('id')
    def id_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^(0|[1-9][0-9]*)$", value):
            raise ValueError(r"must validate the regular expression /^(0|[1-9][0-9]*)$/")
        return value

    @field_validator('last_message_id')
    def last_message_id_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^(0|[1-9][0-9]*)$", value):
            raise ValueError(r"must validate the regular expression /^(0|[1-9][0-9]*)$/")
        return value

    @field_validator('guild_id')
    def guild_id_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^(0|[1-9][0-9]*)$", value):
            raise ValueError(r"must validate the regular expression /^(0|[1-9][0-9]*)$/")
        return value

    @field_validator('parent_id')
    def parent_id_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^(0|[1-9][0-9]*)$", value):
            raise ValueError(r"must validate the regular expression /^(0|[1-9][0-9]*)$/")
        return value

    @field_validator('owner_id')
    def owner_id_validate_regular_expression(cls, value):
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
        """Create an instance of ThreadResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of thread_metadata
        if self.thread_metadata:
            _dict['thread_metadata'] = self.thread_metadata.to_dict()
        # override the default output from pydantic by calling `to_dict()` of member
        if self.member:
            _dict['member'] = self.member.to_dict()
        # set to None if last_pin_timestamp (nullable) is None
        # and model_fields_set contains the field
        if self.last_pin_timestamp is None and "last_pin_timestamp" in self.model_fields_set:
            _dict['last_pin_timestamp'] = None

        # set to None if rate_limit_per_user (nullable) is None
        # and model_fields_set contains the field
        if self.rate_limit_per_user is None and "rate_limit_per_user" in self.model_fields_set:
            _dict['rate_limit_per_user'] = None

        # set to None if bitrate (nullable) is None
        # and model_fields_set contains the field
        if self.bitrate is None and "bitrate" in self.model_fields_set:
            _dict['bitrate'] = None

        # set to None if user_limit (nullable) is None
        # and model_fields_set contains the field
        if self.user_limit is None and "user_limit" in self.model_fields_set:
            _dict['user_limit'] = None

        # set to None if rtc_region (nullable) is None
        # and model_fields_set contains the field
        if self.rtc_region is None and "rtc_region" in self.model_fields_set:
            _dict['rtc_region'] = None

        # set to None if permissions (nullable) is None
        # and model_fields_set contains the field
        if self.permissions is None and "permissions" in self.model_fields_set:
            _dict['permissions'] = None

        # set to None if thread_metadata (nullable) is None
        # and model_fields_set contains the field
        if self.thread_metadata is None and "thread_metadata" in self.model_fields_set:
            _dict['thread_metadata'] = None

        # set to None if applied_tags (nullable) is None
        # and model_fields_set contains the field
        if self.applied_tags is None and "applied_tags" in self.model_fields_set:
            _dict['applied_tags'] = None

        # set to None if member (nullable) is None
        # and model_fields_set contains the field
        if self.member is None and "member" in self.model_fields_set:
            _dict['member'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ThreadResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        # raise errors for additional fields in the input
        for _key in obj.keys():
            if _key not in cls.__properties:
                raise ValueError("Error due to additional fields (not defined in ThreadResponse) in the input: " + _key)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "type": obj.get("type"),
            "last_message_id": obj.get("last_message_id"),
            "flags": obj.get("flags"),
            "last_pin_timestamp": obj.get("last_pin_timestamp"),
            "guild_id": obj.get("guild_id"),
            "name": obj.get("name"),
            "parent_id": obj.get("parent_id"),
            "rate_limit_per_user": obj.get("rate_limit_per_user"),
            "bitrate": obj.get("bitrate"),
            "user_limit": obj.get("user_limit"),
            "rtc_region": obj.get("rtc_region"),
            "video_quality_mode": obj.get("video_quality_mode"),
            "permissions": obj.get("permissions"),
            "owner_id": obj.get("owner_id"),
            "thread_metadata": ThreadMetadataResponse.from_dict(obj["thread_metadata"]) if obj.get("thread_metadata") is not None else None,
            "message_count": obj.get("message_count"),
            "member_count": obj.get("member_count"),
            "total_message_sent": obj.get("total_message_sent"),
            "applied_tags": obj.get("applied_tags"),
            "member": ThreadMemberResponse.from_dict(obj["member"]) if obj.get("member") is not None else None
        })
        return _obj


