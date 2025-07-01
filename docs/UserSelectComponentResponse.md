# UserSelectComponentResponse


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
**default_values** | [**List[UserSelectDefaultValueResponse]**](UserSelectDefaultValueResponse.md) |  | [optional] 

## Example

```python
from dc_rest.models.user_select_component_response import UserSelectComponentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UserSelectComponentResponse from a JSON string
user_select_component_response_instance = UserSelectComponentResponse.from_json(json)
# print the JSON string representation of the object
print(UserSelectComponentResponse.to_json())

# convert the object into a dict
user_select_component_response_dict = user_select_component_response_instance.to_dict()
# create an instance of UserSelectComponentResponse from a dict
user_select_component_response_from_dict = UserSelectComponentResponse.from_dict(user_select_component_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


