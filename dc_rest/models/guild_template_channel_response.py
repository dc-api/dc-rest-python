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
from dc_rest.models.channel_permission_overwrite_response import ChannelPermissionOverwriteResponse
from dc_rest.models.default_reaction_emoji_response import DefaultReactionEmojiResponse
from dc_rest.models.guild_template_channel_tags import GuildTemplateChannelTags
from typing import Optional, Set
from typing_extensions import Self

class GuildTemplateChannelResponse(BaseModel):
    """
    GuildTemplateChannelResponse
    """ # noqa: E501
    id: Optional[StrictInt] = None
    type: StrictInt
    name: Optional[StrictStr] = None
    position: Optional[StrictInt] = None
    topic: Optional[StrictStr] = None
    bitrate: StrictInt
    user_limit: StrictInt
    nsfw: StrictBool
    rate_limit_per_user: StrictInt
    parent_id: Optional[Annotated[str, Field(strict=True)]] = None
    default_auto_archive_duration: Optional[StrictInt] = None
    permission_overwrites: List[Optional[ChannelPermissionOverwriteResponse]]
    available_tags: Optional[List[GuildTemplateChannelTags]] = None
    template: StrictStr
    default_reaction_emoji: Optional[DefaultReactionEmojiResponse] = None
    default_thread_rate_limit_per_user: Optional[StrictInt] = None
    default_sort_order: Optional[StrictInt] = None
    default_forum_layout: Optional[StrictInt] = None
    default_tag_setting: Optional[StrictStr] = None
    icon_emoji: Optional[Dict[str, Any]] = None
    theme_color: Optional[StrictInt] = None
    __properties: ClassVar[List[str]] = ["id", "type", "name", "position", "topic", "bitrate", "user_limit", "nsfw", "rate_limit_per_user", "parent_id", "default_auto_archive_duration", "permission_overwrites", "available_tags", "template", "default_reaction_emoji", "default_thread_rate_limit_per_user", "default_sort_order", "default_forum_layout", "default_tag_setting", "icon_emoji", "theme_color"]

    @field_validator('parent_id')
    def parent_id_validate_regular_expression(cls, value):
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
        """Create an instance of GuildTemplateChannelResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in available_tags (list)
        _items = []
        if self.available_tags:
            for _item_available_tags in self.available_tags:
                if _item_available_tags:
                    _items.append(_item_available_tags.to_dict())
            _dict['available_tags'] = _items
        # override the default output from pydantic by calling `to_dict()` of default_reaction_emoji
        if self.default_reaction_emoji:
            _dict['default_reaction_emoji'] = self.default_reaction_emoji.to_dict()
        # set to None if id (nullable) is None
        # and model_fields_set contains the field
        if self.id is None and "id" in self.model_fields_set:
            _dict['id'] = None

        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        # set to None if position (nullable) is None
        # and model_fields_set contains the field
        if self.position is None and "position" in self.model_fields_set:
            _dict['position'] = None

        # set to None if topic (nullable) is None
        # and model_fields_set contains the field
        if self.topic is None and "topic" in self.model_fields_set:
            _dict['topic'] = None

        # set to None if available_tags (nullable) is None
        # and model_fields_set contains the field
        if self.available_tags is None and "available_tags" in self.model_fields_set:
            _dict['available_tags'] = None

        # set to None if default_reaction_emoji (nullable) is None
        # and model_fields_set contains the field
        if self.default_reaction_emoji is None and "default_reaction_emoji" in self.model_fields_set:
            _dict['default_reaction_emoji'] = None

        # set to None if default_thread_rate_limit_per_user (nullable) is None
        # and model_fields_set contains the field
        if self.default_thread_rate_limit_per_user is None and "default_thread_rate_limit_per_user" in self.model_fields_set:
            _dict['default_thread_rate_limit_per_user'] = None

        # set to None if theme_color (nullable) is None
        # and model_fields_set contains the field
        if self.theme_color is None and "theme_color" in self.model_fields_set:
            _dict['theme_color'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GuildTemplateChannelResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        # raise errors for additional fields in the input
        for _key in obj.keys():
            if _key not in cls.__properties:
                raise ValueError("Error due to additional fields (not defined in GuildTemplateChannelResponse) in the input: " + _key)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "type": obj.get("type"),
            "name": obj.get("name"),
            "position": obj.get("position"),
            "topic": obj.get("topic"),
            "bitrate": obj.get("bitrate"),
            "user_limit": obj.get("user_limit"),
            "nsfw": obj.get("nsfw"),
            "rate_limit_per_user": obj.get("rate_limit_per_user"),
            "parent_id": obj.get("parent_id"),
            "default_auto_archive_duration": obj.get("default_auto_archive_duration"),
            "permission_overwrites": [ChannelPermissionOverwriteResponse.from_dict(_item) for _item in obj["permission_overwrites"]] if obj.get("permission_overwrites") is not None else None,
            "available_tags": [GuildTemplateChannelTags.from_dict(_item) for _item in obj["available_tags"]] if obj.get("available_tags") is not None else None,
            "template": obj.get("template"),
            "default_reaction_emoji": DefaultReactionEmojiResponse.from_dict(obj["default_reaction_emoji"]) if obj.get("default_reaction_emoji") is not None else None,
            "default_thread_rate_limit_per_user": obj.get("default_thread_rate_limit_per_user"),
            "default_sort_order": obj.get("default_sort_order"),
            "default_forum_layout": obj.get("default_forum_layout"),
            "default_tag_setting": obj.get("default_tag_setting"),
            "icon_emoji": obj.get("icon_emoji"),
            "theme_color": obj.get("theme_color")
        })
        return _obj


