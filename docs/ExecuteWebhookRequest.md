# ExecuteWebhookRequest


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
from dc_rest.models.execute_webhook_request import ExecuteWebhookRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ExecuteWebhookRequest from a JSON string
execute_webhook_request_instance = ExecuteWebhookRequest.from_json(json)
# print the JSON string representation of the object
print(ExecuteWebhookRequest.to_json())

# convert the object into a dict
execute_webhook_request_dict = execute_webhook_request_instance.to_dict()
# create an instance of ExecuteWebhookRequest from a dict
execute_webhook_request_from_dict = ExecuteWebhookRequest.from_dict(execute_webhook_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


