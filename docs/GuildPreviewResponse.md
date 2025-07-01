# GuildPreviewResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**icon** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**home_header** | **str** |  | [optional] 
**splash** | **str** |  | [optional] 
**discovery_splash** | **str** |  | [optional] 
**features** | **List[str]** |  | 
**approximate_member_count** | **int** |  | 
**approximate_presence_count** | **int** |  | 
**emojis** | [**List[EmojiResponse]**](EmojiResponse.md) |  | 
**stickers** | [**List[GuildStickerResponse]**](GuildStickerResponse.md) |  | 

## Example

```python
from dc_rest.models.guild_preview_response import GuildPreviewResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GuildPreviewResponse from a JSON string
guild_preview_response_instance = GuildPreviewResponse.from_json(json)
# print the JSON string representation of the object
print(GuildPreviewResponse.to_json())

# convert the object into a dict
guild_preview_response_dict = guild_preview_response_instance.to_dict()
# create an instance of GuildPreviewResponse from a dict
guild_preview_response_from_dict = GuildPreviewResponse.from_dict(guild_preview_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


