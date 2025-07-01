# MediaGalleryComponentResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **int** |  | 
**id** | **int** |  | 
**items** | [**List[MediaGalleryItemResponse]**](MediaGalleryItemResponse.md) |  | 

## Example

```python
from dc_rest.models.media_gallery_component_response import MediaGalleryComponentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MediaGalleryComponentResponse from a JSON string
media_gallery_component_response_instance = MediaGalleryComponentResponse.from_json(json)
# print the JSON string representation of the object
print(MediaGalleryComponentResponse.to_json())

# convert the object into a dict
media_gallery_component_response_dict = media_gallery_component_response_instance.to_dict()
# create an instance of MediaGalleryComponentResponse from a dict
media_gallery_component_response_from_dict = MediaGalleryComponentResponse.from_dict(media_gallery_component_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


