# MessageStickerItemResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**format_type** | **int** |  | 

## Example

```python
from dc_rest.models.message_sticker_item_response import MessageStickerItemResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MessageStickerItemResponse from a JSON string
message_sticker_item_response_instance = MessageStickerItemResponse.from_json(json)
# print the JSON string representation of the object
print(MessageStickerItemResponse.to_json())

# convert the object into a dict
message_sticker_item_response_dict = message_sticker_item_response_instance.to_dict()
# create an instance of MessageStickerItemResponse from a dict
message_sticker_item_response_from_dict = MessageStickerItemResponse.from_dict(message_sticker_item_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


