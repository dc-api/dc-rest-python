# MessageCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | **str** |  | [optional] 
**embeds** | [**List[RichEmbed]**](RichEmbed.md) |  | [optional] 
**allowed_mentions** | [**MessageAllowedMentionsRequest**](MessageAllowedMentionsRequest.md) |  | [optional] 
**sticker_ids** | **List[str]** |  | [optional] 
**components** | [**List[BaseCreateMessageCreateRequestComponentsInner]**](BaseCreateMessageCreateRequestComponentsInner.md) |  | [optional] 
**flags** | **int** |  | [optional] 
**attachments** | [**List[MessageAttachmentRequest]**](MessageAttachmentRequest.md) |  | [optional] 
**poll** | [**PollCreateRequest**](PollCreateRequest.md) |  | [optional] 
**confetti_potion** | **object** |  | [optional] 
**message_reference** | [**MessageReferenceRequest**](MessageReferenceRequest.md) |  | [optional] 
**nonce** | [**BasicMessageResponseNonce**](BasicMessageResponseNonce.md) |  | [optional] 
**enforce_nonce** | **bool** |  | [optional] 
**tts** | **bool** |  | [optional] 

## Example

```python
from dc_rest.models.message_create_request import MessageCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MessageCreateRequest from a JSON string
message_create_request_instance = MessageCreateRequest.from_json(json)
# print the JSON string representation of the object
print(MessageCreateRequest.to_json())

# convert the object into a dict
message_create_request_dict = message_create_request_instance.to_dict()
# create an instance of MessageCreateRequest from a dict
message_create_request_from_dict = MessageCreateRequest.from_dict(message_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


