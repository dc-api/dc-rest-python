# ListGuildIntegrations200ResponseInner


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
**user** | [**UserResponse**](UserResponse.md) |  | 
**revoked** | **bool** |  | [optional] 
**expire_behavior** | **int** |  | [optional] 
**expire_grace_period** | **int** |  | [optional] 
**subscriber_count** | **int** |  | [optional] 
**synced_at** | **datetime** |  | [optional] 
**role_id** | **str** |  | [optional] 
**syncing** | **bool** |  | [optional] 
**enable_emoticons** | **bool** |  | [optional] 

## Example

```python
from dc_rest.models.list_guild_integrations200_response_inner import ListGuildIntegrations200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of ListGuildIntegrations200ResponseInner from a JSON string
list_guild_integrations200_response_inner_instance = ListGuildIntegrations200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(ListGuildIntegrations200ResponseInner.to_json())

# convert the object into a dict
list_guild_integrations200_response_inner_dict = list_guild_integrations200_response_inner_instance.to_dict()
# create an instance of ListGuildIntegrations200ResponseInner from a dict
list_guild_integrations200_response_inner_from_dict = ListGuildIntegrations200ResponseInner.from_dict(list_guild_integrations200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


