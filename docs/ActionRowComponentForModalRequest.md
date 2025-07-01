# ActionRowComponentForModalRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **int** |  | 
**components** | [**List[TextInputComponentForModalRequest]**](TextInputComponentForModalRequest.md) |  | 

## Example

```python
from dc_rest.models.action_row_component_for_modal_request import ActionRowComponentForModalRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ActionRowComponentForModalRequest from a JSON string
action_row_component_for_modal_request_instance = ActionRowComponentForModalRequest.from_json(json)
# print the JSON string representation of the object
print(ActionRowComponentForModalRequest.to_json())

# convert the object into a dict
action_row_component_for_modal_request_dict = action_row_component_for_modal_request_instance.to_dict()
# create an instance of ActionRowComponentForModalRequest from a dict
action_row_component_for_modal_request_from_dict = ActionRowComponentForModalRequest.from_dict(action_row_component_for_modal_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


