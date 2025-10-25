# UserSelectComponentForModalRequest


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
**default_values** | [**List[UserSelectDefaultValue]**](UserSelectDefaultValue.md) |  | [optional] 

## Example

```python
from dc_rest.models.user_select_component_for_modal_request import UserSelectComponentForModalRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UserSelectComponentForModalRequest from a JSON string
user_select_component_for_modal_request_instance = UserSelectComponentForModalRequest.from_json(json)
# print the JSON string representation of the object
print(UserSelectComponentForModalRequest.to_json())

# convert the object into a dict
user_select_component_for_modal_request_dict = user_select_component_for_modal_request_instance.to_dict()
# create an instance of UserSelectComponentForModalRequest from a dict
user_select_component_for_modal_request_from_dict = UserSelectComponentForModalRequest.from_dict(user_select_component_for_modal_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


