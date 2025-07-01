# CreateGuildChannelRequest


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
**available_tags** | [**List[Optional[CreateOrUpdateThreadTagRequest]]**](CreateOrUpdateThreadTagRequest.md) |  | [optional] 

## Example

```python
from dc_rest.models.create_guild_channel_request import CreateGuildChannelRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateGuildChannelRequest from a JSON string
create_guild_channel_request_instance = CreateGuildChannelRequest.from_json(json)
# print the JSON string representation of the object
print(CreateGuildChannelRequest.to_json())

# convert the object into a dict
create_guild_channel_request_dict = create_guild_channel_request_instance.to_dict()
# create an instance of CreateGuildChannelRequest from a dict
create_guild_channel_request_from_dict = CreateGuildChannelRequest.from_dict(create_guild_channel_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


