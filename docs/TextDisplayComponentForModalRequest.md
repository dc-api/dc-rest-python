# TextDisplayComponentForModalRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **int** |  | 
**id** | **int** |  | [optional] 
**content** | **str** |  | 

## Example

```python
from dc_rest.models.text_display_component_for_modal_request import TextDisplayComponentForModalRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TextDisplayComponentForModalRequest from a JSON string
text_display_component_for_modal_request_instance = TextDisplayComponentForModalRequest.from_json(json)
# print the JSON string representation of the object
print(TextDisplayComponentForModalRequest.to_json())

# convert the object into a dict
text_display_component_for_modal_request_dict = text_display_component_for_modal_request_instance.to_dict()
# create an instance of TextDisplayComponentForModalRequest from a dict
text_display_component_for_modal_request_from_dict = TextDisplayComponentForModalRequest.from_dict(text_display_component_for_modal_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


