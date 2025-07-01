# MessageResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **int** |  | 
**content** | **str** |  | 
**mentions** | [**List[UserResponse]**](UserResponse.md) |  | 
**mention_roles** | **List[str]** |  | 
**attachments** | [**List[MessageAttachmentResponse]**](MessageAttachmentResponse.md) |  | 
**embeds** | [**List[MessageEmbedResponse]**](MessageEmbedResponse.md) |  | 
**timestamp** | **datetime** |  | 
**edited_timestamp** | **datetime** |  | [optional] 
**flags** | **int** |  | 
**components** | [**List[BasicMessageResponseComponentsInner]**](BasicMessageResponseComponentsInner.md) |  | 
**resolved** | [**ResolvedObjectsResponse**](ResolvedObjectsResponse.md) |  | [optional] 
**stickers** | [**List[GetSticker200Response]**](GetSticker200Response.md) |  | [optional] 
**sticker_items** | [**List[MessageStickerItemResponse]**](MessageStickerItemResponse.md) |  | [optional] 
**id** | **str** |  | 
**channel_id** | **str** |  | 
**author** | [**UserResponse**](UserResponse.md) |  | 
**pinned** | **bool** |  | 
**mention_everyone** | **bool** |  | 
**tts** | **bool** |  | 
**call** | [**MessageCallResponse**](MessageCallResponse.md) |  | [optional] 
**activity** | **object** |  | [optional] 
**application** | [**BasicApplicationResponse**](BasicApplicationResponse.md) |  | [optional] 
**application_id** | **str** |  | [optional] 
**interaction** | [**MessageInteractionResponse**](MessageInteractionResponse.md) |  | [optional] 
**nonce** | [**BasicMessageResponseNonce**](BasicMessageResponseNonce.md) |  | [optional] 
**webhook_id** | **str** |  | [optional] 
**message_reference** | [**MessageReferenceResponse**](MessageReferenceResponse.md) |  | [optional] 
**thread** | [**ThreadResponse**](ThreadResponse.md) |  | [optional] 
**mention_channels** | [**List[Optional[MessageMentionChannelResponse]]**](MessageMentionChannelResponse.md) |  | [optional] 
**role_subscription_data** | [**MessageRoleSubscriptionDataResponse**](MessageRoleSubscriptionDataResponse.md) |  | [optional] 
**purchase_notification** | [**PurchaseNotificationResponse**](PurchaseNotificationResponse.md) |  | [optional] 
**position** | **int** |  | [optional] 
**poll** | [**PollResponse**](PollResponse.md) |  | [optional] 
**interaction_metadata** | [**BasicMessageResponseInteractionMetadata**](BasicMessageResponseInteractionMetadata.md) |  | [optional] 
**message_snapshots** | [**List[MessageSnapshotResponse]**](MessageSnapshotResponse.md) |  | [optional] 
**reactions** | [**List[MessageReactionResponse]**](MessageReactionResponse.md) |  | [optional] 
**referenced_message** | [**BasicMessageResponse**](BasicMessageResponse.md) |  | [optional] 

## Example

```python
from dc_rest.models.message_response import MessageResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MessageResponse from a JSON string
message_response_instance = MessageResponse.from_json(json)
# print the JSON string representation of the object
print(MessageResponse.to_json())

# convert the object into a dict
message_response_dict = message_response_instance.to_dict()
# create an instance of MessageResponse from a dict
message_response_from_dict = MessageResponse.from_dict(message_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


