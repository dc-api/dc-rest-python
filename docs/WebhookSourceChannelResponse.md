# WebhookSourceChannelResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 

## Example

```python
from dc_rest.models.webhook_source_channel_response import WebhookSourceChannelResponse

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookSourceChannelResponse from a JSON string
webhook_source_channel_response_instance = WebhookSourceChannelResponse.from_json(json)
# print the JSON string representation of the object
print(WebhookSourceChannelResponse.to_json())

# convert the object into a dict
webhook_source_channel_response_dict = webhook_source_channel_response_instance.to_dict()
# create an instance of WebhookSourceChannelResponse from a dict
webhook_source_channel_response_from_dict = WebhookSourceChannelResponse.from_dict(webhook_source_channel_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


