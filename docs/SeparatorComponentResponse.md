# SeparatorComponentResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **int** |  | 
**id** | **int** |  | 
**spacing** | **int** |  | 
**divider** | **bool** |  | 

## Example

```python
from dc_rest.models.separator_component_response import SeparatorComponentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SeparatorComponentResponse from a JSON string
separator_component_response_instance = SeparatorComponentResponse.from_json(json)
# print the JSON string representation of the object
print(SeparatorComponentResponse.to_json())

# convert the object into a dict
separator_component_response_dict = separator_component_response_instance.to_dict()
# create an instance of SeparatorComponentResponse from a dict
separator_component_response_from_dict = SeparatorComponentResponse.from_dict(separator_component_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


