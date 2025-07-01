# GuildSubscriptionIntegrationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**name** | **str** |  | [optional] 
**account** | [**AccountResponse**](AccountResponse.md) |  | [optional] 
**enabled** | **bool** |  | [optional] 
**id** | **str** |  | 

## Example

```python
from dc_rest.models.guild_subscription_integration_response import GuildSubscriptionIntegrationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GuildSubscriptionIntegrationResponse from a JSON string
guild_subscription_integration_response_instance = GuildSubscriptionIntegrationResponse.from_json(json)
# print the JSON string representation of the object
print(GuildSubscriptionIntegrationResponse.to_json())

# convert the object into a dict
guild_subscription_integration_response_dict = guild_subscription_integration_response_instance.to_dict()
# create an instance of GuildSubscriptionIntegrationResponse from a dict
guild_subscription_integration_response_from_dict = GuildSubscriptionIntegrationResponse.from_dict(guild_subscription_integration_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


