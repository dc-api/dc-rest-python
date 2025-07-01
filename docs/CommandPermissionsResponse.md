# CommandPermissionsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**application_id** | **str** |  | 
**guild_id** | **str** |  | 
**permissions** | [**List[CommandPermissionResponse]**](CommandPermissionResponse.md) |  | 

## Example

```python
from dc_rest.models.command_permissions_response import CommandPermissionsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CommandPermissionsResponse from a JSON string
command_permissions_response_instance = CommandPermissionsResponse.from_json(json)
# print the JSON string representation of the object
print(CommandPermissionsResponse.to_json())

# convert the object into a dict
command_permissions_response_dict = command_permissions_response_instance.to_dict()
# create an instance of CommandPermissionsResponse from a dict
command_permissions_response_from_dict = CommandPermissionsResponse.from_dict(command_permissions_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


