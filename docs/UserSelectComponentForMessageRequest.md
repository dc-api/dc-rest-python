# UserSelectComponentForMessageRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **int** |  | 
**custom_id** | **str** |  | 
**placeholder** | **str** |  | [optional] 
**min_values** | **int** |  | [optional] 
**max_values** | **int** |  | [optional] 
**disabled** | **bool** |  | [optional] 
**default_values** | [**List[UserSelectDefaultValue]**](UserSelectDefaultValue.md) |  | [optional] 

## Example

```python
from dc_rest.models.user_select_component_for_message_request import UserSelectComponentForMessageRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UserSelectComponentForMessageRequest from a JSON string
user_select_component_for_message_request_instance = UserSelectComponentForMessageRequest.from_json(json)
# print the JSON string representation of the object
print(UserSelectComponentForMessageRequest.to_json())

# convert the object into a dict
user_select_component_for_message_request_dict = user_select_component_for_message_request_instance.to_dict()
# create an instance of UserSelectComponentForMessageRequest from a dict
user_select_component_for_message_request_from_dict = UserSelectComponentForMessageRequest.from_dict(user_select_component_for_message_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


