# PartialDiscordIntegrationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**type** | **str** |  | 
**name** | **str** |  | [optional] 
**account** | [**AccountResponse**](AccountResponse.md) |  | [optional] 
**application_id** | **str** |  | 

## Example

```python
from dc_rest.models.partial_discord_integration_response import PartialDiscordIntegrationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PartialDiscordIntegrationResponse from a JSON string
partial_discord_integration_response_instance = PartialDiscordIntegrationResponse.from_json(json)
# print the JSON string representation of the object
print(PartialDiscordIntegrationResponse.to_json())

# convert the object into a dict
partial_discord_integration_response_dict = partial_discord_integration_response_instance.to_dict()
# create an instance of PartialDiscordIntegrationResponse from a dict
partial_discord_integration_response_from_dict = PartialDiscordIntegrationResponse.from_dict(partial_discord_integration_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


