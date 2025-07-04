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

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List, Optional
from dc_rest.models.application_command_response import ApplicationCommandResponse
from dc_rest.models.audit_log_entry_response import AuditLogEntryResponse
from dc_rest.models.guild_audit_log_response_integrations_inner import GuildAuditLogResponseIntegrationsInner
from dc_rest.models.list_auto_moderation_rules200_response_inner import ListAutoModerationRules200ResponseInner
from dc_rest.models.list_channel_webhooks200_response_inner import ListChannelWebhooks200ResponseInner
from dc_rest.models.list_guild_scheduled_events200_response_inner import ListGuildScheduledEvents200ResponseInner
from dc_rest.models.thread_response import ThreadResponse
from dc_rest.models.user_response import UserResponse
from typing import Optional, Set
from typing_extensions import Self

class GuildAuditLogResponse(BaseModel):
    """
    GuildAuditLogResponse
    """ # noqa: E501
    audit_log_entries: List[AuditLogEntryResponse]
    users: List[UserResponse]
    integrations: List[GuildAuditLogResponseIntegrationsInner]
    webhooks: List[ListChannelWebhooks200ResponseInner]
    guild_scheduled_events: List[ListGuildScheduledEvents200ResponseInner]
    threads: List[ThreadResponse]
    application_commands: List[ApplicationCommandResponse]
    auto_moderation_rules: List[Optional[ListAutoModerationRules200ResponseInner]]
    __properties: ClassVar[List[str]] = ["audit_log_entries", "users", "integrations", "webhooks", "guild_scheduled_events", "threads", "application_commands", "auto_moderation_rules"]

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
        """Create an instance of GuildAuditLogResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in audit_log_entries (list)
        _items = []
        if self.audit_log_entries:
            for _item_audit_log_entries in self.audit_log_entries:
                if _item_audit_log_entries:
                    _items.append(_item_audit_log_entries.to_dict())
            _dict['audit_log_entries'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in users (list)
        _items = []
        if self.users:
            for _item_users in self.users:
                if _item_users:
                    _items.append(_item_users.to_dict())
            _dict['users'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in integrations (list)
        _items = []
        if self.integrations:
            for _item_integrations in self.integrations:
                if _item_integrations:
                    _items.append(_item_integrations.to_dict())
            _dict['integrations'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in webhooks (list)
        _items = []
        if self.webhooks:
            for _item_webhooks in self.webhooks:
                if _item_webhooks:
                    _items.append(_item_webhooks.to_dict())
            _dict['webhooks'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in guild_scheduled_events (list)
        _items = []
        if self.guild_scheduled_events:
            for _item_guild_scheduled_events in self.guild_scheduled_events:
                if _item_guild_scheduled_events:
                    _items.append(_item_guild_scheduled_events.to_dict())
            _dict['guild_scheduled_events'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in threads (list)
        _items = []
        if self.threads:
            for _item_threads in self.threads:
                if _item_threads:
                    _items.append(_item_threads.to_dict())
            _dict['threads'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in application_commands (list)
        _items = []
        if self.application_commands:
            for _item_application_commands in self.application_commands:
                if _item_application_commands:
                    _items.append(_item_application_commands.to_dict())
            _dict['application_commands'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in auto_moderation_rules (list)
        _items = []
        if self.auto_moderation_rules:
            for _item_auto_moderation_rules in self.auto_moderation_rules:
                if _item_auto_moderation_rules:
                    _items.append(_item_auto_moderation_rules.to_dict())
            _dict['auto_moderation_rules'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GuildAuditLogResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        # raise errors for additional fields in the input
        for _key in obj.keys():
            if _key not in cls.__properties:
                raise ValueError("Error due to additional fields (not defined in GuildAuditLogResponse) in the input: " + _key)

        _obj = cls.model_validate({
            "audit_log_entries": [AuditLogEntryResponse.from_dict(_item) for _item in obj["audit_log_entries"]] if obj.get("audit_log_entries") is not None else None,
            "users": [UserResponse.from_dict(_item) for _item in obj["users"]] if obj.get("users") is not None else None,
            "integrations": [GuildAuditLogResponseIntegrationsInner.from_dict(_item) for _item in obj["integrations"]] if obj.get("integrations") is not None else None,
            "webhooks": [ListChannelWebhooks200ResponseInner.from_dict(_item) for _item in obj["webhooks"]] if obj.get("webhooks") is not None else None,
            "guild_scheduled_events": [ListGuildScheduledEvents200ResponseInner.from_dict(_item) for _item in obj["guild_scheduled_events"]] if obj.get("guild_scheduled_events") is not None else None,
            "threads": [ThreadResponse.from_dict(_item) for _item in obj["threads"]] if obj.get("threads") is not None else None,
            "application_commands": [ApplicationCommandResponse.from_dict(_item) for _item in obj["application_commands"]] if obj.get("application_commands") is not None else None,
            "auto_moderation_rules": [ListAutoModerationRules200ResponseInner.from_dict(_item) for _item in obj["auto_moderation_rules"]] if obj.get("auto_moderation_rules") is not None else None
        })
        return _obj


