# StandardStickerResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**tags** | **str** |  | 
**type** | **int** |  | 
**format_type** | **int** |  | [optional] 
**description** | **str** |  | [optional] 
**pack_id** | **str** |  | 
**sort_value** | **int** |  | 

## Example

```python
from dc_rest.models.standard_sticker_response import StandardStickerResponse

# TODO update the JSON string below
json = "{}"
# create an instance of StandardStickerResponse from a JSON string
standard_sticker_response_instance = StandardStickerResponse.from_json(json)
# print the JSON string representation of the object
print(StandardStickerResponse.to_json())

# convert the object into a dict
standard_sticker_response_dict = standard_sticker_response_instance.to_dict()
# create an instance of StandardStickerResponse from a dict
standard_sticker_response_from_dict = StandardStickerResponse.from_dict(standard_sticker_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


