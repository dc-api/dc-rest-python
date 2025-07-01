# TextDisplayComponentForMessageRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **int** |  | 
**content** | **str** |  | 

## Example

```python
from dc_rest.models.text_display_component_for_message_request import TextDisplayComponentForMessageRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TextDisplayComponentForMessageRequest from a JSON string
text_display_component_for_message_request_instance = TextDisplayComponentForMessageRequest.from_json(json)
# print the JSON string representation of the object
print(TextDisplayComponentForMessageRequest.to_json())

# convert the object into a dict
text_display_component_for_message_request_dict = text_display_component_for_message_request_instance.to_dict()
# create an instance of TextDisplayComponentForMessageRequest from a dict
text_display_component_for_message_request_from_dict = TextDisplayComponentForMessageRequest.from_dict(text_display_component_for_message_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


