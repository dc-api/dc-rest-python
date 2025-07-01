# BaseCreateMessageCreateRequest


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

## Example

```python
from dc_rest.models.base_create_message_create_request import BaseCreateMessageCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BaseCreateMessageCreateRequest from a JSON string
base_create_message_create_request_instance = BaseCreateMessageCreateRequest.from_json(json)
# print the JSON string representation of the object
print(BaseCreateMessageCreateRequest.to_json())

# convert the object into a dict
base_create_message_create_request_dict = base_create_message_create_request_instance.to_dict()
# create an instance of BaseCreateMessageCreateRequest from a dict
base_create_message_create_request_from_dict = BaseCreateMessageCreateRequest.from_dict(base_create_message_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


