# GuildTemplateChannelResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**type** | **int** |  | 
**name** | **str** |  | [optional] 
**position** | **int** |  | [optional] 
**topic** | **str** |  | [optional] 
**bitrate** | **int** |  | 
**user_limit** | **int** |  | 
**nsfw** | **bool** |  | 
**rate_limit_per_user** | **int** |  | 
**parent_id** | **str** |  | [optional] 
**default_auto_archive_duration** | **int** |  | [optional] 
**permission_overwrites** | [**List[Optional[ChannelPermissionOverwriteResponse]]**](ChannelPermissionOverwriteResponse.md) |  | 
**available_tags** | [**List[GuildTemplateChannelTags]**](GuildTemplateChannelTags.md) |  | [optional] 
**template** | **str** |  | 
**default_reaction_emoji** | [**DefaultReactionEmojiResponse**](DefaultReactionEmojiResponse.md) |  | [optional] 
**default_thread_rate_limit_per_user** | **int** |  | [optional] 
**default_sort_order** | **int** |  | [optional] 
**default_forum_layout** | **int** |  | [optional] 
**default_tag_setting** | **str** |  | [optional] 
**icon_emoji** | **object** |  | [optional] 
**theme_color** | **int** |  | [optional] 

## Example

```python
from dc_rest.models.guild_template_channel_response import GuildTemplateChannelResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GuildTemplateChannelResponse from a JSON string
guild_template_channel_response_instance = GuildTemplateChannelResponse.from_json(json)
# print the JSON string representation of the object
print(GuildTemplateChannelResponse.to_json())

# convert the object into a dict
guild_template_channel_response_dict = guild_template_channel_response_instance.to_dict()
# create an instance of GuildTemplateChannelResponse from a dict
guild_template_channel_response_from_dict = GuildTemplateChannelResponse.from_dict(guild_template_channel_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


