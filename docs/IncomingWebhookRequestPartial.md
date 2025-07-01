# IncomingWebhookRequestPartial


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | **str** |  | [optional] 
**embeds** | [**List[RichEmbed]**](RichEmbed.md) |  | [optional] 
**allowed_mentions** | [**MessageAllowedMentionsRequest**](MessageAllowedMentionsRequest.md) |  | [optional] 
**components** | [**List[BaseCreateMessageCreateRequestComponentsInner]**](BaseCreateMessageCreateRequestComponentsInner.md) |  | [optional] 
**attachments** | [**List[MessageAttachmentRequest]**](MessageAttachmentRequest.md) |  | [optional] 
**poll** | [**PollCreateRequest**](PollCreateRequest.md) |  | [optional] 
**tts** | **bool** |  | [optional] 
**flags** | **int** |  | [optional] 
**username** | **str** |  | [optional] 
**avatar_url** | **str** |  | [optional] 
**thread_name** | **str** |  | [optional] 
**applied_tags** | **List[str]** |  | [optional] 

## Example

```python
from dc_rest.models.incoming_webhook_request_partial import IncomingWebhookRequestPartial

# TODO update the JSON string below
json = "{}"
# create an instance of IncomingWebhookRequestPartial from a JSON string
incoming_webhook_request_partial_instance = IncomingWebhookRequestPartial.from_json(json)
# print the JSON string representation of the object
print(IncomingWebhookRequestPartial.to_json())

# convert the object into a dict
incoming_webhook_request_partial_dict = incoming_webhook_request_partial_instance.to_dict()
# create an instance of IncomingWebhookRequestPartial from a dict
incoming_webhook_request_partial_from_dict = IncomingWebhookRequestPartial.from_dict(incoming_webhook_request_partial_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


