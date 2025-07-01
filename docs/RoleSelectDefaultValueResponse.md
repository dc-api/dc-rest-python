# RoleSelectDefaultValueResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**id** | **str** |  | 

## Example

```python
from dc_rest.models.role_select_default_value_response import RoleSelectDefaultValueResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RoleSelectDefaultValueResponse from a JSON string
role_select_default_value_response_instance = RoleSelectDefaultValueResponse.from_json(json)
# print the JSON string representation of the object
print(RoleSelectDefaultValueResponse.to_json())

# convert the object into a dict
role_select_default_value_response_dict = role_select_default_value_response_instance.to_dict()
# create an instance of RoleSelectDefaultValueResponse from a dict
role_select_default_value_response_from_dict = RoleSelectDefaultValueResponse.from_dict(role_select_default_value_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


