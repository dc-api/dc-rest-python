# ApplicationCommandPermission


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**type** | **int** |  | 
**permission** | **bool** |  | 

## Example

```python
from dc_rest.models.application_command_permission import ApplicationCommandPermission

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationCommandPermission from a JSON string
application_command_permission_instance = ApplicationCommandPermission.from_json(json)
# print the JSON string representation of the object
print(ApplicationCommandPermission.to_json())

# convert the object into a dict
application_command_permission_dict = application_command_permission_instance.to_dict()
# create an instance of ApplicationCommandPermission from a dict
application_command_permission_from_dict = ApplicationCommandPermission.from_dict(application_command_permission_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


