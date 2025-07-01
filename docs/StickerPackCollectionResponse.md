# StickerPackCollectionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sticker_packs** | [**List[StickerPackResponse]**](StickerPackResponse.md) |  | 

## Example

```python
from dc_rest.models.sticker_pack_collection_response import StickerPackCollectionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of StickerPackCollectionResponse from a JSON string
sticker_pack_collection_response_instance = StickerPackCollectionResponse.from_json(json)
# print the JSON string representation of the object
print(StickerPackCollectionResponse.to_json())

# convert the object into a dict
sticker_pack_collection_response_dict = sticker_pack_collection_response_instance.to_dict()
# create an instance of StickerPackCollectionResponse from a dict
sticker_pack_collection_response_from_dict = StickerPackCollectionResponse.from_dict(sticker_pack_collection_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


