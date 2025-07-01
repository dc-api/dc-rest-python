# GuildWithCountsResponse


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
**approximate_member_count** | **int** |  | [optional] 
**approximate_presence_count** | **int** |  | [optional] 

## Example

```python
from dc_rest.models.guild_with_counts_response import GuildWithCountsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GuildWithCountsResponse from a JSON string
guild_with_counts_response_instance = GuildWithCountsResponse.from_json(json)
# print the JSON string representation of the object
print(GuildWithCountsResponse.to_json())

# convert the object into a dict
guild_with_counts_response_dict = guild_with_counts_response_instance.to_dict()
# create an instance of GuildWithCountsResponse from a dict
guild_with_counts_response_from_dict = GuildWithCountsResponse.from_dict(guild_with_counts_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


