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

from pydantic import BaseModel, ConfigDict, Field, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from dc_rest.models.base_create_message_create_request_components_inner import BaseCreateMessageCreateRequestComponentsInner
from dc_rest.models.message_allowed_mentions_request import MessageAllowedMentionsRequest
from dc_rest.models.message_attachment_request import MessageAttachmentRequest
from dc_rest.models.rich_embed import RichEmbed
from typing import Optional, Set
from typing_extensions import Self

class IncomingWebhookUpdateForInteractionCallbackRequestPartial(BaseModel):
    """
    IncomingWebhookUpdateForInteractionCallbackRequestPartial
    """ # noqa: E501
    content: Optional[Annotated[str, Field(strict=True, max_length=2000)]] = None
    embeds: Optional[Annotated[List[RichEmbed], Field(max_length=10)]] = None
    allowed_mentions: Optional[MessageAllowedMentionsRequest] = None
    components: Optional[Annotated[List[BaseCreateMessageCreateRequestComponentsInner], Field(max_length=40)]] = None
    attachments: Optional[Annotated[List[MessageAttachmentRequest], Field(max_length=10)]] = None
    flags: Optional[StrictInt] = None
    __properties: ClassVar[List[str]] = ["content", "embeds", "allowed_mentions", "components", "attachments", "flags"]

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
        """Create an instance of IncomingWebhookUpdateForInteractionCallbackRequestPartial from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in embeds (list)
        _items = []
        if self.embeds:
            for _item_embeds in self.embeds:
                if _item_embeds:
                    _items.append(_item_embeds.to_dict())
            _dict['embeds'] = _items
        # override the default output from pydantic by calling `to_dict()` of allowed_mentions
        if self.allowed_mentions:
            _dict['allowed_mentions'] = self.allowed_mentions.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in components (list)
        _items = []
        if self.components:
            for _item_components in self.components:
                if _item_components:
                    _items.append(_item_components.to_dict())
            _dict['components'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in attachments (list)
        _items = []
        if self.attachments:
            for _item_attachments in self.attachments:
                if _item_attachments:
                    _items.append(_item_attachments.to_dict())
            _dict['attachments'] = _items
        # set to None if content (nullable) is None
        # and model_fields_set contains the field
        if self.content is None and "content" in self.model_fields_set:
            _dict['content'] = None

        # set to None if embeds (nullable) is None
        # and model_fields_set contains the field
        if self.embeds is None and "embeds" in self.model_fields_set:
            _dict['embeds'] = None

        # set to None if allowed_mentions (nullable) is None
        # and model_fields_set contains the field
        if self.allowed_mentions is None and "allowed_mentions" in self.model_fields_set:
            _dict['allowed_mentions'] = None

        # set to None if components (nullable) is None
        # and model_fields_set contains the field
        if self.components is None and "components" in self.model_fields_set:
            _dict['components'] = None

        # set to None if attachments (nullable) is None
        # and model_fields_set contains the field
        if self.attachments is None and "attachments" in self.model_fields_set:
            _dict['attachments'] = None

        # set to None if flags (nullable) is None
        # and model_fields_set contains the field
        if self.flags is None and "flags" in self.model_fields_set:
            _dict['flags'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of IncomingWebhookUpdateForInteractionCallbackRequestPartial from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        # raise errors for additional fields in the input
        for _key in obj.keys():
            if _key not in cls.__properties:
                raise ValueError("Error due to additional fields (not defined in IncomingWebhookUpdateForInteractionCallbackRequestPartial) in the input: " + _key)

        _obj = cls.model_validate({
            "content": obj.get("content"),
            "embeds": [RichEmbed.from_dict(_item) for _item in obj["embeds"]] if obj.get("embeds") is not None else None,
            "allowed_mentions": MessageAllowedMentionsRequest.from_dict(obj["allowed_mentions"]) if obj.get("allowed_mentions") is not None else None,
            "components": [BaseCreateMessageCreateRequestComponentsInner.from_dict(_item) for _item in obj["components"]] if obj.get("components") is not None else None,
            "attachments": [MessageAttachmentRequest.from_dict(_item) for _item in obj["attachments"]] if obj.get("attachments") is not None else None,
            "flags": obj.get("flags")
        })
        return _obj


