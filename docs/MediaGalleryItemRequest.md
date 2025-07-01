# MediaGalleryItemRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**spoiler** | **bool** |  | [optional] 
**media** | [**UnfurledMediaRequest**](UnfurledMediaRequest.md) |  | 

## Example

```python
from dc_rest.models.media_gallery_item_request import MediaGalleryItemRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MediaGalleryItemRequest from a JSON string
media_gallery_item_request_instance = MediaGalleryItemRequest.from_json(json)
# print the JSON string representation of the object
print(MediaGalleryItemRequest.to_json())

# convert the object into a dict
media_gallery_item_request_dict = media_gallery_item_request_instance.to_dict()
# create an instance of MediaGalleryItemRequest from a dict
media_gallery_item_request_from_dict = MediaGalleryItemRequest.from_dict(media_gallery_item_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


