# DiscordIntegrationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**name** | **str** |  | [optional] 
**account** | [**AccountResponse**](AccountResponse.md) |  | [optional] 
**enabled** | **bool** |  | [optional] 
**id** | **str** |  | 
**application** | [**IntegrationApplicationResponse**](IntegrationApplicationResponse.md) |  | 
**scopes** | **List[str]** |  | 
**user** | [**UserResponse**](UserResponse.md) |  | [optional] 

## Example

```python
from dc_rest.models.discord_integration_response import DiscordIntegrationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DiscordIntegrationResponse from a JSON string
discord_integration_response_instance = DiscordIntegrationResponse.from_json(json)
# print the JSON string representation of the object
print(DiscordIntegrationResponse.to_json())

# convert the object into a dict
discord_integration_response_dict = discord_integration_response_instance.to_dict()
# create an instance of DiscordIntegrationResponse from a dict
discord_integration_response_from_dict = DiscordIntegrationResponse.from_dict(discord_integration_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


