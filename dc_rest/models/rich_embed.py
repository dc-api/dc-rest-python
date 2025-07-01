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
from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from dc_rest.models.rich_embed_author import RichEmbedAuthor
from dc_rest.models.rich_embed_field import RichEmbedField
from dc_rest.models.rich_embed_footer import RichEmbedFooter
from dc_rest.models.rich_embed_image import RichEmbedImage
from dc_rest.models.rich_embed_provider import RichEmbedProvider
from dc_rest.models.rich_embed_thumbnail import RichEmbedThumbnail
from dc_rest.models.rich_embed_video import RichEmbedVideo
from typing import Optional, Set
from typing_extensions import Self

class RichEmbed(BaseModel):
    """
    RichEmbed
    """ # noqa: E501
    type: Optional[Annotated[str, Field(strict=True, max_length=152133)]] = None
    url: Optional[Annotated[str, Field(strict=True, max_length=2048)]] = None
    title: Optional[Annotated[str, Field(strict=True, max_length=256)]] = None
    color: Optional[Annotated[int, Field(le=16777215, strict=True, ge=0)]] = None
    timestamp: Optional[datetime] = None
    description: Optional[Annotated[str, Field(strict=True, max_length=4096)]] = None
    author: Optional[RichEmbedAuthor] = None
    image: Optional[RichEmbedImage] = None
    thumbnail: Optional[RichEmbedThumbnail] = None
    footer: Optional[RichEmbedFooter] = None
    fields: Optional[Annotated[List[RichEmbedField], Field(max_length=25)]] = None
    provider: Optional[RichEmbedProvider] = None
    video: Optional[RichEmbedVideo] = None
    __properties: ClassVar[List[str]] = ["type", "url", "title", "color", "timestamp", "description", "author", "image", "thumbnail", "footer", "fields", "provider", "video"]

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
        """Create an instance of RichEmbed from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of author
        if self.author:
            _dict['author'] = self.author.to_dict()
        # override the default output from pydantic by calling `to_dict()` of image
        if self.image:
            _dict['image'] = self.image.to_dict()
        # override the default output from pydantic by calling `to_dict()` of thumbnail
        if self.thumbnail:
            _dict['thumbnail'] = self.thumbnail.to_dict()
        # override the default output from pydantic by calling `to_dict()` of footer
        if self.footer:
            _dict['footer'] = self.footer.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in fields (list)
        _items = []
        if self.fields:
            for _item_fields in self.fields:
                if _item_fields:
                    _items.append(_item_fields.to_dict())
            _dict['fields'] = _items
        # override the default output from pydantic by calling `to_dict()` of provider
        if self.provider:
            _dict['provider'] = self.provider.to_dict()
        # override the default output from pydantic by calling `to_dict()` of video
        if self.video:
            _dict['video'] = self.video.to_dict()
        # set to None if type (nullable) is None
        # and model_fields_set contains the field
        if self.type is None and "type" in self.model_fields_set:
            _dict['type'] = None

        # set to None if url (nullable) is None
        # and model_fields_set contains the field
        if self.url is None and "url" in self.model_fields_set:
            _dict['url'] = None

        # set to None if title (nullable) is None
        # and model_fields_set contains the field
        if self.title is None and "title" in self.model_fields_set:
            _dict['title'] = None

        # set to None if color (nullable) is None
        # and model_fields_set contains the field
        if self.color is None and "color" in self.model_fields_set:
            _dict['color'] = None

        # set to None if timestamp (nullable) is None
        # and model_fields_set contains the field
        if self.timestamp is None and "timestamp" in self.model_fields_set:
            _dict['timestamp'] = None

        # set to None if description (nullable) is None
        # and model_fields_set contains the field
        if self.description is None and "description" in self.model_fields_set:
            _dict['description'] = None

        # set to None if author (nullable) is None
        # and model_fields_set contains the field
        if self.author is None and "author" in self.model_fields_set:
            _dict['author'] = None

        # set to None if image (nullable) is None
        # and model_fields_set contains the field
        if self.image is None and "image" in self.model_fields_set:
            _dict['image'] = None

        # set to None if thumbnail (nullable) is None
        # and model_fields_set contains the field
        if self.thumbnail is None and "thumbnail" in self.model_fields_set:
            _dict['thumbnail'] = None

        # set to None if footer (nullable) is None
        # and model_fields_set contains the field
        if self.footer is None and "footer" in self.model_fields_set:
            _dict['footer'] = None

        # set to None if fields (nullable) is None
        # and model_fields_set contains the field
        if self.fields is None and "fields" in self.model_fields_set:
            _dict['fields'] = None

        # set to None if provider (nullable) is None
        # and model_fields_set contains the field
        if self.provider is None and "provider" in self.model_fields_set:
            _dict['provider'] = None

        # set to None if video (nullable) is None
        # and model_fields_set contains the field
        if self.video is None and "video" in self.model_fields_set:
            _dict['video'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RichEmbed from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        # raise errors for additional fields in the input
        for _key in obj.keys():
            if _key not in cls.__properties:
                raise ValueError("Error due to additional fields (not defined in RichEmbed) in the input: " + _key)

        _obj = cls.model_validate({
            "type": obj.get("type"),
            "url": obj.get("url"),
            "title": obj.get("title"),
            "color": obj.get("color"),
            "timestamp": obj.get("timestamp"),
            "description": obj.get("description"),
            "author": RichEmbedAuthor.from_dict(obj["author"]) if obj.get("author") is not None else None,
            "image": RichEmbedImage.from_dict(obj["image"]) if obj.get("image") is not None else None,
            "thumbnail": RichEmbedThumbnail.from_dict(obj["thumbnail"]) if obj.get("thumbnail") is not None else None,
            "footer": RichEmbedFooter.from_dict(obj["footer"]) if obj.get("footer") is not None else None,
            "fields": [RichEmbedField.from_dict(_item) for _item in obj["fields"]] if obj.get("fields") is not None else None,
            "provider": RichEmbedProvider.from_dict(obj["provider"]) if obj.get("provider") is not None else None,
            "video": RichEmbedVideo.from_dict(obj["video"]) if obj.get("video") is not None else None
        })
        return _obj


