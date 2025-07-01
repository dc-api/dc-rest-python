# UpdateChannelRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**icon** | **str** |  | [optional] 
**type** | **int** |  | [optional] 
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
**flags** | **int** |  | [optional] 
**available_tags** | [**List[UpdateThreadTagRequest]**](UpdateThreadTagRequest.md) |  | [optional] 
**archived** | **bool** |  | [optional] 
**locked** | **bool** |  | [optional] 
**invitable** | **bool** |  | [optional] 
**auto_archive_duration** | **int** |  | [optional] 
**applied_tags** | **List[str]** |  | [optional] 

## Example

```python
from dc_rest.models.update_channel_request import UpdateChannelRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateChannelRequest from a JSON string
update_channel_request_instance = UpdateChannelRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateChannelRequest.to_json())

# convert the object into a dict
update_channel_request_dict = update_channel_request_instance.to_dict()
# create an instance of UpdateChannelRequest from a dict
update_channel_request_from_dict = UpdateChannelRequest.from_dict(update_channel_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


