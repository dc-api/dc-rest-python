# TextInputComponentResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **int** |  | 
**id** | **int** |  | 
**custom_id** | **str** |  | 
**style** | **int** |  | 
**label** | **str** |  | [optional] 
**value** | **str** |  | [optional] 
**placeholder** | **str** |  | [optional] 
**required** | **bool** |  | [optional] 
**min_length** | **int** |  | [optional] 
**max_length** | **int** |  | [optional] 

## Example

```python
from dc_rest.models.text_input_component_response import TextInputComponentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TextInputComponentResponse from a JSON string
text_input_component_response_instance = TextInputComponentResponse.from_json(json)
# print the JSON string representation of the object
print(TextInputComponentResponse.to_json())

# convert the object into a dict
text_input_component_response_dict = text_input_component_response_instance.to_dict()
# create an instance of TextInputComponentResponse from a dict
text_input_component_response_from_dict = TextInputComponentResponse.from_dict(text_input_component_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


