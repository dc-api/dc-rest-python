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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from dc_rest.models.mentionable_select_component_for_message_request_default_values_inner import MentionableSelectComponentForMessageRequestDefaultValuesInner
from typing import Optional, Set
from typing_extensions import Self

class MentionableSelectComponentForMessageRequest(BaseModel):
    """
    MentionableSelectComponentForMessageRequest
    """ # noqa: E501
    type: StrictInt
    custom_id: Annotated[str, Field(strict=True, max_length=100)]
    placeholder: Optional[Annotated[str, Field(strict=True, max_length=150)]] = None
    min_values: Optional[Annotated[int, Field(le=25, strict=True, ge=0)]] = None
    max_values: Optional[Annotated[int, Field(le=25, strict=True, ge=1)]] = None
    disabled: Optional[StrictBool] = None
    default_values: Optional[Annotated[List[MentionableSelectComponentForMessageRequestDefaultValuesInner], Field(max_length=25)]] = None
    __properties: ClassVar[List[str]] = ["type", "custom_id", "placeholder", "min_values", "max_values", "disabled", "default_values"]

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
        """Create an instance of MentionableSelectComponentForMessageRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in default_values (list)
        _items = []
        if self.default_values:
            for _item_default_values in self.default_values:
                if _item_default_values:
                    _items.append(_item_default_values.to_dict())
            _dict['default_values'] = _items
        # set to None if placeholder (nullable) is None
        # and model_fields_set contains the field
        if self.placeholder is None and "placeholder" in self.model_fields_set:
            _dict['placeholder'] = None

        # set to None if min_values (nullable) is None
        # and model_fields_set contains the field
        if self.min_values is None and "min_values" in self.model_fields_set:
            _dict['min_values'] = None

        # set to None if max_values (nullable) is None
        # and model_fields_set contains the field
        if self.max_values is None and "max_values" in self.model_fields_set:
            _dict['max_values'] = None

        # set to None if disabled (nullable) is None
        # and model_fields_set contains the field
        if self.disabled is None and "disabled" in self.model_fields_set:
            _dict['disabled'] = None

        # set to None if default_values (nullable) is None
        # and model_fields_set contains the field
        if self.default_values is None and "default_values" in self.model_fields_set:
            _dict['default_values'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of MentionableSelectComponentForMessageRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        # raise errors for additional fields in the input
        for _key in obj.keys():
            if _key not in cls.__properties:
                raise ValueError("Error due to additional fields (not defined in MentionableSelectComponentForMessageRequest) in the input: " + _key)

        _obj = cls.model_validate({
            "type": obj.get("type"),
            "custom_id": obj.get("custom_id"),
            "placeholder": obj.get("placeholder"),
            "min_values": obj.get("min_values"),
            "max_values": obj.get("max_values"),
            "disabled": obj.get("disabled"),
            "default_values": [MentionableSelectComponentForMessageRequestDefaultValuesInner.from_dict(_item) for _item in obj["default_values"]] if obj.get("default_values") is not None else None
        })
        return _obj


