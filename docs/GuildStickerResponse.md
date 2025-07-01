# GuildStickerResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**tags** | **str** |  | 
**type** | **int** |  | 
**format_type** | **int** |  | [optional] 
**description** | **str** |  | [optional] 
**available** | **bool** |  | 
**guild_id** | **str** |  | 
**user** | [**UserResponse**](UserResponse.md) |  | [optional] 

## Example

```python
from dc_rest.models.guild_sticker_response import GuildStickerResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GuildStickerResponse from a JSON string
guild_sticker_response_instance = GuildStickerResponse.from_json(json)
# print the JSON string representation of the object
print(GuildStickerResponse.to_json())

# convert the object into a dict
guild_sticker_response_dict = guild_sticker_response_instance.to_dict()
# create an instance of GuildStickerResponse from a dict
guild_sticker_response_from_dict = GuildStickerResponse.from_dict(guild_sticker_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


