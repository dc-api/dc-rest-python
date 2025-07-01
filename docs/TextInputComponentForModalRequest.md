# TextInputComponentForModalRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **int** |  | 
**custom_id** | **str** |  | 
**style** | **int** |  | 
**label** | **str** |  | 
**value** | **str** |  | [optional] 
**placeholder** | **str** |  | [optional] 
**required** | **bool** |  | [optional] 
**min_length** | **int** |  | [optional] 
**max_length** | **int** |  | [optional] 

## Example

```python
from dc_rest.models.text_input_component_for_modal_request import TextInputComponentForModalRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TextInputComponentForModalRequest from a JSON string
text_input_component_for_modal_request_instance = TextInputComponentForModalRequest.from_json(json)
# print the JSON string representation of the object
print(TextInputComponentForModalRequest.to_json())

# convert the object into a dict
text_input_component_for_modal_request_dict = text_input_component_for_modal_request_instance.to_dict()
# create an instance of TextInputComponentForModalRequest from a dict
text_input_component_for_modal_request_from_dict = TextInputComponentForModalRequest.from_dict(text_input_component_for_modal_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


