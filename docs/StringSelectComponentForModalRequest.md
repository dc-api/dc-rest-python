# StringSelectComponentForModalRequest


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
**options** | [**List[StringSelectOptionForRequest]**](StringSelectOptionForRequest.md) |  | 

## Example

```python
from dc_rest.models.string_select_component_for_modal_request import StringSelectComponentForModalRequest

# TODO update the JSON string below
json = "{}"
# create an instance of StringSelectComponentForModalRequest from a JSON string
string_select_component_for_modal_request_instance = StringSelectComponentForModalRequest.from_json(json)
# print the JSON string representation of the object
print(StringSelectComponentForModalRequest.to_json())

# convert the object into a dict
string_select_component_for_modal_request_dict = string_select_component_for_modal_request_instance.to_dict()
# create an instance of StringSelectComponentForModalRequest from a dict
string_select_component_for_modal_request_from_dict = StringSelectComponentForModalRequest.from_dict(string_select_component_for_modal_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


