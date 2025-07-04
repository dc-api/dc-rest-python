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

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from dc_rest.models.scheduled_event_user_response import ScheduledEventUserResponse
from dc_rest.models.user_response import UserResponse
from typing import Optional, Set
from typing_extensions import Self

class StageScheduledEventResponse(BaseModel):
    """
    StageScheduledEventResponse
    """ # noqa: E501
    id: Annotated[str, Field(strict=True)]
    guild_id: Annotated[str, Field(strict=True)]
    name: StrictStr
    description: Optional[StrictStr] = None
    channel_id: Optional[Annotated[str, Field(strict=True)]] = None
    creator_id: Optional[Annotated[str, Field(strict=True)]] = None
    creator: Optional[UserResponse] = None
    image: Optional[StrictStr] = None
    scheduled_start_time: datetime
    scheduled_end_time: Optional[datetime] = None
    status: Optional[StrictInt]
    entity_type: Optional[StrictInt]
    entity_id: Optional[Annotated[str, Field(strict=True)]] = None
    user_count: Optional[StrictInt] = None
    privacy_level: Optional[Any]
    user_rsvp: Optional[ScheduledEventUserResponse] = None
    entity_metadata: Optional[Dict[str, Any]] = None
    __properties: ClassVar[List[str]] = ["id", "guild_id", "name", "description", "channel_id", "creator_id", "creator", "image", "scheduled_start_time", "scheduled_end_time", "status", "entity_type", "entity_id", "user_count", "privacy_level", "user_rsvp", "entity_metadata"]

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

    @field_validator('channel_id')
    def channel_id_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^(0|[1-9][0-9]*)$", value):
            raise ValueError(r"must validate the regular expression /^(0|[1-9][0-9]*)$/")
        return value

    @field_validator('creator_id')
    def creator_id_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^(0|[1-9][0-9]*)$", value):
            raise ValueError(r"must validate the regular expression /^(0|[1-9][0-9]*)$/")
        return value

    @field_validator('entity_id')
    def entity_id_validate_regular_expression(cls, value):
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
        """Create an instance of StageScheduledEventResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of creator
        if self.creator:
            _dict['creator'] = self.creator.to_dict()
        # override the default output from pydantic by calling `to_dict()` of user_rsvp
        if self.user_rsvp:
            _dict['user_rsvp'] = self.user_rsvp.to_dict()
        # set to None if description (nullable) is None
        # and model_fields_set contains the field
        if self.description is None and "description" in self.model_fields_set:
            _dict['description'] = None

        # set to None if creator (nullable) is None
        # and model_fields_set contains the field
        if self.creator is None and "creator" in self.model_fields_set:
            _dict['creator'] = None

        # set to None if image (nullable) is None
        # and model_fields_set contains the field
        if self.image is None and "image" in self.model_fields_set:
            _dict['image'] = None

        # set to None if scheduled_end_time (nullable) is None
        # and model_fields_set contains the field
        if self.scheduled_end_time is None and "scheduled_end_time" in self.model_fields_set:
            _dict['scheduled_end_time'] = None

        # set to None if status (nullable) is None
        # and model_fields_set contains the field
        if self.status is None and "status" in self.model_fields_set:
            _dict['status'] = None

        # set to None if entity_type (nullable) is None
        # and model_fields_set contains the field
        if self.entity_type is None and "entity_type" in self.model_fields_set:
            _dict['entity_type'] = None

        # set to None if user_count (nullable) is None
        # and model_fields_set contains the field
        if self.user_count is None and "user_count" in self.model_fields_set:
            _dict['user_count'] = None

        # set to None if privacy_level (nullable) is None
        # and model_fields_set contains the field
        if self.privacy_level is None and "privacy_level" in self.model_fields_set:
            _dict['privacy_level'] = None

        # set to None if user_rsvp (nullable) is None
        # and model_fields_set contains the field
        if self.user_rsvp is None and "user_rsvp" in self.model_fields_set:
            _dict['user_rsvp'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of StageScheduledEventResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        # raise errors for additional fields in the input
        for _key in obj.keys():
            if _key not in cls.__properties:
                raise ValueError("Error due to additional fields (not defined in StageScheduledEventResponse) in the input: " + _key)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "guild_id": obj.get("guild_id"),
            "name": obj.get("name"),
            "description": obj.get("description"),
            "channel_id": obj.get("channel_id"),
            "creator_id": obj.get("creator_id"),
            "creator": UserResponse.from_dict(obj["creator"]) if obj.get("creator") is not None else None,
            "image": obj.get("image"),
            "scheduled_start_time": obj.get("scheduled_start_time"),
            "scheduled_end_time": obj.get("scheduled_end_time"),
            "status": obj.get("status"),
            "entity_type": obj.get("entity_type"),
            "entity_id": obj.get("entity_id"),
            "user_count": obj.get("user_count"),
            "privacy_level": obj.get("privacy_level"),
            "user_rsvp": ScheduledEventUserResponse.from_dict(obj["user_rsvp"]) if obj.get("user_rsvp") is not None else None,
            "entity_metadata": obj.get("entity_metadata")
        })
        return _obj


