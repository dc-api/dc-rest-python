# IncomingWebhookUpdateRequestPartial


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | **str** |  | [optional] 
**embeds** | [**List[RichEmbed]**](RichEmbed.md) |  | [optional] 
**allowed_mentions** | [**MessageAllowedMentionsRequest**](MessageAllowedMentionsRequest.md) |  | [optional] 
**components** | [**List[BaseCreateMessageCreateRequestComponentsInner]**](BaseCreateMessageCreateRequestComponentsInner.md) |  | [optional] 
**attachments** | [**List[MessageAttachmentRequest]**](MessageAttachmentRequest.md) |  | [optional] 
**poll** | [**PollCreateRequest**](PollCreateRequest.md) |  | [optional] 
**flags** | **int** |  | [optional] 

## Example

```python
from dc_rest.models.incoming_webhook_update_request_partial import IncomingWebhookUpdateRequestPartial

# TODO update the JSON string below
json = "{}"
# create an instance of IncomingWebhookUpdateRequestPartial from a JSON string
incoming_webhook_update_request_partial_instance = IncomingWebhookUpdateRequestPartial.from_json(json)
# print the JSON string representation of the object
print(IncomingWebhookUpdateRequestPartial.to_json())

# convert the object into a dict
incoming_webhook_update_request_partial_dict = incoming_webhook_update_request_partial_instance.to_dict()
# create an instance of IncomingWebhookUpdateRequestPartial from a dict
incoming_webhook_update_request_partial_from_dict = IncomingWebhookUpdateRequestPartial.from_dict(incoming_webhook_update_request_partial_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


