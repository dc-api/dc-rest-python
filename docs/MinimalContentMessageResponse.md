# MinimalContentMessageResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **int** |  | 
**content** | **str** |  | 
**mentions** | [**List[UserResponse]**](UserResponse.md) |  | 
**mention_roles** | **List[str]** |  | 
**attachments** | [**List[MessageAttachmentResponse]**](MessageAttachmentResponse.md) |  | 
**embeds** | [**List[MessageEmbedResponse]**](MessageEmbedResponse.md) |  | 
**timestamp** | **datetime** |  | 
**edited_timestamp** | **datetime** |  | [optional] 
**flags** | **int** |  | 
**components** | [**List[BasicMessageResponseComponentsInner]**](BasicMessageResponseComponentsInner.md) |  | 
**resolved** | [**ResolvedObjectsResponse**](ResolvedObjectsResponse.md) |  | [optional] 
**stickers** | [**List[GetSticker200Response]**](GetSticker200Response.md) |  | [optional] 
**sticker_items** | [**List[MessageStickerItemResponse]**](MessageStickerItemResponse.md) |  | [optional] 

## Example

```python
from dc_rest.models.minimal_content_message_response import MinimalContentMessageResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MinimalContentMessageResponse from a JSON string
minimal_content_message_response_instance = MinimalContentMessageResponse.from_json(json)
# print the JSON string representation of the object
print(MinimalContentMessageResponse.to_json())

# convert the object into a dict
minimal_content_message_response_dict = minimal_content_message_response_instance.to_dict()
# create an instance of MinimalContentMessageResponse from a dict
minimal_content_message_response_from_dict = MinimalContentMessageResponse.from_dict(minimal_content_message_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


