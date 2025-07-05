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
import json
import pprint
from pydantic import BaseModel, ConfigDict, Field, StrictStr, ValidationError, field_validator
from typing import Any, List, Optional
from dc_rest.models.button_component_response import ButtonComponentResponse
from dc_rest.models.channel_select_component_response import ChannelSelectComponentResponse
from dc_rest.models.mentionable_select_component_response import MentionableSelectComponentResponse
from dc_rest.models.role_select_component_response import RoleSelectComponentResponse
from dc_rest.models.string_select_component_response import StringSelectComponentResponse
from dc_rest.models.text_input_component_response import TextInputComponentResponse
from dc_rest.models.user_select_component_response import UserSelectComponentResponse
from pydantic import StrictStr, Field
from typing import Union, List, Set, Optional, Dict
from typing_extensions import Literal, Self

ACTIONROWCOMPONENTRESPONSECOMPONENTSINNER_ONE_OF_SCHEMAS = ["ButtonComponentResponse", "ChannelSelectComponentResponse", "MentionableSelectComponentResponse", "RoleSelectComponentResponse", "StringSelectComponentResponse", "TextInputComponentResponse", "UserSelectComponentResponse"]

class ActionRowComponentResponseComponentsInner(BaseModel):
    """
    ActionRowComponentResponseComponentsInner
    """
    # data type: ButtonComponentResponse
    oneof_schema_1_validator: Optional[ButtonComponentResponse] = None
    # data type: ChannelSelectComponentResponse
    oneof_schema_2_validator: Optional[ChannelSelectComponentResponse] = None
    # data type: MentionableSelectComponentResponse
    oneof_schema_3_validator: Optional[MentionableSelectComponentResponse] = None
    # data type: RoleSelectComponentResponse
    oneof_schema_4_validator: Optional[RoleSelectComponentResponse] = None
    # data type: StringSelectComponentResponse
    oneof_schema_5_validator: Optional[StringSelectComponentResponse] = None
    # data type: TextInputComponentResponse
    oneof_schema_6_validator: Optional[TextInputComponentResponse] = None
    # data type: UserSelectComponentResponse
    oneof_schema_7_validator: Optional[UserSelectComponentResponse] = None
    actual_instance: Optional[Union[ButtonComponentResponse, ChannelSelectComponentResponse, MentionableSelectComponentResponse, RoleSelectComponentResponse, StringSelectComponentResponse, TextInputComponentResponse, UserSelectComponentResponse]] = None
    one_of_schemas: Set[str] = { "ButtonComponentResponse", "ChannelSelectComponentResponse", "MentionableSelectComponentResponse", "RoleSelectComponentResponse", "StringSelectComponentResponse", "TextInputComponentResponse", "UserSelectComponentResponse" }

    model_config = ConfigDict(
        validate_assignment=True,
        protected_namespaces=(),
    )


    def __init__(self, *args, **kwargs) -> None:
        if args:
            if len(args) > 1:
                raise ValueError("If a position argument is used, only 1 is allowed to set `actual_instance`")
            if kwargs:
                raise ValueError("If a position argument is used, keyword arguments cannot be used.")
            super().__init__(actual_instance=args[0])
        else:
            super().__init__(**kwargs)

    @field_validator('actual_instance')
    def actual_instance_must_validate_oneof(cls, v):
        instance = ActionRowComponentResponseComponentsInner.model_construct()
        error_messages = []
        match = 0
        # validate data type: ButtonComponentResponse
        if not isinstance(v, ButtonComponentResponse):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ButtonComponentResponse`")
        else:
            match += 1
        # validate data type: ChannelSelectComponentResponse
        if not isinstance(v, ChannelSelectComponentResponse):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ChannelSelectComponentResponse`")
        else:
            match += 1
        # validate data type: MentionableSelectComponentResponse
        if not isinstance(v, MentionableSelectComponentResponse):
            error_messages.append(f"Error! Input type `{type(v)}` is not `MentionableSelectComponentResponse`")
        else:
            match += 1
        # validate data type: RoleSelectComponentResponse
        if not isinstance(v, RoleSelectComponentResponse):
            error_messages.append(f"Error! Input type `{type(v)}` is not `RoleSelectComponentResponse`")
        else:
            match += 1
        # validate data type: StringSelectComponentResponse
        if not isinstance(v, StringSelectComponentResponse):
            error_messages.append(f"Error! Input type `{type(v)}` is not `StringSelectComponentResponse`")
        else:
            match += 1
        # validate data type: TextInputComponentResponse
        if not isinstance(v, TextInputComponentResponse):
            error_messages.append(f"Error! Input type `{type(v)}` is not `TextInputComponentResponse`")
        else:
            match += 1
        # validate data type: UserSelectComponentResponse
        if not isinstance(v, UserSelectComponentResponse):
            error_messages.append(f"Error! Input type `{type(v)}` is not `UserSelectComponentResponse`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in ActionRowComponentResponseComponentsInner with oneOf schemas: ButtonComponentResponse, ChannelSelectComponentResponse, MentionableSelectComponentResponse, RoleSelectComponentResponse, StringSelectComponentResponse, TextInputComponentResponse, UserSelectComponentResponse. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in ActionRowComponentResponseComponentsInner with oneOf schemas: ButtonComponentResponse, ChannelSelectComponentResponse, MentionableSelectComponentResponse, RoleSelectComponentResponse, StringSelectComponentResponse, TextInputComponentResponse, UserSelectComponentResponse. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: Union[str, Dict[str, Any]]) -> Self:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Returns the object represented by the json string"""
        instance = cls.model_construct()
        error_messages = []
        match = 0

        # deserialize data into ButtonComponentResponse
        try:
            instance.actual_instance = ButtonComponentResponse.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into ChannelSelectComponentResponse
        try:
            instance.actual_instance = ChannelSelectComponentResponse.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into MentionableSelectComponentResponse
        try:
            instance.actual_instance = MentionableSelectComponentResponse.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into RoleSelectComponentResponse
        try:
            instance.actual_instance = RoleSelectComponentResponse.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into StringSelectComponentResponse
        try:
            instance.actual_instance = StringSelectComponentResponse.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into TextInputComponentResponse
        try:
            instance.actual_instance = TextInputComponentResponse.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into UserSelectComponentResponse
        try:
            instance.actual_instance = UserSelectComponentResponse.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into ActionRowComponentResponseComponentsInner with oneOf schemas: ButtonComponentResponse, ChannelSelectComponentResponse, MentionableSelectComponentResponse, RoleSelectComponentResponse, StringSelectComponentResponse, TextInputComponentResponse, UserSelectComponentResponse. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into ActionRowComponentResponseComponentsInner with oneOf schemas: ButtonComponentResponse, ChannelSelectComponentResponse, MentionableSelectComponentResponse, RoleSelectComponentResponse, StringSelectComponentResponse, TextInputComponentResponse, UserSelectComponentResponse. Details: " + ", ".join(error_messages))
        else:
            return instance

    def to_json(self) -> str:
        """Returns the JSON representation of the actual instance"""
        if self.actual_instance is None:
            return "null"

        if hasattr(self.actual_instance, "to_json") and callable(self.actual_instance.to_json):
            return self.actual_instance.to_json()
        else:
            return json.dumps(self.actual_instance)

    def to_dict(self) -> Optional[Union[Dict[str, Any], ButtonComponentResponse, ChannelSelectComponentResponse, MentionableSelectComponentResponse, RoleSelectComponentResponse, StringSelectComponentResponse, TextInputComponentResponse, UserSelectComponentResponse]]:
        """Returns the dict representation of the actual instance"""
        if self.actual_instance is None:
            return None

        if hasattr(self.actual_instance, "to_dict") and callable(self.actual_instance.to_dict):
            return self.actual_instance.to_dict()
        else:
            # primitive type
            return self.actual_instance

    def to_str(self) -> str:
        """Returns the string representation of the actual instance"""
        return pprint.pformat(self.model_dump())


