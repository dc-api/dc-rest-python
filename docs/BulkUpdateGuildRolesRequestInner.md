# BulkUpdateGuildRolesRequestInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**position** | **int** |  | [optional] 

## Example

```python
from dc_rest.models.bulk_update_guild_roles_request_inner import BulkUpdateGuildRolesRequestInner

# TODO update the JSON string below
json = "{}"
# create an instance of BulkUpdateGuildRolesRequestInner from a JSON string
bulk_update_guild_roles_request_inner_instance = BulkUpdateGuildRolesRequestInner.from_json(json)
# print the JSON string representation of the object
print(BulkUpdateGuildRolesRequestInner.to_json())

# convert the object into a dict
bulk_update_guild_roles_request_inner_dict = bulk_update_guild_roles_request_inner_instance.to_dict()
# create an instance of BulkUpdateGuildRolesRequestInner from a dict
bulk_update_guild_roles_request_inner_from_dict = BulkUpdateGuildRolesRequestInner.from_dict(bulk_update_guild_roles_request_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


