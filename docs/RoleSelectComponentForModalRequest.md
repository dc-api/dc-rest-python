# RoleSelectComponentForModalRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **int** |  | 
**id** | **int** |  | [optional] 
**custom_id** | **str** |  | 
**placeholder** | **str** |  | [optional] 
**min_values** | **int** |  | [optional] 
**max_values** | **int** |  | [optional] 
**disabled** | **bool** |  | [optional] 
**required** | **bool** |  | [optional] 
**default_values** | [**List[RoleSelectDefaultValue]**](RoleSelectDefaultValue.md) |  | [optional] 

## Example

```python
from dc_rest.models.role_select_component_for_modal_request import RoleSelectComponentForModalRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RoleSelectComponentForModalRequest from a JSON string
role_select_component_for_modal_request_instance = RoleSelectComponentForModalRequest.from_json(json)
# print the JSON string representation of the object
print(RoleSelectComponentForModalRequest.to_json())

# convert the object into a dict
role_select_component_for_modal_request_dict = role_select_component_for_modal_request_instance.to_dict()
# create an instance of RoleSelectComponentForModalRequest from a dict
role_select_component_for_modal_request_from_dict = RoleSelectComponentForModalRequest.from_dict(role_select_component_for_modal_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


