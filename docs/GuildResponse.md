# GuildResponse


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
**banner** | **str** |  | [optional] 
**owner_id** | **str** |  | 
**application_id** | **str** |  | [optional] 
**region** | **str** |  | 
**afk_channel_id** | **str** |  | [optional] 
**afk_timeout** | **int** |  | 
**system_channel_id** | **str** |  | [optional] 
**system_channel_flags** | **int** |  | 
**widget_enabled** | **bool** |  | 
**widget_channel_id** | **str** |  | [optional] 
**verification_level** | **int** |  | 
**roles** | [**List[GuildRoleResponse]**](GuildRoleResponse.md) |  | 
**default_message_notifications** | **int** |  | 
**mfa_level** | **int** |  | 
**explicit_content_filter** | **int** |  | 
**max_presences** | **int** |  | [optional] 
**max_members** | **int** |  | [optional] 
**max_stage_video_channel_users** | **int** |  | [optional] 
**max_video_channel_users** | **int** |  | [optional] 
**vanity_url_code** | **str** |  | [optional] 
**premium_tier** | **int** |  | 
**premium_subscription_count** | **int** |  | 
**preferred_locale** | **str** |  | 
**rules_channel_id** | **str** |  | [optional] 
**safety_alerts_channel_id** | **str** |  | [optional] 
**public_updates_channel_id** | **str** |  | [optional] 
**premium_progress_bar_enabled** | **bool** |  | 
**nsfw** | **bool** |  | 
**nsfw_level** | **int** |  | 
**emojis** | [**List[EmojiResponse]**](EmojiResponse.md) |  | 
**stickers** | [**List[GuildStickerResponse]**](GuildStickerResponse.md) |  | 

## Example

```python
from dc_rest.models.guild_response import GuildResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GuildResponse from a JSON string
guild_response_instance = GuildResponse.from_json(json)
# print the JSON string representation of the object
print(GuildResponse.to_json())

# convert the object into a dict
guild_response_dict = guild_response_instance.to_dict()
# create an instance of GuildResponse from a dict
guild_response_from_dict = GuildResponse.from_dict(guild_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


