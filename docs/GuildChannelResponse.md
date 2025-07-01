# GuildChannelResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**type** | **int** |  | 
**last_message_id** | **str** |  | [optional] 
**flags** | **int** |  | 
**last_pin_timestamp** | **datetime** |  | [optional] 
**guild_id** | **str** |  | 
**name** | **str** |  | 
**parent_id** | **str** |  | [optional] 
**rate_limit_per_user** | **int** |  | [optional] 
**bitrate** | **int** |  | [optional] 
**user_limit** | **int** |  | [optional] 
**rtc_region** | **str** |  | [optional] 
**video_quality_mode** | **int** |  | [optional] 
**permissions** | **str** |  | [optional] 
**topic** | **str** |  | [optional] 
**default_auto_archive_duration** | **int** |  | [optional] 
**default_thread_rate_limit_per_user** | **int** |  | [optional] 
**position** | **int** |  | 
**permission_overwrites** | [**List[ChannelPermissionOverwriteResponse]**](ChannelPermissionOverwriteResponse.md) |  | [optional] 
**nsfw** | **bool** |  | [optional] 
**available_tags** | [**List[ForumTagResponse]**](ForumTagResponse.md) |  | [optional] 
**default_reaction_emoji** | [**DefaultReactionEmojiResponse**](DefaultReactionEmojiResponse.md) |  | [optional] 
**default_sort_order** | **int** |  | [optional] 
**default_forum_layout** | **int** |  | [optional] 
**default_tag_setting** | **str** |  | [optional] 
**hd_streaming_until** | **datetime** |  | [optional] 
**hd_streaming_buyer_id** | **str** |  | [optional] 

## Example

```python
from dc_rest.models.guild_channel_response import GuildChannelResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GuildChannelResponse from a JSON string
guild_channel_response_instance = GuildChannelResponse.from_json(json)
# print the JSON string representation of the object
print(GuildChannelResponse.to_json())

# convert the object into a dict
guild_channel_response_dict = guild_channel_response_instance.to_dict()
# create an instance of GuildChannelResponse from a dict
guild_channel_response_from_dict = GuildChannelResponse.from_dict(guild_channel_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


