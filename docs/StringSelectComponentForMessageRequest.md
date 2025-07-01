# StringSelectComponentForMessageRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **int** |  | 
**custom_id** | **str** |  | 
**placeholder** | **str** |  | [optional] 
**min_values** | **int** |  | [optional] 
**max_values** | **int** |  | [optional] 
**disabled** | **bool** |  | [optional] 
**options** | [**List[StringSelectOptionForMessageRequest]**](StringSelectOptionForMessageRequest.md) |  | 

## Example

```python
from dc_rest.models.string_select_component_for_message_request import StringSelectComponentForMessageRequest

# TODO update the JSON string below
json = "{}"
# create an instance of StringSelectComponentForMessageRequest from a JSON string
string_select_component_for_message_request_instance = StringSelectComponentForMessageRequest.from_json(json)
# print the JSON string representation of the object
print(StringSelectComponentForMessageRequest.to_json())

# convert the object into a dict
string_select_component_for_message_request_dict = string_select_component_for_message_request_instance.to_dict()
# create an instance of StringSelectComponentForMessageRequest from a dict
string_select_component_for_message_request_from_dict = StringSelectComponentForMessageRequest.from_dict(string_select_component_for_message_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


