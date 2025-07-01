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

from pydantic import BaseModel, ConfigDict, StrictBool
from typing import Any, ClassVar, Dict, List, Optional
from dc_rest.models.message_response import MessageResponse
from dc_rest.models.thread_member_response import ThreadMemberResponse
from dc_rest.models.thread_response import ThreadResponse
from typing import Optional, Set
from typing_extensions import Self

class ThreadsResponse(BaseModel):
    """
    ThreadsResponse
    """ # noqa: E501
    threads: List[ThreadResponse]
    members: List[ThreadMemberResponse]
    has_more: Optional[StrictBool] = None
    first_messages: Optional[List[MessageResponse]] = None
    __properties: ClassVar[List[str]] = ["threads", "members", "has_more", "first_messages"]

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
        """Create an instance of ThreadsResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in threads (list)
        _items = []
        if self.threads:
            for _item_threads in self.threads:
                if _item_threads:
                    _items.append(_item_threads.to_dict())
            _dict['threads'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in members (list)
        _items = []
        if self.members:
            for _item_members in self.members:
                if _item_members:
                    _items.append(_item_members.to_dict())
            _dict['members'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in first_messages (list)
        _items = []
        if self.first_messages:
            for _item_first_messages in self.first_messages:
                if _item_first_messages:
                    _items.append(_item_first_messages.to_dict())
            _dict['first_messages'] = _items
        # set to None if has_more (nullable) is None
        # and model_fields_set contains the field
        if self.has_more is None and "has_more" in self.model_fields_set:
            _dict['has_more'] = None

        # set to None if first_messages (nullable) is None
        # and model_fields_set contains the field
        if self.first_messages is None and "first_messages" in self.model_fields_set:
            _dict['first_messages'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ThreadsResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        # raise errors for additional fields in the input
        for _key in obj.keys():
            if _key not in cls.__properties:
                raise ValueError("Error due to additional fields (not defined in ThreadsResponse) in the input: " + _key)

        _obj = cls.model_validate({
            "threads": [ThreadResponse.from_dict(_item) for _item in obj["threads"]] if obj.get("threads") is not None else None,
            "members": [ThreadMemberResponse.from_dict(_item) for _item in obj["members"]] if obj.get("members") is not None else None,
            "has_more": obj.get("has_more"),
            "first_messages": [MessageResponse.from_dict(_item) for _item in obj["first_messages"]] if obj.get("first_messages") is not None else None
        })
        return _obj


