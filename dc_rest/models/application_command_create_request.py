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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from dc_rest.models.application_command_create_request_options_inner import ApplicationCommandCreateRequestOptionsInner
from typing import Optional, Set
from typing_extensions import Self

class ApplicationCommandCreateRequest(BaseModel):
    """
    ApplicationCommandCreateRequest
    """ # noqa: E501
    name: Annotated[str, Field(min_length=1, strict=True, max_length=32)]
    name_localizations: Optional[Dict[str, Annotated[str, Field(min_length=1, strict=True, max_length=32)]]] = None
    description: Optional[Annotated[str, Field(strict=True, max_length=100)]] = None
    description_localizations: Optional[Dict[str, Annotated[str, Field(min_length=1, strict=True, max_length=100)]]] = None
    options: Optional[Annotated[List[ApplicationCommandCreateRequestOptionsInner], Field(max_length=25)]] = None
    default_member_permissions: Optional[Annotated[int, Field(le=4503599627370495, strict=True, ge=0)]] = None
    dm_permission: Optional[StrictBool] = None
    contexts: Optional[Annotated[List[StrictInt], Field(min_length=1)]] = None
    integration_types: Optional[Annotated[List[StrictInt], Field(min_length=1)]] = None
    handler: Optional[StrictInt] = None
    type: Optional[StrictInt] = None
    __properties: ClassVar[List[str]] = ["name", "name_localizations", "description", "description_localizations", "options", "default_member_permissions", "dm_permission", "contexts", "integration_types", "handler", "type"]

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
        """Create an instance of ApplicationCommandCreateRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in options (list)
        _items = []
        if self.options:
            for _item_options in self.options:
                if _item_options:
                    _items.append(_item_options.to_dict())
            _dict['options'] = _items
        # set to None if description (nullable) is None
        # and model_fields_set contains the field
        if self.description is None and "description" in self.model_fields_set:
            _dict['description'] = None

        # set to None if options (nullable) is None
        # and model_fields_set contains the field
        if self.options is None and "options" in self.model_fields_set:
            _dict['options'] = None

        # set to None if default_member_permissions (nullable) is None
        # and model_fields_set contains the field
        if self.default_member_permissions is None and "default_member_permissions" in self.model_fields_set:
            _dict['default_member_permissions'] = None

        # set to None if dm_permission (nullable) is None
        # and model_fields_set contains the field
        if self.dm_permission is None and "dm_permission" in self.model_fields_set:
            _dict['dm_permission'] = None

        # set to None if contexts (nullable) is None
        # and model_fields_set contains the field
        if self.contexts is None and "contexts" in self.model_fields_set:
            _dict['contexts'] = None

        # set to None if integration_types (nullable) is None
        # and model_fields_set contains the field
        if self.integration_types is None and "integration_types" in self.model_fields_set:
            _dict['integration_types'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ApplicationCommandCreateRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        # raise errors for additional fields in the input
        for _key in obj.keys():
            if _key not in cls.__properties:
                raise ValueError("Error due to additional fields (not defined in ApplicationCommandCreateRequest) in the input: " + _key)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "name_localizations": obj.get("name_localizations"),
            "description": obj.get("description"),
            "description_localizations": obj.get("description_localizations"),
            "options": [ApplicationCommandCreateRequestOptionsInner.from_dict(_item) for _item in obj["options"]] if obj.get("options") is not None else None,
            "default_member_permissions": obj.get("default_member_permissions"),
            "dm_permission": obj.get("dm_permission"),
            "contexts": obj.get("contexts"),
            "integration_types": obj.get("integration_types"),
            "handler": obj.get("handler"),
            "type": obj.get("type")
        })
        return _obj


