# ThumbnailComponentForMessageRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **int** |  | 
**description** | **str** |  | [optional] 
**spoiler** | **bool** |  | [optional] 
**media** | [**UnfurledMediaRequest**](UnfurledMediaRequest.md) |  | 

## Example

```python
from dc_rest.models.thumbnail_component_for_message_request import ThumbnailComponentForMessageRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ThumbnailComponentForMessageRequest from a JSON string
thumbnail_component_for_message_request_instance = ThumbnailComponentForMessageRequest.from_json(json)
# print the JSON string representation of the object
print(ThumbnailComponentForMessageRequest.to_json())

# convert the object into a dict
thumbnail_component_for_message_request_dict = thumbnail_component_for_message_request_instance.to_dict()
# create an instance of ThumbnailComponentForMessageRequest from a dict
thumbnail_component_for_message_request_from_dict = ThumbnailComponentForMessageRequest.from_dict(thumbnail_component_for_message_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


