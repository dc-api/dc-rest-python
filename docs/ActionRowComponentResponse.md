# ActionRowComponentResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **int** |  | 
**id** | **int** |  | 
**components** | [**List[ActionRowComponentResponseComponentsInner]**](ActionRowComponentResponseComponentsInner.md) |  | [optional] 

## Example

```python
from dc_rest.models.action_row_component_response import ActionRowComponentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ActionRowComponentResponse from a JSON string
action_row_component_response_instance = ActionRowComponentResponse.from_json(json)
# print the JSON string representation of the object
print(ActionRowComponentResponse.to_json())

# convert the object into a dict
action_row_component_response_dict = action_row_component_response_instance.to_dict()
# create an instance of ActionRowComponentResponse from a dict
action_row_component_response_from_dict = ActionRowComponentResponse.from_dict(action_row_component_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


