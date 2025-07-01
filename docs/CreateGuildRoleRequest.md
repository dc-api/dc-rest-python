# CreateGuildRoleRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**permissions** | **int** |  | [optional] 
**color** | **int** |  | [optional] 
**hoist** | **bool** |  | [optional] 
**mentionable** | **bool** |  | [optional] 
**icon** | **str** |  | [optional] 
**unicode_emoji** | **str** |  | [optional] 

## Example

```python
from dc_rest.models.create_guild_role_request import CreateGuildRoleRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateGuildRoleRequest from a JSON string
create_guild_role_request_instance = CreateGuildRoleRequest.from_json(json)
# print the JSON string representation of the object
print(CreateGuildRoleRequest.to_json())

# convert the object into a dict
create_guild_role_request_dict = create_guild_role_request_instance.to_dict()
# create an instance of CreateGuildRoleRequest from a dict
create_guild_role_request_from_dict = CreateGuildRoleRequest.from_dict(create_guild_role_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


