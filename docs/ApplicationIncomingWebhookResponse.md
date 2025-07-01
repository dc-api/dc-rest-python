# ApplicationIncomingWebhookResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application_id** | **str** |  | [optional] 
**avatar** | **str** |  | [optional] 
**channel_id** | **str** |  | [optional] 
**guild_id** | **str** |  | [optional] 
**id** | **str** |  | 
**name** | **str** |  | 
**type** | **int** |  | 
**user** | [**UserResponse**](UserResponse.md) |  | [optional] 

## Example

```python
from dc_rest.models.application_incoming_webhook_response import ApplicationIncomingWebhookResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationIncomingWebhookResponse from a JSON string
application_incoming_webhook_response_instance = ApplicationIncomingWebhookResponse.from_json(json)
# print the JSON string representation of the object
print(ApplicationIncomingWebhookResponse.to_json())

# convert the object into a dict
application_incoming_webhook_response_dict = application_incoming_webhook_response_instance.to_dict()
# create an instance of ApplicationIncomingWebhookResponse from a dict
application_incoming_webhook_response_from_dict = ApplicationIncomingWebhookResponse.from_dict(application_incoming_webhook_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


