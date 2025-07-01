# coding: utf-8

"""
Discord HTTP API (Preview) - REST API Client
Preview of the Discord v10 HTTP API specification. See https://discord.com/developers/docs for more details.

## Metadata

- **Copyright**: Copyright (c) 2025 Qntx
- **Author**: ΣX <gitctrlx@gmail.com>
- **Version**: 10
- **Modified**: 2025-07-01T10:27:27.208780920Z[Etc/UTC]
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
from dc_rest.models.application_command_option_string_choice import ApplicationCommandOptionStringChoice
from typing import Optional, Set
from typing_extensions import Self

class ApplicationCommandStringOption(BaseModel):
    """
    ApplicationCommandStringOption
    """ # noqa: E501
    type: StrictInt
    name: Annotated[str, Field(min_length=1, strict=True, max_length=32)]
    name_localizations: Optional[Dict[str, Annotated[str, Field(min_length=1, strict=True, max_length=32)]]] = None
    description: Annotated[str, Field(min_length=1, strict=True, max_length=100)]
    description_localizations: Optional[Dict[str, Annotated[str, Field(min_length=1, strict=True, max_length=100)]]] = None
    required: Optional[StrictBool] = None
    autocomplete: Optional[StrictBool] = None
    min_length: Optional[Annotated[int, Field(le=6000, strict=True, ge=0)]] = None
    max_length: Optional[Annotated[int, Field(le=6000, strict=True, ge=1)]] = None
    choices: Optional[Annotated[List[ApplicationCommandOptionStringChoice], Field(max_length=25)]] = None
    __properties: ClassVar[List[str]] = ["type", "name", "name_localizations", "description", "description_localizations", "required", "autocomplete", "min_length", "max_length", "choices"]

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
        """Create an instance of ApplicationCommandStringOption from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in choices (list)
        _items = []
        if self.choices:
            for _item_choices in self.choices:
                if _item_choices:
                    _items.append(_item_choices.to_dict())
            _dict['choices'] = _items
        # set to None if required (nullable) is None
        # and model_fields_set contains the field
        if self.required is None and "required" in self.model_fields_set:
            _dict['required'] = None

        # set to None if autocomplete (nullable) is None
        # and model_fields_set contains the field
        if self.autocomplete is None and "autocomplete" in self.model_fields_set:
            _dict['autocomplete'] = None

        # set to None if min_length (nullable) is None
        # and model_fields_set contains the field
        if self.min_length is None and "min_length" in self.model_fields_set:
            _dict['min_length'] = None

        # set to None if max_length (nullable) is None
        # and model_fields_set contains the field
        if self.max_length is None and "max_length" in self.model_fields_set:
            _dict['max_length'] = None

        # set to None if choices (nullable) is None
        # and model_fields_set contains the field
        if self.choices is None and "choices" in self.model_fields_set:
            _dict['choices'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ApplicationCommandStringOption from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        # raise errors for additional fields in the input
        for _key in obj.keys():
            if _key not in cls.__properties:
                raise ValueError("Error due to additional fields (not defined in ApplicationCommandStringOption) in the input: " + _key)

        _obj = cls.model_validate({
            "type": obj.get("type"),
            "name": obj.get("name"),
            "name_localizations": obj.get("name_localizations"),
            "description": obj.get("description"),
            "description_localizations": obj.get("description_localizations"),
            "required": obj.get("required"),
            "autocomplete": obj.get("autocomplete"),
            "min_length": obj.get("min_length"),
            "max_length": obj.get("max_length"),
            "choices": [ApplicationCommandOptionStringChoice.from_dict(_item) for _item in obj["choices"]] if obj.get("choices") is not None else None
        })
        return _obj


