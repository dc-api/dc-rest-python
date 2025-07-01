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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class UpdateThreadRequestPartial(BaseModel):
    """
    UpdateThreadRequestPartial
    """ # noqa: E501
    name: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=100)]] = None
    archived: Optional[StrictBool] = None
    locked: Optional[StrictBool] = None
    invitable: Optional[StrictBool] = None
    auto_archive_duration: Optional[StrictInt] = None
    rate_limit_per_user: Optional[Annotated[int, Field(le=21600, strict=True, ge=0)]] = None
    flags: Optional[StrictInt] = None
    applied_tags: Optional[Annotated[List[Annotated[str, Field(strict=True)]], Field(max_length=5)]] = None
    bitrate: Optional[Annotated[int, Field(strict=True, ge=8000)]] = None
    user_limit: Optional[Annotated[int, Field(le=99, strict=True, ge=0)]] = None
    rtc_region: Optional[StrictStr] = None
    video_quality_mode: Optional[StrictInt] = None
    __properties: ClassVar[List[str]] = ["name", "archived", "locked", "invitable", "auto_archive_duration", "rate_limit_per_user", "flags", "applied_tags", "bitrate", "user_limit", "rtc_region", "video_quality_mode"]

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
        """Create an instance of UpdateThreadRequestPartial from a JSON string"""
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
        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        # set to None if archived (nullable) is None
        # and model_fields_set contains the field
        if self.archived is None and "archived" in self.model_fields_set:
            _dict['archived'] = None

        # set to None if locked (nullable) is None
        # and model_fields_set contains the field
        if self.locked is None and "locked" in self.model_fields_set:
            _dict['locked'] = None

        # set to None if invitable (nullable) is None
        # and model_fields_set contains the field
        if self.invitable is None and "invitable" in self.model_fields_set:
            _dict['invitable'] = None

        # set to None if rate_limit_per_user (nullable) is None
        # and model_fields_set contains the field
        if self.rate_limit_per_user is None and "rate_limit_per_user" in self.model_fields_set:
            _dict['rate_limit_per_user'] = None

        # set to None if flags (nullable) is None
        # and model_fields_set contains the field
        if self.flags is None and "flags" in self.model_fields_set:
            _dict['flags'] = None

        # set to None if applied_tags (nullable) is None
        # and model_fields_set contains the field
        if self.applied_tags is None and "applied_tags" in self.model_fields_set:
            _dict['applied_tags'] = None

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

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of UpdateThreadRequestPartial from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        # raise errors for additional fields in the input
        for _key in obj.keys():
            if _key not in cls.__properties:
                raise ValueError("Error due to additional fields (not defined in UpdateThreadRequestPartial) in the input: " + _key)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "archived": obj.get("archived"),
            "locked": obj.get("locked"),
            "invitable": obj.get("invitable"),
            "auto_archive_duration": obj.get("auto_archive_duration"),
            "rate_limit_per_user": obj.get("rate_limit_per_user"),
            "flags": obj.get("flags"),
            "applied_tags": obj.get("applied_tags"),
            "bitrate": obj.get("bitrate"),
            "user_limit": obj.get("user_limit"),
            "rtc_region": obj.get("rtc_region"),
            "video_quality_mode": obj.get("video_quality_mode")
        })
        return _obj


