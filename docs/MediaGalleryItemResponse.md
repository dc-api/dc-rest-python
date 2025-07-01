# MediaGalleryItemResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**media** | [**UnfurledMediaResponse**](UnfurledMediaResponse.md) |  | 
**description** | **str** |  | [optional] 
**spoiler** | **bool** |  | 

## Example

```python
from dc_rest.models.media_gallery_item_response import MediaGalleryItemResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MediaGalleryItemResponse from a JSON string
media_gallery_item_response_instance = MediaGalleryItemResponse.from_json(json)
# print the JSON string representation of the object
print(MediaGalleryItemResponse.to_json())

# convert the object into a dict
media_gallery_item_response_dict = media_gallery_item_response_instance.to_dict()
# create an instance of MediaGalleryItemResponse from a dict
media_gallery_item_response_from_dict = MediaGalleryItemResponse.from_dict(media_gallery_item_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


