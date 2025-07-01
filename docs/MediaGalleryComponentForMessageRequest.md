# MediaGalleryComponentForMessageRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **int** |  | 
**items** | [**List[MediaGalleryItemRequest]**](MediaGalleryItemRequest.md) |  | 

## Example

```python
from dc_rest.models.media_gallery_component_for_message_request import MediaGalleryComponentForMessageRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MediaGalleryComponentForMessageRequest from a JSON string
media_gallery_component_for_message_request_instance = MediaGalleryComponentForMessageRequest.from_json(json)
# print the JSON string representation of the object
print(MediaGalleryComponentForMessageRequest.to_json())

# convert the object into a dict
media_gallery_component_for_message_request_dict = media_gallery_component_for_message_request_instance.to_dict()
# create an instance of MediaGalleryComponentForMessageRequest from a dict
media_gallery_component_for_message_request_from_dict = MediaGalleryComponentForMessageRequest.from_dict(media_gallery_component_for_message_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


