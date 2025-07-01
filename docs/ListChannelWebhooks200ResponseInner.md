# ListChannelWebhooks200ResponseInner


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
**source_guild** | [**WebhookSourceGuildResponse**](WebhookSourceGuildResponse.md) |  | [optional] 
**source_channel** | [**WebhookSourceChannelResponse**](WebhookSourceChannelResponse.md) |  | [optional] 
**token** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from dc_rest.models.list_channel_webhooks200_response_inner import ListChannelWebhooks200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of ListChannelWebhooks200ResponseInner from a JSON string
list_channel_webhooks200_response_inner_instance = ListChannelWebhooks200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(ListChannelWebhooks200ResponseInner.to_json())

# convert the object into a dict
list_channel_webhooks200_response_inner_dict = list_channel_webhooks200_response_inner_instance.to_dict()
# create an instance of ListChannelWebhooks200ResponseInner from a dict
list_channel_webhooks200_response_inner_from_dict = ListChannelWebhooks200ResponseInner.from_dict(list_channel_webhooks200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


