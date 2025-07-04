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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from dc_rest.models.webhook_slack_embed_field import WebhookSlackEmbedField
from typing import Optional, Set
from typing_extensions import Self

class WebhookSlackEmbed(BaseModel):
    """
    WebhookSlackEmbed
    """ # noqa: E501
    title: Optional[Annotated[str, Field(strict=True, max_length=152133)]] = None
    title_link: Optional[Annotated[str, Field(strict=True, max_length=2048)]] = None
    text: Optional[Annotated[str, Field(strict=True, max_length=152133)]] = None
    color: Optional[Annotated[str, Field(strict=True, max_length=7)]] = None
    ts: Optional[StrictInt] = None
    pretext: Optional[Annotated[str, Field(strict=True, max_length=152133)]] = None
    footer: Optional[Annotated[str, Field(strict=True, max_length=152133)]] = None
    footer_icon: Optional[Annotated[str, Field(strict=True, max_length=2048)]] = None
    author_name: Optional[Annotated[str, Field(strict=True, max_length=152133)]] = None
    author_link: Optional[Annotated[str, Field(strict=True, max_length=2048)]] = None
    author_icon: Optional[Annotated[str, Field(strict=True, max_length=2048)]] = None
    image_url: Optional[Annotated[str, Field(strict=True, max_length=2048)]] = None
    thumb_url: Optional[Annotated[str, Field(strict=True, max_length=2048)]] = None
    fields: Optional[Annotated[List[WebhookSlackEmbedField], Field(max_length=1521)]] = None
    __properties: ClassVar[List[str]] = ["title", "title_link", "text", "color", "ts", "pretext", "footer", "footer_icon", "author_name", "author_link", "author_icon", "image_url", "thumb_url", "fields"]

    @field_validator('color')
    def color_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^#(([0-9a-fA-F]{2}){3}|([0-9a-fA-F]){3})$", value):
            raise ValueError(r"must validate the regular expression /^#(([0-9a-fA-F]{2}){3}|([0-9a-fA-F]){3})$/")
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
        """Create an instance of WebhookSlackEmbed from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in fields (list)
        _items = []
        if self.fields:
            for _item_fields in self.fields:
                if _item_fields:
                    _items.append(_item_fields.to_dict())
            _dict['fields'] = _items
        # set to None if title (nullable) is None
        # and model_fields_set contains the field
        if self.title is None and "title" in self.model_fields_set:
            _dict['title'] = None

        # set to None if title_link (nullable) is None
        # and model_fields_set contains the field
        if self.title_link is None and "title_link" in self.model_fields_set:
            _dict['title_link'] = None

        # set to None if text (nullable) is None
        # and model_fields_set contains the field
        if self.text is None and "text" in self.model_fields_set:
            _dict['text'] = None

        # set to None if color (nullable) is None
        # and model_fields_set contains the field
        if self.color is None and "color" in self.model_fields_set:
            _dict['color'] = None

        # set to None if ts (nullable) is None
        # and model_fields_set contains the field
        if self.ts is None and "ts" in self.model_fields_set:
            _dict['ts'] = None

        # set to None if pretext (nullable) is None
        # and model_fields_set contains the field
        if self.pretext is None and "pretext" in self.model_fields_set:
            _dict['pretext'] = None

        # set to None if footer (nullable) is None
        # and model_fields_set contains the field
        if self.footer is None and "footer" in self.model_fields_set:
            _dict['footer'] = None

        # set to None if footer_icon (nullable) is None
        # and model_fields_set contains the field
        if self.footer_icon is None and "footer_icon" in self.model_fields_set:
            _dict['footer_icon'] = None

        # set to None if author_name (nullable) is None
        # and model_fields_set contains the field
        if self.author_name is None and "author_name" in self.model_fields_set:
            _dict['author_name'] = None

        # set to None if author_link (nullable) is None
        # and model_fields_set contains the field
        if self.author_link is None and "author_link" in self.model_fields_set:
            _dict['author_link'] = None

        # set to None if author_icon (nullable) is None
        # and model_fields_set contains the field
        if self.author_icon is None and "author_icon" in self.model_fields_set:
            _dict['author_icon'] = None

        # set to None if image_url (nullable) is None
        # and model_fields_set contains the field
        if self.image_url is None and "image_url" in self.model_fields_set:
            _dict['image_url'] = None

        # set to None if thumb_url (nullable) is None
        # and model_fields_set contains the field
        if self.thumb_url is None and "thumb_url" in self.model_fields_set:
            _dict['thumb_url'] = None

        # set to None if fields (nullable) is None
        # and model_fields_set contains the field
        if self.fields is None and "fields" in self.model_fields_set:
            _dict['fields'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of WebhookSlackEmbed from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        # raise errors for additional fields in the input
        for _key in obj.keys():
            if _key not in cls.__properties:
                raise ValueError("Error due to additional fields (not defined in WebhookSlackEmbed) in the input: " + _key)

        _obj = cls.model_validate({
            "title": obj.get("title"),
            "title_link": obj.get("title_link"),
            "text": obj.get("text"),
            "color": obj.get("color"),
            "ts": obj.get("ts"),
            "pretext": obj.get("pretext"),
            "footer": obj.get("footer"),
            "footer_icon": obj.get("footer_icon"),
            "author_name": obj.get("author_name"),
            "author_link": obj.get("author_link"),
            "author_icon": obj.get("author_icon"),
            "image_url": obj.get("image_url"),
            "thumb_url": obj.get("thumb_url"),
            "fields": [WebhookSlackEmbedField.from_dict(_item) for _item in obj["fields"]] if obj.get("fields") is not None else None
        })
        return _obj


