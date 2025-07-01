# PruneGuildRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**days** | **int** |  | [optional] 
**compute_prune_count** | **bool** |  | [optional] 
**include_roles** | [**PruneGuildRequestIncludeRoles**](PruneGuildRequestIncludeRoles.md) |  | [optional] 

## Example

```python
from dc_rest.models.prune_guild_request import PruneGuildRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PruneGuildRequest from a JSON string
prune_guild_request_instance = PruneGuildRequest.from_json(json)
# print the JSON string representation of the object
print(PruneGuildRequest.to_json())

# convert the object into a dict
prune_guild_request_dict = prune_guild_request_instance.to_dict()
# create an instance of PruneGuildRequest from a dict
prune_guild_request_from_dict = PruneGuildRequest.from_dict(prune_guild_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


