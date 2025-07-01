# ConnectedAccountGuildResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**icon** | **str** |  | [optional] 
**name** | **str** |  | 

## Example

```python
from dc_rest.models.connected_account_guild_response import ConnectedAccountGuildResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectedAccountGuildResponse from a JSON string
connected_account_guild_response_instance = ConnectedAccountGuildResponse.from_json(json)
# print the JSON string representation of the object
print(ConnectedAccountGuildResponse.to_json())

# convert the object into a dict
connected_account_guild_response_dict = connected_account_guild_response_instance.to_dict()
# create an instance of ConnectedAccountGuildResponse from a dict
connected_account_guild_response_from_dict = ConnectedAccountGuildResponse.from_dict(connected_account_guild_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


