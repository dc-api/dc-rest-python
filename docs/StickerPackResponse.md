# StickerPackResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**sku_id** | **str** |  | 
**name** | **str** |  | 
**description** | **str** |  | [optional] 
**stickers** | [**List[StandardStickerResponse]**](StandardStickerResponse.md) |  | 
**cover_sticker_id** | **str** |  | [optional] 
**banner_asset_id** | **str** |  | [optional] 

## Example

```python
from dc_rest.models.sticker_pack_response import StickerPackResponse

# TODO update the JSON string below
json = "{}"
# create an instance of StickerPackResponse from a JSON string
sticker_pack_response_instance = StickerPackResponse.from_json(json)
# print the JSON string representation of the object
print(StickerPackResponse.to_json())

# convert the object into a dict
sticker_pack_response_dict = sticker_pack_response_instance.to_dict()
# create an instance of StickerPackResponse from a dict
sticker_pack_response_from_dict = StickerPackResponse.from_dict(sticker_pack_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


