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
from dc_rest.models.application_command_attachment_option_response import ApplicationCommandAttachmentOptionResponse
from dc_rest.models.application_command_boolean_option_response import ApplicationCommandBooleanOptionResponse
from dc_rest.models.application_command_channel_option_response import ApplicationCommandChannelOptionResponse
from dc_rest.models.application_command_integer_option_response import ApplicationCommandIntegerOptionResponse
from dc_rest.models.application_command_mentionable_option_response import ApplicationCommandMentionableOptionResponse
from dc_rest.models.application_command_number_option_response import ApplicationCommandNumberOptionResponse
from dc_rest.models.application_command_role_option_response import ApplicationCommandRoleOptionResponse
from dc_rest.models.application_command_string_option_response import ApplicationCommandStringOptionResponse
from dc_rest.models.application_command_subcommand_group_option_response import ApplicationCommandSubcommandGroupOptionResponse
from dc_rest.models.application_command_subcommand_option_response import ApplicationCommandSubcommandOptionResponse
from dc_rest.models.application_command_user_option_response import ApplicationCommandUserOptionResponse
from pydantic import StrictStr, Field
from typing import Union, List, Set, Optional, Dict
from typing_extensions import Literal, Self

APPLICATIONCOMMANDRESPONSEOPTIONSINNER_ONE_OF_SCHEMAS = ["ApplicationCommandAttachmentOptionResponse", "ApplicationCommandBooleanOptionResponse", "ApplicationCommandChannelOptionResponse", "ApplicationCommandIntegerOptionResponse", "ApplicationCommandMentionableOptionResponse", "ApplicationCommandNumberOptionResponse", "ApplicationCommandRoleOptionResponse", "ApplicationCommandStringOptionResponse", "ApplicationCommandSubcommandGroupOptionResponse", "ApplicationCommandSubcommandOptionResponse", "ApplicationCommandUserOptionResponse"]

class ApplicationCommandResponseOptionsInner(BaseModel):
    """
    ApplicationCommandResponseOptionsInner
    """
    # data type: ApplicationCommandAttachmentOptionResponse
    oneof_schema_1_validator: Optional[ApplicationCommandAttachmentOptionResponse] = None
    # data type: ApplicationCommandBooleanOptionResponse
    oneof_schema_2_validator: Optional[ApplicationCommandBooleanOptionResponse] = None
    # data type: ApplicationCommandChannelOptionResponse
    oneof_schema_3_validator: Optional[ApplicationCommandChannelOptionResponse] = None
    # data type: ApplicationCommandIntegerOptionResponse
    oneof_schema_4_validator: Optional[ApplicationCommandIntegerOptionResponse] = None
    # data type: ApplicationCommandMentionableOptionResponse
    oneof_schema_5_validator: Optional[ApplicationCommandMentionableOptionResponse] = None
    # data type: ApplicationCommandNumberOptionResponse
    oneof_schema_6_validator: Optional[ApplicationCommandNumberOptionResponse] = None
    # data type: ApplicationCommandRoleOptionResponse
    oneof_schema_7_validator: Optional[ApplicationCommandRoleOptionResponse] = None
    # data type: ApplicationCommandStringOptionResponse
    oneof_schema_8_validator: Optional[ApplicationCommandStringOptionResponse] = None
    # data type: ApplicationCommandSubcommandGroupOptionResponse
    oneof_schema_9_validator: Optional[ApplicationCommandSubcommandGroupOptionResponse] = None
    # data type: ApplicationCommandSubcommandOptionResponse
    oneof_schema_10_validator: Optional[ApplicationCommandSubcommandOptionResponse] = None
    # data type: ApplicationCommandUserOptionResponse
    oneof_schema_11_validator: Optional[ApplicationCommandUserOptionResponse] = None
    actual_instance: Optional[Union[ApplicationCommandAttachmentOptionResponse, ApplicationCommandBooleanOptionResponse, ApplicationCommandChannelOptionResponse, ApplicationCommandIntegerOptionResponse, ApplicationCommandMentionableOptionResponse, ApplicationCommandNumberOptionResponse, ApplicationCommandRoleOptionResponse, ApplicationCommandStringOptionResponse, ApplicationCommandSubcommandGroupOptionResponse, ApplicationCommandSubcommandOptionResponse, ApplicationCommandUserOptionResponse]] = None
    one_of_schemas: Set[str] = { "ApplicationCommandAttachmentOptionResponse", "ApplicationCommandBooleanOptionResponse", "ApplicationCommandChannelOptionResponse", "ApplicationCommandIntegerOptionResponse", "ApplicationCommandMentionableOptionResponse", "ApplicationCommandNumberOptionResponse", "ApplicationCommandRoleOptionResponse", "ApplicationCommandStringOptionResponse", "ApplicationCommandSubcommandGroupOptionResponse", "ApplicationCommandSubcommandOptionResponse", "ApplicationCommandUserOptionResponse" }

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
        instance = ApplicationCommandResponseOptionsInner.model_construct()
        error_messages = []
        match = 0
        # validate data type: ApplicationCommandAttachmentOptionResponse
        if not isinstance(v, ApplicationCommandAttachmentOptionResponse):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ApplicationCommandAttachmentOptionResponse`")
        else:
            match += 1
        # validate data type: ApplicationCommandBooleanOptionResponse
        if not isinstance(v, ApplicationCommandBooleanOptionResponse):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ApplicationCommandBooleanOptionResponse`")
        else:
            match += 1
        # validate data type: ApplicationCommandChannelOptionResponse
        if not isinstance(v, ApplicationCommandChannelOptionResponse):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ApplicationCommandChannelOptionResponse`")
        else:
            match += 1
        # validate data type: ApplicationCommandIntegerOptionResponse
        if not isinstance(v, ApplicationCommandIntegerOptionResponse):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ApplicationCommandIntegerOptionResponse`")
        else:
            match += 1
        # validate data type: ApplicationCommandMentionableOptionResponse
        if not isinstance(v, ApplicationCommandMentionableOptionResponse):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ApplicationCommandMentionableOptionResponse`")
        else:
            match += 1
        # validate data type: ApplicationCommandNumberOptionResponse
        if not isinstance(v, ApplicationCommandNumberOptionResponse):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ApplicationCommandNumberOptionResponse`")
        else:
            match += 1
        # validate data type: ApplicationCommandRoleOptionResponse
        if not isinstance(v, ApplicationCommandRoleOptionResponse):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ApplicationCommandRoleOptionResponse`")
        else:
            match += 1
        # validate data type: ApplicationCommandStringOptionResponse
        if not isinstance(v, ApplicationCommandStringOptionResponse):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ApplicationCommandStringOptionResponse`")
        else:
            match += 1
        # validate data type: ApplicationCommandSubcommandGroupOptionResponse
        if not isinstance(v, ApplicationCommandSubcommandGroupOptionResponse):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ApplicationCommandSubcommandGroupOptionResponse`")
        else:
            match += 1
        # validate data type: ApplicationCommandSubcommandOptionResponse
        if not isinstance(v, ApplicationCommandSubcommandOptionResponse):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ApplicationCommandSubcommandOptionResponse`")
        else:
            match += 1
        # validate data type: ApplicationCommandUserOptionResponse
        if not isinstance(v, ApplicationCommandUserOptionResponse):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ApplicationCommandUserOptionResponse`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in ApplicationCommandResponseOptionsInner with oneOf schemas: ApplicationCommandAttachmentOptionResponse, ApplicationCommandBooleanOptionResponse, ApplicationCommandChannelOptionResponse, ApplicationCommandIntegerOptionResponse, ApplicationCommandMentionableOptionResponse, ApplicationCommandNumberOptionResponse, ApplicationCommandRoleOptionResponse, ApplicationCommandStringOptionResponse, ApplicationCommandSubcommandGroupOptionResponse, ApplicationCommandSubcommandOptionResponse, ApplicationCommandUserOptionResponse. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in ApplicationCommandResponseOptionsInner with oneOf schemas: ApplicationCommandAttachmentOptionResponse, ApplicationCommandBooleanOptionResponse, ApplicationCommandChannelOptionResponse, ApplicationCommandIntegerOptionResponse, ApplicationCommandMentionableOptionResponse, ApplicationCommandNumberOptionResponse, ApplicationCommandRoleOptionResponse, ApplicationCommandStringOptionResponse, ApplicationCommandSubcommandGroupOptionResponse, ApplicationCommandSubcommandOptionResponse, ApplicationCommandUserOptionResponse. Details: " + ", ".join(error_messages))
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

        # deserialize data into ApplicationCommandAttachmentOptionResponse
        try:
            instance.actual_instance = ApplicationCommandAttachmentOptionResponse.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into ApplicationCommandBooleanOptionResponse
        try:
            instance.actual_instance = ApplicationCommandBooleanOptionResponse.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into ApplicationCommandChannelOptionResponse
        try:
            instance.actual_instance = ApplicationCommandChannelOptionResponse.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into ApplicationCommandIntegerOptionResponse
        try:
            instance.actual_instance = ApplicationCommandIntegerOptionResponse.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into ApplicationCommandMentionableOptionResponse
        try:
            instance.actual_instance = ApplicationCommandMentionableOptionResponse.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into ApplicationCommandNumberOptionResponse
        try:
            instance.actual_instance = ApplicationCommandNumberOptionResponse.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into ApplicationCommandRoleOptionResponse
        try:
            instance.actual_instance = ApplicationCommandRoleOptionResponse.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into ApplicationCommandStringOptionResponse
        try:
            instance.actual_instance = ApplicationCommandStringOptionResponse.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into ApplicationCommandSubcommandGroupOptionResponse
        try:
            instance.actual_instance = ApplicationCommandSubcommandGroupOptionResponse.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into ApplicationCommandSubcommandOptionResponse
        try:
            instance.actual_instance = ApplicationCommandSubcommandOptionResponse.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into ApplicationCommandUserOptionResponse
        try:
            instance.actual_instance = ApplicationCommandUserOptionResponse.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into ApplicationCommandResponseOptionsInner with oneOf schemas: ApplicationCommandAttachmentOptionResponse, ApplicationCommandBooleanOptionResponse, ApplicationCommandChannelOptionResponse, ApplicationCommandIntegerOptionResponse, ApplicationCommandMentionableOptionResponse, ApplicationCommandNumberOptionResponse, ApplicationCommandRoleOptionResponse, ApplicationCommandStringOptionResponse, ApplicationCommandSubcommandGroupOptionResponse, ApplicationCommandSubcommandOptionResponse, ApplicationCommandUserOptionResponse. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into ApplicationCommandResponseOptionsInner with oneOf schemas: ApplicationCommandAttachmentOptionResponse, ApplicationCommandBooleanOptionResponse, ApplicationCommandChannelOptionResponse, ApplicationCommandIntegerOptionResponse, ApplicationCommandMentionableOptionResponse, ApplicationCommandNumberOptionResponse, ApplicationCommandRoleOptionResponse, ApplicationCommandStringOptionResponse, ApplicationCommandSubcommandGroupOptionResponse, ApplicationCommandSubcommandOptionResponse, ApplicationCommandUserOptionResponse. Details: " + ", ".join(error_messages))
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

    def to_dict(self) -> Optional[Union[Dict[str, Any], ApplicationCommandAttachmentOptionResponse, ApplicationCommandBooleanOptionResponse, ApplicationCommandChannelOptionResponse, ApplicationCommandIntegerOptionResponse, ApplicationCommandMentionableOptionResponse, ApplicationCommandNumberOptionResponse, ApplicationCommandRoleOptionResponse, ApplicationCommandStringOptionResponse, ApplicationCommandSubcommandGroupOptionResponse, ApplicationCommandSubcommandOptionResponse, ApplicationCommandUserOptionResponse]]:
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


