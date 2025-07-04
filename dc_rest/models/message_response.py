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
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from dc_rest.models.basic_application_response import BasicApplicationResponse
from dc_rest.models.basic_message_response import BasicMessageResponse
from dc_rest.models.basic_message_response_components_inner import BasicMessageResponseComponentsInner
from dc_rest.models.basic_message_response_interaction_metadata import BasicMessageResponseInteractionMetadata
from dc_rest.models.basic_message_response_nonce import BasicMessageResponseNonce
from dc_rest.models.get_sticker200_response import GetSticker200Response
from dc_rest.models.message_attachment_response import MessageAttachmentResponse
from dc_rest.models.message_call_response import MessageCallResponse
from dc_rest.models.message_embed_response import MessageEmbedResponse
from dc_rest.models.message_interaction_response import MessageInteractionResponse
from dc_rest.models.message_mention_channel_response import MessageMentionChannelResponse
from dc_rest.models.message_reaction_response import MessageReactionResponse
from dc_rest.models.message_reference_response import MessageReferenceResponse
from dc_rest.models.message_role_subscription_data_response import MessageRoleSubscriptionDataResponse
from dc_rest.models.message_snapshot_response import MessageSnapshotResponse
from dc_rest.models.message_sticker_item_response import MessageStickerItemResponse
from dc_rest.models.poll_response import PollResponse
from dc_rest.models.purchase_notification_response import PurchaseNotificationResponse
from dc_rest.models.resolved_objects_response import ResolvedObjectsResponse
from dc_rest.models.thread_response import ThreadResponse
from dc_rest.models.user_response import UserResponse
from typing import Optional, Set
from typing_extensions import Self

class MessageResponse(BaseModel):
    """
    MessageResponse
    """ # noqa: E501
    type: StrictInt
    content: StrictStr
    mentions: List[UserResponse]
    mention_roles: List[Annotated[str, Field(strict=True)]]
    attachments: List[MessageAttachmentResponse]
    embeds: List[MessageEmbedResponse]
    timestamp: datetime
    edited_timestamp: Optional[datetime] = None
    flags: StrictInt
    components: List[BasicMessageResponseComponentsInner]
    resolved: Optional[ResolvedObjectsResponse] = None
    stickers: Optional[List[GetSticker200Response]] = None
    sticker_items: Optional[List[MessageStickerItemResponse]] = None
    id: Annotated[str, Field(strict=True)]
    channel_id: Annotated[str, Field(strict=True)]
    author: UserResponse
    pinned: StrictBool
    mention_everyone: StrictBool
    tts: StrictBool
    call: Optional[MessageCallResponse] = None
    activity: Optional[Dict[str, Any]] = None
    application: Optional[BasicApplicationResponse] = None
    application_id: Optional[Annotated[str, Field(strict=True)]] = None
    interaction: Optional[MessageInteractionResponse] = None
    nonce: Optional[BasicMessageResponseNonce] = None
    webhook_id: Optional[Annotated[str, Field(strict=True)]] = None
    message_reference: Optional[MessageReferenceResponse] = None
    thread: Optional[ThreadResponse] = None
    mention_channels: Optional[List[Optional[MessageMentionChannelResponse]]] = None
    role_subscription_data: Optional[MessageRoleSubscriptionDataResponse] = None
    purchase_notification: Optional[PurchaseNotificationResponse] = None
    position: Optional[StrictInt] = None
    poll: Optional[PollResponse] = None
    interaction_metadata: Optional[BasicMessageResponseInteractionMetadata] = None
    message_snapshots: Optional[List[MessageSnapshotResponse]] = None
    reactions: Optional[List[MessageReactionResponse]] = None
    referenced_message: Optional[BasicMessageResponse] = None
    __properties: ClassVar[List[str]] = ["type", "content", "mentions", "mention_roles", "attachments", "embeds", "timestamp", "edited_timestamp", "flags", "components", "resolved", "stickers", "sticker_items", "id", "channel_id", "author", "pinned", "mention_everyone", "tts", "call", "activity", "application", "application_id", "interaction", "nonce", "webhook_id", "message_reference", "thread", "mention_channels", "role_subscription_data", "purchase_notification", "position", "poll", "interaction_metadata", "message_snapshots", "reactions", "referenced_message"]

    @field_validator('id')
    def id_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^(0|[1-9][0-9]*)$", value):
            raise ValueError(r"must validate the regular expression /^(0|[1-9][0-9]*)$/")
        return value

    @field_validator('channel_id')
    def channel_id_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^(0|[1-9][0-9]*)$", value):
            raise ValueError(r"must validate the regular expression /^(0|[1-9][0-9]*)$/")
        return value

    @field_validator('application_id')
    def application_id_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^(0|[1-9][0-9]*)$", value):
            raise ValueError(r"must validate the regular expression /^(0|[1-9][0-9]*)$/")
        return value

    @field_validator('webhook_id')
    def webhook_id_validate_regular_expression(cls, value):
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
        """Create an instance of MessageResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in mentions (list)
        _items = []
        if self.mentions:
            for _item_mentions in self.mentions:
                if _item_mentions:
                    _items.append(_item_mentions.to_dict())
            _dict['mentions'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in attachments (list)
        _items = []
        if self.attachments:
            for _item_attachments in self.attachments:
                if _item_attachments:
                    _items.append(_item_attachments.to_dict())
            _dict['attachments'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in embeds (list)
        _items = []
        if self.embeds:
            for _item_embeds in self.embeds:
                if _item_embeds:
                    _items.append(_item_embeds.to_dict())
            _dict['embeds'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in components (list)
        _items = []
        if self.components:
            for _item_components in self.components:
                if _item_components:
                    _items.append(_item_components.to_dict())
            _dict['components'] = _items
        # override the default output from pydantic by calling `to_dict()` of resolved
        if self.resolved:
            _dict['resolved'] = self.resolved.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in stickers (list)
        _items = []
        if self.stickers:
            for _item_stickers in self.stickers:
                if _item_stickers:
                    _items.append(_item_stickers.to_dict())
            _dict['stickers'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in sticker_items (list)
        _items = []
        if self.sticker_items:
            for _item_sticker_items in self.sticker_items:
                if _item_sticker_items:
                    _items.append(_item_sticker_items.to_dict())
            _dict['sticker_items'] = _items
        # override the default output from pydantic by calling `to_dict()` of author
        if self.author:
            _dict['author'] = self.author.to_dict()
        # override the default output from pydantic by calling `to_dict()` of call
        if self.call:
            _dict['call'] = self.call.to_dict()
        # override the default output from pydantic by calling `to_dict()` of application
        if self.application:
            _dict['application'] = self.application.to_dict()
        # override the default output from pydantic by calling `to_dict()` of interaction
        if self.interaction:
            _dict['interaction'] = self.interaction.to_dict()
        # override the default output from pydantic by calling `to_dict()` of nonce
        if self.nonce:
            _dict['nonce'] = self.nonce.to_dict()
        # override the default output from pydantic by calling `to_dict()` of message_reference
        if self.message_reference:
            _dict['message_reference'] = self.message_reference.to_dict()
        # override the default output from pydantic by calling `to_dict()` of thread
        if self.thread:
            _dict['thread'] = self.thread.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in mention_channels (list)
        _items = []
        if self.mention_channels:
            for _item_mention_channels in self.mention_channels:
                if _item_mention_channels:
                    _items.append(_item_mention_channels.to_dict())
            _dict['mention_channels'] = _items
        # override the default output from pydantic by calling `to_dict()` of role_subscription_data
        if self.role_subscription_data:
            _dict['role_subscription_data'] = self.role_subscription_data.to_dict()
        # override the default output from pydantic by calling `to_dict()` of purchase_notification
        if self.purchase_notification:
            _dict['purchase_notification'] = self.purchase_notification.to_dict()
        # override the default output from pydantic by calling `to_dict()` of poll
        if self.poll:
            _dict['poll'] = self.poll.to_dict()
        # override the default output from pydantic by calling `to_dict()` of interaction_metadata
        if self.interaction_metadata:
            _dict['interaction_metadata'] = self.interaction_metadata.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in message_snapshots (list)
        _items = []
        if self.message_snapshots:
            for _item_message_snapshots in self.message_snapshots:
                if _item_message_snapshots:
                    _items.append(_item_message_snapshots.to_dict())
            _dict['message_snapshots'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in reactions (list)
        _items = []
        if self.reactions:
            for _item_reactions in self.reactions:
                if _item_reactions:
                    _items.append(_item_reactions.to_dict())
            _dict['reactions'] = _items
        # override the default output from pydantic by calling `to_dict()` of referenced_message
        if self.referenced_message:
            _dict['referenced_message'] = self.referenced_message.to_dict()
        # set to None if edited_timestamp (nullable) is None
        # and model_fields_set contains the field
        if self.edited_timestamp is None and "edited_timestamp" in self.model_fields_set:
            _dict['edited_timestamp'] = None

        # set to None if resolved (nullable) is None
        # and model_fields_set contains the field
        if self.resolved is None and "resolved" in self.model_fields_set:
            _dict['resolved'] = None

        # set to None if stickers (nullable) is None
        # and model_fields_set contains the field
        if self.stickers is None and "stickers" in self.model_fields_set:
            _dict['stickers'] = None

        # set to None if sticker_items (nullable) is None
        # and model_fields_set contains the field
        if self.sticker_items is None and "sticker_items" in self.model_fields_set:
            _dict['sticker_items'] = None

        # set to None if call (nullable) is None
        # and model_fields_set contains the field
        if self.call is None and "call" in self.model_fields_set:
            _dict['call'] = None

        # set to None if application (nullable) is None
        # and model_fields_set contains the field
        if self.application is None and "application" in self.model_fields_set:
            _dict['application'] = None

        # set to None if interaction (nullable) is None
        # and model_fields_set contains the field
        if self.interaction is None and "interaction" in self.model_fields_set:
            _dict['interaction'] = None

        # set to None if nonce (nullable) is None
        # and model_fields_set contains the field
        if self.nonce is None and "nonce" in self.model_fields_set:
            _dict['nonce'] = None

        # set to None if message_reference (nullable) is None
        # and model_fields_set contains the field
        if self.message_reference is None and "message_reference" in self.model_fields_set:
            _dict['message_reference'] = None

        # set to None if thread (nullable) is None
        # and model_fields_set contains the field
        if self.thread is None and "thread" in self.model_fields_set:
            _dict['thread'] = None

        # set to None if mention_channels (nullable) is None
        # and model_fields_set contains the field
        if self.mention_channels is None and "mention_channels" in self.model_fields_set:
            _dict['mention_channels'] = None

        # set to None if role_subscription_data (nullable) is None
        # and model_fields_set contains the field
        if self.role_subscription_data is None and "role_subscription_data" in self.model_fields_set:
            _dict['role_subscription_data'] = None

        # set to None if purchase_notification (nullable) is None
        # and model_fields_set contains the field
        if self.purchase_notification is None and "purchase_notification" in self.model_fields_set:
            _dict['purchase_notification'] = None

        # set to None if position (nullable) is None
        # and model_fields_set contains the field
        if self.position is None and "position" in self.model_fields_set:
            _dict['position'] = None

        # set to None if poll (nullable) is None
        # and model_fields_set contains the field
        if self.poll is None and "poll" in self.model_fields_set:
            _dict['poll'] = None

        # set to None if interaction_metadata (nullable) is None
        # and model_fields_set contains the field
        if self.interaction_metadata is None and "interaction_metadata" in self.model_fields_set:
            _dict['interaction_metadata'] = None

        # set to None if message_snapshots (nullable) is None
        # and model_fields_set contains the field
        if self.message_snapshots is None and "message_snapshots" in self.model_fields_set:
            _dict['message_snapshots'] = None

        # set to None if reactions (nullable) is None
        # and model_fields_set contains the field
        if self.reactions is None and "reactions" in self.model_fields_set:
            _dict['reactions'] = None

        # set to None if referenced_message (nullable) is None
        # and model_fields_set contains the field
        if self.referenced_message is None and "referenced_message" in self.model_fields_set:
            _dict['referenced_message'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of MessageResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        # raise errors for additional fields in the input
        for _key in obj.keys():
            if _key not in cls.__properties:
                raise ValueError("Error due to additional fields (not defined in MessageResponse) in the input: " + _key)

        _obj = cls.model_validate({
            "type": obj.get("type"),
            "content": obj.get("content"),
            "mentions": [UserResponse.from_dict(_item) for _item in obj["mentions"]] if obj.get("mentions") is not None else None,
            "mention_roles": obj.get("mention_roles"),
            "attachments": [MessageAttachmentResponse.from_dict(_item) for _item in obj["attachments"]] if obj.get("attachments") is not None else None,
            "embeds": [MessageEmbedResponse.from_dict(_item) for _item in obj["embeds"]] if obj.get("embeds") is not None else None,
            "timestamp": obj.get("timestamp"),
            "edited_timestamp": obj.get("edited_timestamp"),
            "flags": obj.get("flags"),
            "components": [BasicMessageResponseComponentsInner.from_dict(_item) for _item in obj["components"]] if obj.get("components") is not None else None,
            "resolved": ResolvedObjectsResponse.from_dict(obj["resolved"]) if obj.get("resolved") is not None else None,
            "stickers": [GetSticker200Response.from_dict(_item) for _item in obj["stickers"]] if obj.get("stickers") is not None else None,
            "sticker_items": [MessageStickerItemResponse.from_dict(_item) for _item in obj["sticker_items"]] if obj.get("sticker_items") is not None else None,
            "id": obj.get("id"),
            "channel_id": obj.get("channel_id"),
            "author": UserResponse.from_dict(obj["author"]) if obj.get("author") is not None else None,
            "pinned": obj.get("pinned"),
            "mention_everyone": obj.get("mention_everyone"),
            "tts": obj.get("tts"),
            "call": MessageCallResponse.from_dict(obj["call"]) if obj.get("call") is not None else None,
            "activity": obj.get("activity"),
            "application": BasicApplicationResponse.from_dict(obj["application"]) if obj.get("application") is not None else None,
            "application_id": obj.get("application_id"),
            "interaction": MessageInteractionResponse.from_dict(obj["interaction"]) if obj.get("interaction") is not None else None,
            "nonce": BasicMessageResponseNonce.from_dict(obj["nonce"]) if obj.get("nonce") is not None else None,
            "webhook_id": obj.get("webhook_id"),
            "message_reference": MessageReferenceResponse.from_dict(obj["message_reference"]) if obj.get("message_reference") is not None else None,
            "thread": ThreadResponse.from_dict(obj["thread"]) if obj.get("thread") is not None else None,
            "mention_channels": [MessageMentionChannelResponse.from_dict(_item) for _item in obj["mention_channels"]] if obj.get("mention_channels") is not None else None,
            "role_subscription_data": MessageRoleSubscriptionDataResponse.from_dict(obj["role_subscription_data"]) if obj.get("role_subscription_data") is not None else None,
            "purchase_notification": PurchaseNotificationResponse.from_dict(obj["purchase_notification"]) if obj.get("purchase_notification") is not None else None,
            "position": obj.get("position"),
            "poll": PollResponse.from_dict(obj["poll"]) if obj.get("poll") is not None else None,
            "interaction_metadata": BasicMessageResponseInteractionMetadata.from_dict(obj["interaction_metadata"]) if obj.get("interaction_metadata") is not None else None,
            "message_snapshots": [MessageSnapshotResponse.from_dict(_item) for _item in obj["message_snapshots"]] if obj.get("message_snapshots") is not None else None,
            "reactions": [MessageReactionResponse.from_dict(_item) for _item in obj["reactions"]] if obj.get("reactions") is not None else None,
            "referenced_message": BasicMessageResponse.from_dict(obj["referenced_message"]) if obj.get("referenced_message") is not None else None
        })
        return _obj


