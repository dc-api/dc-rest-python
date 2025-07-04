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
from dc_rest.models.application_integration_type_configuration_response import ApplicationIntegrationTypeConfigurationResponse
from dc_rest.models.application_o_auth2_install_params_response import ApplicationOAuth2InstallParamsResponse
from dc_rest.models.team_response import TeamResponse
from dc_rest.models.user_response import UserResponse
from typing import Optional, Set
from typing_extensions import Self

class PrivateApplicationResponse(BaseModel):
    """
    PrivateApplicationResponse
    """ # noqa: E501
    id: Annotated[str, Field(strict=True)]
    name: StrictStr
    icon: Optional[StrictStr] = None
    description: StrictStr
    type: Optional[StrictInt] = None
    cover_image: Optional[StrictStr] = None
    primary_sku_id: Optional[Annotated[str, Field(strict=True)]] = None
    bot: Optional[UserResponse] = None
    slug: Optional[StrictStr] = None
    guild_id: Optional[Annotated[str, Field(strict=True)]] = None
    rpc_origins: Optional[List[Optional[StrictStr]]] = None
    bot_public: Optional[StrictBool] = None
    bot_require_code_grant: Optional[StrictBool] = None
    terms_of_service_url: Optional[StrictStr] = None
    privacy_policy_url: Optional[StrictStr] = None
    custom_install_url: Optional[StrictStr] = None
    install_params: Optional[ApplicationOAuth2InstallParamsResponse] = None
    integration_types_config: Optional[Dict[str, ApplicationIntegrationTypeConfigurationResponse]] = None
    verify_key: StrictStr
    flags: StrictInt
    max_participants: Optional[StrictInt] = None
    tags: Optional[List[StrictStr]] = None
    redirect_uris: List[Optional[StrictStr]]
    interactions_endpoint_url: Optional[StrictStr] = None
    role_connections_verification_url: Optional[StrictStr] = None
    owner: UserResponse
    approximate_guild_count: Optional[StrictInt] = None
    approximate_user_install_count: StrictInt
    approximate_user_authorization_count: StrictInt
    explicit_content_filter: StrictInt
    team: Optional[TeamResponse] = None
    __properties: ClassVar[List[str]] = ["id", "name", "icon", "description", "type", "cover_image", "primary_sku_id", "bot", "slug", "guild_id", "rpc_origins", "bot_public", "bot_require_code_grant", "terms_of_service_url", "privacy_policy_url", "custom_install_url", "install_params", "integration_types_config", "verify_key", "flags", "max_participants", "tags", "redirect_uris", "interactions_endpoint_url", "role_connections_verification_url", "owner", "approximate_guild_count", "approximate_user_install_count", "approximate_user_authorization_count", "explicit_content_filter", "team"]

    @field_validator('id')
    def id_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^(0|[1-9][0-9]*)$", value):
            raise ValueError(r"must validate the regular expression /^(0|[1-9][0-9]*)$/")
        return value

    @field_validator('primary_sku_id')
    def primary_sku_id_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^(0|[1-9][0-9]*)$", value):
            raise ValueError(r"must validate the regular expression /^(0|[1-9][0-9]*)$/")
        return value

    @field_validator('guild_id')
    def guild_id_validate_regular_expression(cls, value):
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
        """Create an instance of PrivateApplicationResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of bot
        if self.bot:
            _dict['bot'] = self.bot.to_dict()
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
        # override the default output from pydantic by calling `to_dict()` of owner
        if self.owner:
            _dict['owner'] = self.owner.to_dict()
        # override the default output from pydantic by calling `to_dict()` of team
        if self.team:
            _dict['team'] = self.team.to_dict()
        # set to None if icon (nullable) is None
        # and model_fields_set contains the field
        if self.icon is None and "icon" in self.model_fields_set:
            _dict['icon'] = None

        # set to None if type (nullable) is None
        # and model_fields_set contains the field
        if self.type is None and "type" in self.model_fields_set:
            _dict['type'] = None

        # set to None if cover_image (nullable) is None
        # and model_fields_set contains the field
        if self.cover_image is None and "cover_image" in self.model_fields_set:
            _dict['cover_image'] = None

        # set to None if bot (nullable) is None
        # and model_fields_set contains the field
        if self.bot is None and "bot" in self.model_fields_set:
            _dict['bot'] = None

        # set to None if slug (nullable) is None
        # and model_fields_set contains the field
        if self.slug is None and "slug" in self.model_fields_set:
            _dict['slug'] = None

        # set to None if rpc_origins (nullable) is None
        # and model_fields_set contains the field
        if self.rpc_origins is None and "rpc_origins" in self.model_fields_set:
            _dict['rpc_origins'] = None

        # set to None if bot_public (nullable) is None
        # and model_fields_set contains the field
        if self.bot_public is None and "bot_public" in self.model_fields_set:
            _dict['bot_public'] = None

        # set to None if bot_require_code_grant (nullable) is None
        # and model_fields_set contains the field
        if self.bot_require_code_grant is None and "bot_require_code_grant" in self.model_fields_set:
            _dict['bot_require_code_grant'] = None

        # set to None if terms_of_service_url (nullable) is None
        # and model_fields_set contains the field
        if self.terms_of_service_url is None and "terms_of_service_url" in self.model_fields_set:
            _dict['terms_of_service_url'] = None

        # set to None if privacy_policy_url (nullable) is None
        # and model_fields_set contains the field
        if self.privacy_policy_url is None and "privacy_policy_url" in self.model_fields_set:
            _dict['privacy_policy_url'] = None

        # set to None if custom_install_url (nullable) is None
        # and model_fields_set contains the field
        if self.custom_install_url is None and "custom_install_url" in self.model_fields_set:
            _dict['custom_install_url'] = None

        # set to None if install_params (nullable) is None
        # and model_fields_set contains the field
        if self.install_params is None and "install_params" in self.model_fields_set:
            _dict['install_params'] = None

        # set to None if max_participants (nullable) is None
        # and model_fields_set contains the field
        if self.max_participants is None and "max_participants" in self.model_fields_set:
            _dict['max_participants'] = None

        # set to None if tags (nullable) is None
        # and model_fields_set contains the field
        if self.tags is None and "tags" in self.model_fields_set:
            _dict['tags'] = None

        # set to None if interactions_endpoint_url (nullable) is None
        # and model_fields_set contains the field
        if self.interactions_endpoint_url is None and "interactions_endpoint_url" in self.model_fields_set:
            _dict['interactions_endpoint_url'] = None

        # set to None if role_connections_verification_url (nullable) is None
        # and model_fields_set contains the field
        if self.role_connections_verification_url is None and "role_connections_verification_url" in self.model_fields_set:
            _dict['role_connections_verification_url'] = None

        # set to None if approximate_guild_count (nullable) is None
        # and model_fields_set contains the field
        if self.approximate_guild_count is None and "approximate_guild_count" in self.model_fields_set:
            _dict['approximate_guild_count'] = None

        # set to None if team (nullable) is None
        # and model_fields_set contains the field
        if self.team is None and "team" in self.model_fields_set:
            _dict['team'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PrivateApplicationResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        # raise errors for additional fields in the input
        for _key in obj.keys():
            if _key not in cls.__properties:
                raise ValueError("Error due to additional fields (not defined in PrivateApplicationResponse) in the input: " + _key)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "icon": obj.get("icon"),
            "description": obj.get("description"),
            "type": obj.get("type"),
            "cover_image": obj.get("cover_image"),
            "primary_sku_id": obj.get("primary_sku_id"),
            "bot": UserResponse.from_dict(obj["bot"]) if obj.get("bot") is not None else None,
            "slug": obj.get("slug"),
            "guild_id": obj.get("guild_id"),
            "rpc_origins": obj.get("rpc_origins"),
            "bot_public": obj.get("bot_public"),
            "bot_require_code_grant": obj.get("bot_require_code_grant"),
            "terms_of_service_url": obj.get("terms_of_service_url"),
            "privacy_policy_url": obj.get("privacy_policy_url"),
            "custom_install_url": obj.get("custom_install_url"),
            "install_params": ApplicationOAuth2InstallParamsResponse.from_dict(obj["install_params"]) if obj.get("install_params") is not None else None,
            "integration_types_config": dict(
                (_k, ApplicationIntegrationTypeConfigurationResponse.from_dict(_v))
                for _k, _v in obj["integration_types_config"].items()
            )
            if obj.get("integration_types_config") is not None
            else None,
            "verify_key": obj.get("verify_key"),
            "flags": obj.get("flags"),
            "max_participants": obj.get("max_participants"),
            "tags": obj.get("tags"),
            "redirect_uris": obj.get("redirect_uris"),
            "interactions_endpoint_url": obj.get("interactions_endpoint_url"),
            "role_connections_verification_url": obj.get("role_connections_verification_url"),
            "owner": UserResponse.from_dict(obj["owner"]) if obj.get("owner") is not None else None,
            "approximate_guild_count": obj.get("approximate_guild_count"),
            "approximate_user_install_count": obj.get("approximate_user_install_count"),
            "approximate_user_authorization_count": obj.get("approximate_user_authorization_count"),
            "explicit_content_filter": obj.get("explicit_content_filter"),
            "team": TeamResponse.from_dict(obj["team"]) if obj.get("team") is not None else None
        })
        return _obj


