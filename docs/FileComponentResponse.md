# FileComponentResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **int** |  | 
**id** | **int** |  | 
**file** | [**UnfurledMediaResponse**](UnfurledMediaResponse.md) |  | 
**name** | **str** |  | [optional] 
**size** | **int** |  | [optional] 
**spoiler** | **bool** |  | 

## Example

```python
from dc_rest.models.file_component_response import FileComponentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FileComponentResponse from a JSON string
file_component_response_instance = FileComponentResponse.from_json(json)
# print the JSON string representation of the object
print(FileComponentResponse.to_json())

# convert the object into a dict
file_component_response_dict = file_component_response_instance.to_dict()
# create an instance of FileComponentResponse from a dict
file_component_response_from_dict = FileComponentResponse.from_dict(file_component_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


