# ActionRowComponentForMessageRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **int** |  | 
**components** | [**List[ActionRowComponentForMessageRequestComponentsInner]**](ActionRowComponentForMessageRequestComponentsInner.md) |  | 

## Example

```python
from dc_rest.models.action_row_component_for_message_request import ActionRowComponentForMessageRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ActionRowComponentForMessageRequest from a JSON string
action_row_component_for_message_request_instance = ActionRowComponentForMessageRequest.from_json(json)
# print the JSON string representation of the object
print(ActionRowComponentForMessageRequest.to_json())

# convert the object into a dict
action_row_component_for_message_request_dict = action_row_component_for_message_request_instance.to_dict()
# create an instance of ActionRowComponentForMessageRequest from a dict
action_row_component_for_message_request_from_dict = ActionRowComponentForMessageRequest.from_dict(action_row_component_for_message_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


