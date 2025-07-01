# CommandPermissionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**type** | **int** |  | 
**permission** | **bool** |  | 

## Example

```python
from dc_rest.models.command_permission_response import CommandPermissionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CommandPermissionResponse from a JSON string
command_permission_response_instance = CommandPermissionResponse.from_json(json)
# print the JSON string representation of the object
print(CommandPermissionResponse.to_json())

# convert the object into a dict
command_permission_response_dict = command_permission_response_instance.to_dict()
# create an instance of CommandPermissionResponse from a dict
command_permission_response_from_dict = CommandPermissionResponse.from_dict(command_permission_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


