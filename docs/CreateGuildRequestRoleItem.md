# CreateGuildRequestRoleItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | [optional] 
**permissions** | **int** |  | [optional] 
**color** | **int** |  | [optional] 
**hoist** | **bool** |  | [optional] 
**mentionable** | **bool** |  | [optional] 
**unicode_emoji** | **str** |  | [optional] 

## Example

```python
from dc_rest.models.create_guild_request_role_item import CreateGuildRequestRoleItem

# TODO update the JSON string below
json = "{}"
# create an instance of CreateGuildRequestRoleItem from a JSON string
create_guild_request_role_item_instance = CreateGuildRequestRoleItem.from_json(json)
# print the JSON string representation of the object
print(CreateGuildRequestRoleItem.to_json())

# convert the object into a dict
create_guild_request_role_item_dict = create_guild_request_role_item_instance.to_dict()
# create an instance of CreateGuildRequestRoleItem from a dict
create_guild_request_role_item_from_dict = CreateGuildRequestRoleItem.from_dict(create_guild_request_role_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


