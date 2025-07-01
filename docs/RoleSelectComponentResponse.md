# RoleSelectComponentResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **int** |  | 
**id** | **int** |  | 
**custom_id** | **str** |  | 
**placeholder** | **str** |  | [optional] 
**min_values** | **int** |  | [optional] 
**max_values** | **int** |  | [optional] 
**disabled** | **bool** |  | [optional] 
**default_values** | [**List[RoleSelectDefaultValueResponse]**](RoleSelectDefaultValueResponse.md) |  | [optional] 

## Example

```python
from dc_rest.models.role_select_component_response import RoleSelectComponentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RoleSelectComponentResponse from a JSON string
role_select_component_response_instance = RoleSelectComponentResponse.from_json(json)
# print the JSON string representation of the object
print(RoleSelectComponentResponse.to_json())

# convert the object into a dict
role_select_component_response_dict = role_select_component_response_instance.to_dict()
# create an instance of RoleSelectComponentResponse from a dict
role_select_component_response_from_dict = RoleSelectComponentResponse.from_dict(role_select_component_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


