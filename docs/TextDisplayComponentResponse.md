# TextDisplayComponentResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **int** |  | 
**id** | **int** |  | 
**content** | **str** |  | 

## Example

```python
from dc_rest.models.text_display_component_response import TextDisplayComponentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TextDisplayComponentResponse from a JSON string
text_display_component_response_instance = TextDisplayComponentResponse.from_json(json)
# print the JSON string representation of the object
print(TextDisplayComponentResponse.to_json())

# convert the object into a dict
text_display_component_response_dict = text_display_component_response_instance.to_dict()
# create an instance of TextDisplayComponentResponse from a dict
text_display_component_response_from_dict = TextDisplayComponentResponse.from_dict(text_display_component_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


