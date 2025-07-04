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
from typing import Optional, Set
from typing_extensions import Self

class GuildPatchRequestPartial(BaseModel):
    """
    GuildPatchRequestPartial
    """ # noqa: E501
    name: Optional[Annotated[str, Field(min_length=2, strict=True, max_length=100)]] = None
    description: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=300)]] = None
    region: Optional[StrictStr] = None
    icon: Optional[StrictStr] = None
    verification_level: Optional[StrictInt] = None
    default_message_notifications: Optional[StrictInt] = None
    explicit_content_filter: Optional[StrictInt] = None
    preferred_locale: Optional[StrictStr] = None
    afk_timeout: Optional[StrictInt] = None
    afk_channel_id: Optional[Annotated[str, Field(strict=True)]] = None
    system_channel_id: Optional[Annotated[str, Field(strict=True)]] = None
    owner_id: Optional[Annotated[str, Field(strict=True)]] = None
    splash: Optional[StrictStr] = None
    banner: Optional[StrictStr] = None
    system_channel_flags: Optional[StrictInt] = None
    features: Optional[Annotated[List[Optional[Annotated[str, Field(strict=True, max_length=152133)]]], Field(max_length=1521)]] = None
    discovery_splash: Optional[StrictStr] = None
    home_header: Optional[StrictStr] = None
    rules_channel_id: Optional[Annotated[str, Field(strict=True)]] = None
    safety_alerts_channel_id: Optional[Annotated[str, Field(strict=True)]] = None
    public_updates_channel_id: Optional[Annotated[str, Field(strict=True)]] = None
    premium_progress_bar_enabled: Optional[StrictBool] = None
    __properties: ClassVar[List[str]] = ["name", "description", "region", "icon", "verification_level", "default_message_notifications", "explicit_content_filter", "preferred_locale", "afk_timeout", "afk_channel_id", "system_channel_id", "owner_id", "splash", "banner", "system_channel_flags", "features", "discovery_splash", "home_header", "rules_channel_id", "safety_alerts_channel_id", "public_updates_channel_id", "premium_progress_bar_enabled"]

    @field_validator('afk_channel_id')
    def afk_channel_id_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^(0|[1-9][0-9]*)$", value):
            raise ValueError(r"must validate the regular expression /^(0|[1-9][0-9]*)$/")
        return value

    @field_validator('system_channel_id')
    def system_channel_id_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^(0|[1-9][0-9]*)$", value):
            raise ValueError(r"must validate the regular expression /^(0|[1-9][0-9]*)$/")
        return value

    @field_validator('owner_id')
    def owner_id_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^(0|[1-9][0-9]*)$", value):
            raise ValueError(r"must validate the regular expression /^(0|[1-9][0-9]*)$/")
        return value

    @field_validator('rules_channel_id')
    def rules_channel_id_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^(0|[1-9][0-9]*)$", value):
            raise ValueError(r"must validate the regular expression /^(0|[1-9][0-9]*)$/")
        return value

    @field_validator('safety_alerts_channel_id')
    def safety_alerts_channel_id_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^(0|[1-9][0-9]*)$", value):
            raise ValueError(r"must validate the regular expression /^(0|[1-9][0-9]*)$/")
        return value

    @field_validator('public_updates_channel_id')
    def public_updates_channel_id_validate_regular_expression(cls, value):
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
        """Create an instance of GuildPatchRequestPartial from a JSON string"""
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
        # set to None if description (nullable) is None
        # and model_fields_set contains the field
        if self.description is None and "description" in self.model_fields_set:
            _dict['description'] = None

        # set to None if region (nullable) is None
        # and model_fields_set contains the field
        if self.region is None and "region" in self.model_fields_set:
            _dict['region'] = None

        # set to None if icon (nullable) is None
        # and model_fields_set contains the field
        if self.icon is None and "icon" in self.model_fields_set:
            _dict['icon'] = None

        # set to None if afk_timeout (nullable) is None
        # and model_fields_set contains the field
        if self.afk_timeout is None and "afk_timeout" in self.model_fields_set:
            _dict['afk_timeout'] = None

        # set to None if splash (nullable) is None
        # and model_fields_set contains the field
        if self.splash is None and "splash" in self.model_fields_set:
            _dict['splash'] = None

        # set to None if banner (nullable) is None
        # and model_fields_set contains the field
        if self.banner is None and "banner" in self.model_fields_set:
            _dict['banner'] = None

        # set to None if system_channel_flags (nullable) is None
        # and model_fields_set contains the field
        if self.system_channel_flags is None and "system_channel_flags" in self.model_fields_set:
            _dict['system_channel_flags'] = None

        # set to None if features (nullable) is None
        # and model_fields_set contains the field
        if self.features is None and "features" in self.model_fields_set:
            _dict['features'] = None

        # set to None if discovery_splash (nullable) is None
        # and model_fields_set contains the field
        if self.discovery_splash is None and "discovery_splash" in self.model_fields_set:
            _dict['discovery_splash'] = None

        # set to None if home_header (nullable) is None
        # and model_fields_set contains the field
        if self.home_header is None and "home_header" in self.model_fields_set:
            _dict['home_header'] = None

        # set to None if premium_progress_bar_enabled (nullable) is None
        # and model_fields_set contains the field
        if self.premium_progress_bar_enabled is None and "premium_progress_bar_enabled" in self.model_fields_set:
            _dict['premium_progress_bar_enabled'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GuildPatchRequestPartial from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        # raise errors for additional fields in the input
        for _key in obj.keys():
            if _key not in cls.__properties:
                raise ValueError("Error due to additional fields (not defined in GuildPatchRequestPartial) in the input: " + _key)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "description": obj.get("description"),
            "region": obj.get("region"),
            "icon": obj.get("icon"),
            "verification_level": obj.get("verification_level"),
            "default_message_notifications": obj.get("default_message_notifications"),
            "explicit_content_filter": obj.get("explicit_content_filter"),
            "preferred_locale": obj.get("preferred_locale"),
            "afk_timeout": obj.get("afk_timeout"),
            "afk_channel_id": obj.get("afk_channel_id"),
            "system_channel_id": obj.get("system_channel_id"),
            "owner_id": obj.get("owner_id"),
            "splash": obj.get("splash"),
            "banner": obj.get("banner"),
            "system_channel_flags": obj.get("system_channel_flags"),
            "features": obj.get("features"),
            "discovery_splash": obj.get("discovery_splash"),
            "home_header": obj.get("home_header"),
            "rules_channel_id": obj.get("rules_channel_id"),
            "safety_alerts_channel_id": obj.get("safety_alerts_channel_id"),
            "public_updates_channel_id": obj.get("public_updates_channel_id"),
            "premium_progress_bar_enabled": obj.get("premium_progress_bar_enabled")
        })
        return _obj


