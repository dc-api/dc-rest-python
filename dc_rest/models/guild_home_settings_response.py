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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from dc_rest.models.new_member_action_response import NewMemberActionResponse
from dc_rest.models.resource_channel_response import ResourceChannelResponse
from dc_rest.models.welcome_message_response import WelcomeMessageResponse
from typing import Optional, Set
from typing_extensions import Self

class GuildHomeSettingsResponse(BaseModel):
    """
    GuildHomeSettingsResponse
    """ # noqa: E501
    guild_id: Annotated[str, Field(strict=True)]
    enabled: StrictBool
    welcome_message: Optional[WelcomeMessageResponse] = None
    new_member_actions: Optional[List[Optional[NewMemberActionResponse]]] = None
    resource_channels: Optional[List[Optional[ResourceChannelResponse]]] = None
    __properties: ClassVar[List[str]] = ["guild_id", "enabled", "welcome_message", "new_member_actions", "resource_channels"]

    @field_validator('guild_id')
    def guild_id_validate_regular_expression(cls, value):
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
        """Create an instance of GuildHomeSettingsResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of welcome_message
        if self.welcome_message:
            _dict['welcome_message'] = self.welcome_message.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in new_member_actions (list)
        _items = []
        if self.new_member_actions:
            for _item_new_member_actions in self.new_member_actions:
                if _item_new_member_actions:
                    _items.append(_item_new_member_actions.to_dict())
            _dict['new_member_actions'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in resource_channels (list)
        _items = []
        if self.resource_channels:
            for _item_resource_channels in self.resource_channels:
                if _item_resource_channels:
                    _items.append(_item_resource_channels.to_dict())
            _dict['resource_channels'] = _items
        # set to None if welcome_message (nullable) is None
        # and model_fields_set contains the field
        if self.welcome_message is None and "welcome_message" in self.model_fields_set:
            _dict['welcome_message'] = None

        # set to None if new_member_actions (nullable) is None
        # and model_fields_set contains the field
        if self.new_member_actions is None and "new_member_actions" in self.model_fields_set:
            _dict['new_member_actions'] = None

        # set to None if resource_channels (nullable) is None
        # and model_fields_set contains the field
        if self.resource_channels is None and "resource_channels" in self.model_fields_set:
            _dict['resource_channels'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GuildHomeSettingsResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        # raise errors for additional fields in the input
        for _key in obj.keys():
            if _key not in cls.__properties:
                raise ValueError("Error due to additional fields (not defined in GuildHomeSettingsResponse) in the input: " + _key)

        _obj = cls.model_validate({
            "guild_id": obj.get("guild_id"),
            "enabled": obj.get("enabled"),
            "welcome_message": WelcomeMessageResponse.from_dict(obj["welcome_message"]) if obj.get("welcome_message") is not None else None,
            "new_member_actions": [NewMemberActionResponse.from_dict(_item) for _item in obj["new_member_actions"]] if obj.get("new_member_actions") is not None else None,
            "resource_channels": [ResourceChannelResponse.from_dict(_item) for _item in obj["resource_channels"]] if obj.get("resource_channels") is not None else None
        })
        return _obj


