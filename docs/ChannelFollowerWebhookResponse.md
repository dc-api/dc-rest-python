# ChannelFollowerWebhookResponse


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

## Example

```python
from dc_rest.models.channel_follower_webhook_response import ChannelFollowerWebhookResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ChannelFollowerWebhookResponse from a JSON string
channel_follower_webhook_response_instance = ChannelFollowerWebhookResponse.from_json(json)
# print the JSON string representation of the object
print(ChannelFollowerWebhookResponse.to_json())

# convert the object into a dict
channel_follower_webhook_response_dict = channel_follower_webhook_response_instance.to_dict()
# create an instance of ChannelFollowerWebhookResponse from a dict
channel_follower_webhook_response_from_dict = ChannelFollowerWebhookResponse.from_dict(channel_follower_webhook_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


