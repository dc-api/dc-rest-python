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
from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from dc_rest.models.basic_message_response_components_inner import BasicMessageResponseComponentsInner
from dc_rest.models.get_sticker200_response import GetSticker200Response
from dc_rest.models.message_attachment_response import MessageAttachmentResponse
from dc_rest.models.message_embed_response import MessageEmbedResponse
from dc_rest.models.message_sticker_item_response import MessageStickerItemResponse
from dc_rest.models.resolved_objects_response import ResolvedObjectsResponse
from dc_rest.models.user_response import UserResponse
from typing import Optional, Set
from typing_extensions import Self

class MinimalContentMessageResponse(BaseModel):
    """
    MinimalContentMessageResponse
    """ # noqa: E501
    type: StrictInt
    content: StrictStr
    mentions: List[UserResponse]
    mention_roles: List[Annotated[str, Field(strict=True)]]
    attachments: List[MessageAttachmentResponse]
    embeds: List[MessageEmbedResponse]
    timestamp: datetime
    edited_timestamp: Optional[datetime] = None
    flags: StrictInt
    components: List[BasicMessageResponseComponentsInner]
    resolved: Optional[ResolvedObjectsResponse] = None
    stickers: Optional[List[GetSticker200Response]] = None
    sticker_items: Optional[List[MessageStickerItemResponse]] = None
    __properties: ClassVar[List[str]] = ["type", "content", "mentions", "mention_roles", "attachments", "embeds", "timestamp", "edited_timestamp", "flags", "components", "resolved", "stickers", "sticker_items"]

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
        """Create an instance of MinimalContentMessageResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in mentions (list)
        _items = []
        if self.mentions:
            for _item_mentions in self.mentions:
                if _item_mentions:
                    _items.append(_item_mentions.to_dict())
            _dict['mentions'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in attachments (list)
        _items = []
        if self.attachments:
            for _item_attachments in self.attachments:
                if _item_attachments:
                    _items.append(_item_attachments.to_dict())
            _dict['attachments'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in embeds (list)
        _items = []
        if self.embeds:
            for _item_embeds in self.embeds:
                if _item_embeds:
                    _items.append(_item_embeds.to_dict())
            _dict['embeds'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in components (list)
        _items = []
        if self.components:
            for _item_components in self.components:
                if _item_components:
                    _items.append(_item_components.to_dict())
            _dict['components'] = _items
        # override the default output from pydantic by calling `to_dict()` of resolved
        if self.resolved:
            _dict['resolved'] = self.resolved.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in stickers (list)
        _items = []
        if self.stickers:
            for _item_stickers in self.stickers:
                if _item_stickers:
                    _items.append(_item_stickers.to_dict())
            _dict['stickers'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in sticker_items (list)
        _items = []
        if self.sticker_items:
            for _item_sticker_items in self.sticker_items:
                if _item_sticker_items:
                    _items.append(_item_sticker_items.to_dict())
            _dict['sticker_items'] = _items
        # set to None if edited_timestamp (nullable) is None
        # and model_fields_set contains the field
        if self.edited_timestamp is None and "edited_timestamp" in self.model_fields_set:
            _dict['edited_timestamp'] = None

        # set to None if resolved (nullable) is None
        # and model_fields_set contains the field
        if self.resolved is None and "resolved" in self.model_fields_set:
            _dict['resolved'] = None

        # set to None if stickers (nullable) is None
        # and model_fields_set contains the field
        if self.stickers is None and "stickers" in self.model_fields_set:
            _dict['stickers'] = None

        # set to None if sticker_items (nullable) is None
        # and model_fields_set contains the field
        if self.sticker_items is None and "sticker_items" in self.model_fields_set:
            _dict['sticker_items'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of MinimalContentMessageResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        # raise errors for additional fields in the input
        for _key in obj.keys():
            if _key not in cls.__properties:
                raise ValueError("Error due to additional fields (not defined in MinimalContentMessageResponse) in the input: " + _key)

        _obj = cls.model_validate({
            "type": obj.get("type"),
            "content": obj.get("content"),
            "mentions": [UserResponse.from_dict(_item) for _item in obj["mentions"]] if obj.get("mentions") is not None else None,
            "mention_roles": obj.get("mention_roles"),
            "attachments": [MessageAttachmentResponse.from_dict(_item) for _item in obj["attachments"]] if obj.get("attachments") is not None else None,
            "embeds": [MessageEmbedResponse.from_dict(_item) for _item in obj["embeds"]] if obj.get("embeds") is not None else None,
            "timestamp": obj.get("timestamp"),
            "edited_timestamp": obj.get("edited_timestamp"),
            "flags": obj.get("flags"),
            "components": [BasicMessageResponseComponentsInner.from_dict(_item) for _item in obj["components"]] if obj.get("components") is not None else None,
            "resolved": ResolvedObjectsResponse.from_dict(obj["resolved"]) if obj.get("resolved") is not None else None,
            "stickers": [GetSticker200Response.from_dict(_item) for _item in obj["stickers"]] if obj.get("stickers") is not None else None,
            "sticker_items": [MessageStickerItemResponse.from_dict(_item) for _item in obj["sticker_items"]] if obj.get("sticker_items") is not None else None
        })
        return _obj


