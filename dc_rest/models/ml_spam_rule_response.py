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
from dc_rest.models.default_keyword_rule_response_actions_inner import DefaultKeywordRuleResponseActionsInner
from typing import Optional, Set
from typing_extensions import Self

class MLSpamRuleResponse(BaseModel):
    """
    MLSpamRuleResponse
    """ # noqa: E501
    id: Annotated[str, Field(strict=True)]
    guild_id: Annotated[str, Field(strict=True)]
    creator_id: Annotated[str, Field(strict=True)]
    name: StrictStr
    event_type: StrictInt
    actions: List[DefaultKeywordRuleResponseActionsInner]
    trigger_type: StrictInt
    enabled: Optional[StrictBool] = None
    exempt_roles: Optional[List[Annotated[str, Field(strict=True)]]] = None
    exempt_channels: Optional[List[Annotated[str, Field(strict=True)]]] = None
    trigger_metadata: Dict[str, Any]
    __properties: ClassVar[List[str]] = ["id", "guild_id", "creator_id", "name", "event_type", "actions", "trigger_type", "enabled", "exempt_roles", "exempt_channels", "trigger_metadata"]

    @field_validator('id')
    def id_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^(0|[1-9][0-9]*)$", value):
            raise ValueError(r"must validate the regular expression /^(0|[1-9][0-9]*)$/")
        return value

    @field_validator('guild_id')
    def guild_id_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^(0|[1-9][0-9]*)$", value):
            raise ValueError(r"must validate the regular expression /^(0|[1-9][0-9]*)$/")
        return value

    @field_validator('creator_id')
    def creator_id_validate_regular_expression(cls, value):
        """Validates the regular expression"""
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
        """Create an instance of MLSpamRuleResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in actions (list)
        _items = []
        if self.actions:
            for _item_actions in self.actions:
                if _item_actions:
                    _items.append(_item_actions.to_dict())
            _dict['actions'] = _items
        # set to None if enabled (nullable) is None
        # and model_fields_set contains the field
        if self.enabled is None and "enabled" in self.model_fields_set:
            _dict['enabled'] = None

        # set to None if exempt_roles (nullable) is None
        # and model_fields_set contains the field
        if self.exempt_roles is None and "exempt_roles" in self.model_fields_set:
            _dict['exempt_roles'] = None

        # set to None if exempt_channels (nullable) is None
        # and model_fields_set contains the field
        if self.exempt_channels is None and "exempt_channels" in self.model_fields_set:
            _dict['exempt_channels'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of MLSpamRuleResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        # raise errors for additional fields in the input
        for _key in obj.keys():
            if _key not in cls.__properties:
                raise ValueError("Error due to additional fields (not defined in MLSpamRuleResponse) in the input: " + _key)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "guild_id": obj.get("guild_id"),
            "creator_id": obj.get("creator_id"),
            "name": obj.get("name"),
            "event_type": obj.get("event_type"),
            "actions": [DefaultKeywordRuleResponseActionsInner.from_dict(_item) for _item in obj["actions"]] if obj.get("actions") is not None else None,
            "trigger_type": obj.get("trigger_type"),
            "enabled": obj.get("enabled"),
            "exempt_roles": obj.get("exempt_roles"),
            "exempt_channels": obj.get("exempt_channels"),
            "trigger_metadata": obj.get("trigger_metadata")
        })
        return _obj


