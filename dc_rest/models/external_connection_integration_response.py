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

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from dc_rest.models.account_response import AccountResponse
from dc_rest.models.user_response import UserResponse
from typing import Optional, Set
from typing_extensions import Self

class ExternalConnectionIntegrationResponse(BaseModel):
    """
    ExternalConnectionIntegrationResponse
    """ # noqa: E501
    type: Optional[StrictStr]
    name: Optional[StrictStr] = None
    account: Optional[AccountResponse] = None
    enabled: Optional[StrictBool] = None
    id: StrictStr
    user: UserResponse
    revoked: Optional[StrictBool] = None
    expire_behavior: Optional[StrictInt] = None
    expire_grace_period: Optional[StrictInt] = None
    subscriber_count: Optional[StrictInt] = None
    synced_at: Optional[datetime] = None
    role_id: Optional[Annotated[str, Field(strict=True)]] = None
    syncing: Optional[StrictBool] = None
    enable_emoticons: Optional[StrictBool] = None
    __properties: ClassVar[List[str]] = ["type", "name", "account", "enabled", "id", "user", "revoked", "expire_behavior", "expire_grace_period", "subscriber_count", "synced_at", "role_id", "syncing", "enable_emoticons"]

    @field_validator('role_id')
    def role_id_validate_regular_expression(cls, value):
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
        """Create an instance of ExternalConnectionIntegrationResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of account
        if self.account:
            _dict['account'] = self.account.to_dict()
        # override the default output from pydantic by calling `to_dict()` of user
        if self.user:
            _dict['user'] = self.user.to_dict()
        # set to None if type (nullable) is None
        # and model_fields_set contains the field
        if self.type is None and "type" in self.model_fields_set:
            _dict['type'] = None

        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        # set to None if account (nullable) is None
        # and model_fields_set contains the field
        if self.account is None and "account" in self.model_fields_set:
            _dict['account'] = None

        # set to None if enabled (nullable) is None
        # and model_fields_set contains the field
        if self.enabled is None and "enabled" in self.model_fields_set:
            _dict['enabled'] = None

        # set to None if revoked (nullable) is None
        # and model_fields_set contains the field
        if self.revoked is None and "revoked" in self.model_fields_set:
            _dict['revoked'] = None

        # set to None if subscriber_count (nullable) is None
        # and model_fields_set contains the field
        if self.subscriber_count is None and "subscriber_count" in self.model_fields_set:
            _dict['subscriber_count'] = None

        # set to None if synced_at (nullable) is None
        # and model_fields_set contains the field
        if self.synced_at is None and "synced_at" in self.model_fields_set:
            _dict['synced_at'] = None

        # set to None if syncing (nullable) is None
        # and model_fields_set contains the field
        if self.syncing is None and "syncing" in self.model_fields_set:
            _dict['syncing'] = None

        # set to None if enable_emoticons (nullable) is None
        # and model_fields_set contains the field
        if self.enable_emoticons is None and "enable_emoticons" in self.model_fields_set:
            _dict['enable_emoticons'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ExternalConnectionIntegrationResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        # raise errors for additional fields in the input
        for _key in obj.keys():
            if _key not in cls.__properties:
                raise ValueError("Error due to additional fields (not defined in ExternalConnectionIntegrationResponse) in the input: " + _key)

        _obj = cls.model_validate({
            "type": obj.get("type"),
            "name": obj.get("name"),
            "account": AccountResponse.from_dict(obj["account"]) if obj.get("account") is not None else None,
            "enabled": obj.get("enabled"),
            "id": obj.get("id"),
            "user": UserResponse.from_dict(obj["user"]) if obj.get("user") is not None else None,
            "revoked": obj.get("revoked"),
            "expire_behavior": obj.get("expire_behavior"),
            "expire_grace_period": obj.get("expire_grace_period"),
            "subscriber_count": obj.get("subscriber_count"),
            "synced_at": obj.get("synced_at"),
            "role_id": obj.get("role_id"),
            "syncing": obj.get("syncing"),
            "enable_emoticons": obj.get("enable_emoticons")
        })
        return _obj


