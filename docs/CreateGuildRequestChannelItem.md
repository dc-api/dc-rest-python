# CreateGuildRequestChannelItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **int** |  | [optional] 
**name** | **str** |  | 
**position** | **int** |  | [optional] 
**topic** | **str** |  | [optional] 
**bitrate** | **int** |  | [optional] 
**user_limit** | **int** |  | [optional] 
**nsfw** | **bool** |  | [optional] 
**rate_limit_per_user** | **int** |  | [optional] 
**parent_id** | **str** |  | [optional] 
**permission_overwrites** | [**List[ChannelPermissionOverwriteRequest]**](ChannelPermissionOverwriteRequest.md) |  | [optional] 
**rtc_region** | **str** |  | [optional] 
**video_quality_mode** | **int** |  | [optional] 
**default_auto_archive_duration** | **int** |  | [optional] 
**default_reaction_emoji** | [**UpdateDefaultReactionEmojiRequest**](UpdateDefaultReactionEmojiRequest.md) |  | [optional] 
**default_thread_rate_limit_per_user** | **int** |  | [optional] 
**default_sort_order** | **int** |  | [optional] 
**default_forum_layout** | **int** |  | [optional] 
**default_tag_setting** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**available_tags** | [**List[CreateOrUpdateThreadTagRequest]**](CreateOrUpdateThreadTagRequest.md) |  | [optional] 

## Example

```python
from dc_rest.models.create_guild_request_channel_item import CreateGuildRequestChannelItem

# TODO update the JSON string below
json = "{}"
# create an instance of CreateGuildRequestChannelItem from a JSON string
create_guild_request_channel_item_instance = CreateGuildRequestChannelItem.from_json(json)
# print the JSON string representation of the object
print(CreateGuildRequestChannelItem.to_json())

# convert the object into a dict
create_guild_request_channel_item_dict = create_guild_request_channel_item_instance.to_dict()
# create an instance of CreateGuildRequestChannelItem from a dict
create_guild_request_channel_item_from_dict = CreateGuildRequestChannelItem.from_dict(create_guild_request_channel_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


