# UserSelectDefaultValueResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**id** | **str** |  | 

## Example

```python
from dc_rest.models.user_select_default_value_response import UserSelectDefaultValueResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UserSelectDefaultValueResponse from a JSON string
user_select_default_value_response_instance = UserSelectDefaultValueResponse.from_json(json)
# print the JSON string representation of the object
print(UserSelectDefaultValueResponse.to_json())

# convert the object into a dict
user_select_default_value_response_dict = user_select_default_value_response_instance.to_dict()
# create an instance of UserSelectDefaultValueResponse from a dict
user_select_default_value_response_from_dict = UserSelectDefaultValueResponse.from_dict(user_select_default_value_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


