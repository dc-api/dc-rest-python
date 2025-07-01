# GuildIncomingWebhookResponse


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
**token** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from dc_rest.models.guild_incoming_webhook_response import GuildIncomingWebhookResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GuildIncomingWebhookResponse from a JSON string
guild_incoming_webhook_response_instance = GuildIncomingWebhookResponse.from_json(json)
# print the JSON string representation of the object
print(GuildIncomingWebhookResponse.to_json())

# convert the object into a dict
guild_incoming_webhook_response_dict = guild_incoming_webhook_response_instance.to_dict()
# create an instance of GuildIncomingWebhookResponse from a dict
guild_incoming_webhook_response_from_dict = GuildIncomingWebhookResponse.from_dict(guild_incoming_webhook_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


