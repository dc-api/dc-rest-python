# MessageEditRequestPartial


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | **str** |  | [optional] 
**embeds** | [**List[RichEmbed]**](RichEmbed.md) |  | [optional] 
**flags** | **int** |  | [optional] 
**allowed_mentions** | [**MessageAllowedMentionsRequest**](MessageAllowedMentionsRequest.md) |  | [optional] 
**sticker_ids** | **List[str]** |  | [optional] 
**components** | [**List[BaseCreateMessageCreateRequestComponentsInner]**](BaseCreateMessageCreateRequestComponentsInner.md) |  | [optional] 
**attachments** | [**List[MessageAttachmentRequest]**](MessageAttachmentRequest.md) |  | [optional] 

## Example

```python
from dc_rest.models.message_edit_request_partial import MessageEditRequestPartial

# TODO update the JSON string below
json = "{}"
# create an instance of MessageEditRequestPartial from a JSON string
message_edit_request_partial_instance = MessageEditRequestPartial.from_json(json)
# print the JSON string representation of the object
print(MessageEditRequestPartial.to_json())

# convert the object into a dict
message_edit_request_partial_dict = message_edit_request_partial_instance.to_dict()
# create an instance of MessageEditRequestPartial from a dict
message_edit_request_partial_from_dict = MessageEditRequestPartial.from_dict(message_edit_request_partial_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


