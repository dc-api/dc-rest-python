# StringSelectComponentResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **int** |  | 
**id** | **int** |  | 
**custom_id** | **str** |  | 
**placeholder** | **str** |  | [optional] 
**min_values** | **int** |  | [optional] 
**max_values** | **int** |  | [optional] 
**disabled** | **bool** |  | [optional] 
**options** | [**List[StringSelectOptionResponse]**](StringSelectOptionResponse.md) |  | 

## Example

```python
from dc_rest.models.string_select_component_response import StringSelectComponentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of StringSelectComponentResponse from a JSON string
string_select_component_response_instance = StringSelectComponentResponse.from_json(json)
# print the JSON string representation of the object
print(StringSelectComponentResponse.to_json())

# convert the object into a dict
string_select_component_response_dict = string_select_component_response_instance.to_dict()
# create an instance of StringSelectComponentResponse from a dict
string_select_component_response_from_dict = StringSelectComponentResponse.from_dict(string_select_component_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


