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
from dc_rest.models.channel_permission_overwrite_request import ChannelPermissionOverwriteRequest
from dc_rest.models.create_or_update_thread_tag_request import CreateOrUpdateThreadTagRequest
from dc_rest.models.update_default_reaction_emoji_request import UpdateDefaultReactionEmojiRequest
from typing import Optional, Set
from typing_extensions import Self

class CreateGuildRequestChannelItem(BaseModel):
    """
    CreateGuildRequestChannelItem
    """ # noqa: E501
    type: Optional[StrictInt] = None
    name: Annotated[str, Field(min_length=1, strict=True, max_length=100)]
    position: Optional[Annotated[int, Field(strict=True, ge=0)]] = None
    topic: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=4096)]] = None
    bitrate: Optional[Annotated[int, Field(strict=True, ge=8000)]] = None
    user_limit: Optional[Annotated[int, Field(strict=True, ge=0)]] = None
    nsfw: Optional[StrictBool] = None
    rate_limit_per_user: Optional[Annotated[int, Field(le=21600, strict=True, ge=0)]] = None
    parent_id: Optional[Annotated[str, Field(strict=True)]] = None
    permission_overwrites: Optional[Annotated[List[ChannelPermissionOverwriteRequest], Field(max_length=100)]] = None
    rtc_region: Optional[StrictStr] = None
    video_quality_mode: Optional[StrictInt] = None
    default_auto_archive_duration: Optional[StrictInt] = None
    default_reaction_emoji: Optional[UpdateDefaultReactionEmojiRequest] = None
    default_thread_rate_limit_per_user: Optional[Annotated[int, Field(le=21600, strict=True, ge=0)]] = None
    default_sort_order: Optional[StrictInt] = None
    default_forum_layout: Optional[StrictInt] = None
    default_tag_setting: Optional[StrictStr] = None
    id: Optional[Annotated[str, Field(strict=True)]] = None
    available_tags: Optional[Annotated[List[CreateOrUpdateThreadTagRequest], Field(max_length=20)]] = None
    __properties: ClassVar[List[str]] = ["type", "name", "position", "topic", "bitrate", "user_limit", "nsfw", "rate_limit_per_user", "parent_id", "permission_overwrites", "rtc_region", "video_quality_mode", "default_auto_archive_duration", "default_reaction_emoji", "default_thread_rate_limit_per_user", "default_sort_order", "default_forum_layout", "default_tag_setting", "id", "available_tags"]

    @field_validator('parent_id')
    def parent_id_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^(0|[1-9][0-9]*)$", value):
            raise ValueError(r"must validate the regular expression /^(0|[1-9][0-9]*)$/")
        return value

    @field_validator('id')
    def id_validate_regular_expression(cls, value):
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
        """Create an instance of CreateGuildRequestChannelItem from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in permission_overwrites (list)
        _items = []
        if self.permission_overwrites:
            for _item_permission_overwrites in self.permission_overwrites:
                if _item_permission_overwrites:
                    _items.append(_item_permission_overwrites.to_dict())
            _dict['permission_overwrites'] = _items
        # override the default output from pydantic by calling `to_dict()` of default_reaction_emoji
        if self.default_reaction_emoji:
            _dict['default_reaction_emoji'] = self.default_reaction_emoji.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in available_tags (list)
        _items = []
        if self.available_tags:
            for _item_available_tags in self.available_tags:
                if _item_available_tags:
                    _items.append(_item_available_tags.to_dict())
            _dict['available_tags'] = _items
        # set to None if type (nullable) is None
        # and model_fields_set contains the field
        if self.type is None and "type" in self.model_fields_set:
            _dict['type'] = None

        # set to None if position (nullable) is None
        # and model_fields_set contains the field
        if self.position is None and "position" in self.model_fields_set:
            _dict['position'] = None

        # set to None if topic (nullable) is None
        # and model_fields_set contains the field
        if self.topic is None and "topic" in self.model_fields_set:
            _dict['topic'] = None

        # set to None if bitrate (nullable) is None
        # and model_fields_set contains the field
        if self.bitrate is None and "bitrate" in self.model_fields_set:
            _dict['bitrate'] = None

        # set to None if user_limit (nullable) is None
        # and model_fields_set contains the field
        if self.user_limit is None and "user_limit" in self.model_fields_set:
            _dict['user_limit'] = None

        # set to None if nsfw (nullable) is None
        # and model_fields_set contains the field
        if self.nsfw is None and "nsfw" in self.model_fields_set:
            _dict['nsfw'] = None

        # set to None if rate_limit_per_user (nullable) is None
        # and model_fields_set contains the field
        if self.rate_limit_per_user is None and "rate_limit_per_user" in self.model_fields_set:
            _dict['rate_limit_per_user'] = None

        # set to None if permission_overwrites (nullable) is None
        # and model_fields_set contains the field
        if self.permission_overwrites is None and "permission_overwrites" in self.model_fields_set:
            _dict['permission_overwrites'] = None

        # set to None if rtc_region (nullable) is None
        # and model_fields_set contains the field
        if self.rtc_region is None and "rtc_region" in self.model_fields_set:
            _dict['rtc_region'] = None

        # set to None if default_reaction_emoji (nullable) is None
        # and model_fields_set contains the field
        if self.default_reaction_emoji is None and "default_reaction_emoji" in self.model_fields_set:
            _dict['default_reaction_emoji'] = None

        # set to None if default_thread_rate_limit_per_user (nullable) is None
        # and model_fields_set contains the field
        if self.default_thread_rate_limit_per_user is None and "default_thread_rate_limit_per_user" in self.model_fields_set:
            _dict['default_thread_rate_limit_per_user'] = None

        # set to None if available_tags (nullable) is None
        # and model_fields_set contains the field
        if self.available_tags is None and "available_tags" in self.model_fields_set:
            _dict['available_tags'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CreateGuildRequestChannelItem from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        # raise errors for additional fields in the input
        for _key in obj.keys():
            if _key not in cls.__properties:
                raise ValueError("Error due to additional fields (not defined in CreateGuildRequestChannelItem) in the input: " + _key)

        _obj = cls.model_validate({
            "type": obj.get("type"),
            "name": obj.get("name"),
            "position": obj.get("position"),
            "topic": obj.get("topic"),
            "bitrate": obj.get("bitrate"),
            "user_limit": obj.get("user_limit"),
            "nsfw": obj.get("nsfw"),
            "rate_limit_per_user": obj.get("rate_limit_per_user"),
            "parent_id": obj.get("parent_id"),
            "permission_overwrites": [ChannelPermissionOverwriteRequest.from_dict(_item) for _item in obj["permission_overwrites"]] if obj.get("permission_overwrites") is not None else None,
            "rtc_region": obj.get("rtc_region"),
            "video_quality_mode": obj.get("video_quality_mode"),
            "default_auto_archive_duration": obj.get("default_auto_archive_duration"),
            "default_reaction_emoji": UpdateDefaultReactionEmojiRequest.from_dict(obj["default_reaction_emoji"]) if obj.get("default_reaction_emoji") is not None else None,
            "default_thread_rate_limit_per_user": obj.get("default_thread_rate_limit_per_user"),
            "default_sort_order": obj.get("default_sort_order"),
            "default_forum_layout": obj.get("default_forum_layout"),
            "default_tag_setting": obj.get("default_tag_setting"),
            "id": obj.get("id"),
            "available_tags": [CreateOrUpdateThreadTagRequest.from_dict(_item) for _item in obj["available_tags"]] if obj.get("available_tags") is not None else None
        })
        return _obj


