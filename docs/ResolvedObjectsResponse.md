# ResolvedObjectsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**users** | [**Dict[str, UserResponse]**](UserResponse.md) |  | 
**members** | [**Dict[str, GuildMemberResponse]**](GuildMemberResponse.md) |  | 
**channels** | [**Dict[str, GetChannel200Response]**](GetChannel200Response.md) |  | 
**roles** | [**Dict[str, GuildRoleResponse]**](GuildRoleResponse.md) |  | 

## Example

```python
from dc_rest.models.resolved_objects_response import ResolvedObjectsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ResolvedObjectsResponse from a JSON string
resolved_objects_response_instance = ResolvedObjectsResponse.from_json(json)
# print the JSON string representation of the object
print(ResolvedObjectsResponse.to_json())

# convert the object into a dict
resolved_objects_response_dict = resolved_objects_response_instance.to_dict()
# create an instance of ResolvedObjectsResponse from a dict
resolved_objects_response_from_dict = ResolvedObjectsResponse.from_dict(resolved_objects_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


