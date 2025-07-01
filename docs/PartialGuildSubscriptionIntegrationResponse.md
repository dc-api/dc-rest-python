# PartialGuildSubscriptionIntegrationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**type** | **str** |  | 
**name** | **str** |  | [optional] 
**account** | [**AccountResponse**](AccountResponse.md) |  | [optional] 

## Example

```python
from dc_rest.models.partial_guild_subscription_integration_response import PartialGuildSubscriptionIntegrationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PartialGuildSubscriptionIntegrationResponse from a JSON string
partial_guild_subscription_integration_response_instance = PartialGuildSubscriptionIntegrationResponse.from_json(json)
# print the JSON string representation of the object
print(PartialGuildSubscriptionIntegrationResponse.to_json())

# convert the object into a dict
partial_guild_subscription_integration_response_dict = partial_guild_subscription_integration_response_instance.to_dict()
# create an instance of PartialGuildSubscriptionIntegrationResponse from a dict
partial_guild_subscription_integration_response_from_dict = PartialGuildSubscriptionIntegrationResponse.from_dict(partial_guild_subscription_integration_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


