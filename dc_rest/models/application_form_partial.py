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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from dc_rest.models.application_form_partial_description import ApplicationFormPartialDescription
from dc_rest.models.application_form_partial_integration_types_config_value import ApplicationFormPartialIntegrationTypesConfigValue
from dc_rest.models.application_o_auth2_install_params import ApplicationOAuth2InstallParams
from typing import Optional, Set
from typing_extensions import Self

class ApplicationFormPartial(BaseModel):
    """
    ApplicationFormPartial
    """ # noqa: E501
    description: Optional[ApplicationFormPartialDescription] = None
    icon: Optional[StrictStr] = None
    cover_image: Optional[StrictStr] = None
    team_id: Optional[Annotated[str, Field(strict=True)]] = None
    flags: Optional[StrictInt] = None
    interactions_endpoint_url: Optional[Annotated[str, Field(strict=True, max_length=2048)]] = None
    explicit_content_filter: Optional[StrictInt] = None
    max_participants: Optional[Annotated[int, Field(strict=True, ge=-1)]] = None
    type: Optional[StrictInt] = None
    tags: Optional[Annotated[List[Annotated[str, Field(strict=True, max_length=20)]], Field(max_length=5)]] = None
    custom_install_url: Optional[Annotated[str, Field(strict=True, max_length=2048)]] = None
    install_params: Optional[ApplicationOAuth2InstallParams] = None
    role_connections_verification_url: Optional[Annotated[str, Field(strict=True, max_length=2048)]] = None
    integration_types_config: Optional[Dict[str, Optional[ApplicationFormPartialIntegrationTypesConfigValue]]] = None
    __properties: ClassVar[List[str]] = ["description", "icon", "cover_image", "team_id", "flags", "interactions_endpoint_url", "explicit_content_filter", "max_participants", "type", "tags", "custom_install_url", "install_params", "role_connections_verification_url", "integration_types_config"]

    @field_validator('team_id')
    def team_id_validate_regular_expression(cls, value):
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
        """Create an instance of ApplicationFormPartial from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of description
        if self.description:
            _dict['description'] = self.description.to_dict()
        # override the default output from pydantic by calling `to_dict()` of install_params
        if self.install_params:
            _dict['install_params'] = self.install_params.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each value in integration_types_config (dict)
        _field_dict = {}
        if self.integration_types_config:
            for _key_integration_types_config in self.integration_types_config:
                if self.integration_types_config[_key_integration_types_config]:
                    _field_dict[_key_integration_types_config] = self.integration_types_config[_key_integration_types_config].to_dict()
            _dict['integration_types_config'] = _field_dict
        # set to None if icon (nullable) is None
        # and model_fields_set contains the field
        if self.icon is None and "icon" in self.model_fields_set:
            _dict['icon'] = None

        # set to None if cover_image (nullable) is None
        # and model_fields_set contains the field
        if self.cover_image is None and "cover_image" in self.model_fields_set:
            _dict['cover_image'] = None

        # set to None if flags (nullable) is None
        # and model_fields_set contains the field
        if self.flags is None and "flags" in self.model_fields_set:
            _dict['flags'] = None

        # set to None if interactions_endpoint_url (nullable) is None
        # and model_fields_set contains the field
        if self.interactions_endpoint_url is None and "interactions_endpoint_url" in self.model_fields_set:
            _dict['interactions_endpoint_url'] = None

        # set to None if max_participants (nullable) is None
        # and model_fields_set contains the field
        if self.max_participants is None and "max_participants" in self.model_fields_set:
            _dict['max_participants'] = None

        # set to None if type (nullable) is None
        # and model_fields_set contains the field
        if self.type is None and "type" in self.model_fields_set:
            _dict['type'] = None

        # set to None if tags (nullable) is None
        # and model_fields_set contains the field
        if self.tags is None and "tags" in self.model_fields_set:
            _dict['tags'] = None

        # set to None if custom_install_url (nullable) is None
        # and model_fields_set contains the field
        if self.custom_install_url is None and "custom_install_url" in self.model_fields_set:
            _dict['custom_install_url'] = None

        # set to None if install_params (nullable) is None
        # and model_fields_set contains the field
        if self.install_params is None and "install_params" in self.model_fields_set:
            _dict['install_params'] = None

        # set to None if role_connections_verification_url (nullable) is None
        # and model_fields_set contains the field
        if self.role_connections_verification_url is None and "role_connections_verification_url" in self.model_fields_set:
            _dict['role_connections_verification_url'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ApplicationFormPartial from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        # raise errors for additional fields in the input
        for _key in obj.keys():
            if _key not in cls.__properties:
                raise ValueError("Error due to additional fields (not defined in ApplicationFormPartial) in the input: " + _key)

        _obj = cls.model_validate({
            "description": ApplicationFormPartialDescription.from_dict(obj["description"]) if obj.get("description") is not None else None,
            "icon": obj.get("icon"),
            "cover_image": obj.get("cover_image"),
            "team_id": obj.get("team_id"),
            "flags": obj.get("flags"),
            "interactions_endpoint_url": obj.get("interactions_endpoint_url"),
            "explicit_content_filter": obj.get("explicit_content_filter"),
            "max_participants": obj.get("max_participants"),
            "type": obj.get("type"),
            "tags": obj.get("tags"),
            "custom_install_url": obj.get("custom_install_url"),
            "install_params": ApplicationOAuth2InstallParams.from_dict(obj["install_params"]) if obj.get("install_params") is not None else None,
            "role_connections_verification_url": obj.get("role_connections_verification_url"),
            "integration_types_config": dict(
                (_k, ApplicationFormPartialIntegrationTypesConfigValue.from_dict(_v))
                for _k, _v in obj["integration_types_config"].items()
            )
            if obj.get("integration_types_config") is not None
            else None
        })
        return _obj


