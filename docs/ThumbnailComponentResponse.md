# ThumbnailComponentResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **int** |  | 
**id** | **int** |  | 
**media** | [**UnfurledMediaResponse**](UnfurledMediaResponse.md) |  | 
**description** | **str** |  | [optional] 
**spoiler** | **bool** |  | 

## Example

```python
from dc_rest.models.thumbnail_component_response import ThumbnailComponentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ThumbnailComponentResponse from a JSON string
thumbnail_component_response_instance = ThumbnailComponentResponse.from_json(json)
# print the JSON string representation of the object
print(ThumbnailComponentResponse.to_json())

# convert the object into a dict
thumbnail_component_response_dict = thumbnail_component_response_instance.to_dict()
# create an instance of ThumbnailComponentResponse from a dict
thumbnail_component_response_from_dict = ThumbnailComponentResponse.from_dict(thumbnail_component_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


