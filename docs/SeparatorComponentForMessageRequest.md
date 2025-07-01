# SeparatorComponentForMessageRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **int** |  | 
**spacing** | **int** |  | [optional] 
**divider** | **bool** |  | [optional] 

## Example

```python
from dc_rest.models.separator_component_for_message_request import SeparatorComponentForMessageRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SeparatorComponentForMessageRequest from a JSON string
separator_component_for_message_request_instance = SeparatorComponentForMessageRequest.from_json(json)
# print the JSON string representation of the object
print(SeparatorComponentForMessageRequest.to_json())

# convert the object into a dict
separator_component_for_message_request_dict = separator_component_for_message_request_instance.to_dict()
# create an instance of SeparatorComponentForMessageRequest from a dict
separator_component_for_message_request_from_dict = SeparatorComponentForMessageRequest.from_dict(separator_component_for_message_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


