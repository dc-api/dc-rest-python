# UpdateGuildStickerRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**tags** | **str** |  | [optional] 
**description** | **str** |  | [optional] 

## Example

```python
from dc_rest.models.update_guild_sticker_request import UpdateGuildStickerRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateGuildStickerRequest from a JSON string
update_guild_sticker_request_instance = UpdateGuildStickerRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateGuildStickerRequest.to_json())

# convert the object into a dict
update_guild_sticker_request_dict = update_guild_sticker_request_instance.to_dict()
# create an instance of UpdateGuildStickerRequest from a dict
update_guild_sticker_request_from_dict = UpdateGuildStickerRequest.from_dict(update_guild_sticker_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


