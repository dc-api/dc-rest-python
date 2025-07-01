# GetChannel200Response


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
**recipients** | [**List[UserResponse]**](UserResponse.md) |  | 
**icon** | **str** |  | [optional] 
**owner_id** | **str** |  | 
**managed** | **bool** |  | [optional] 
**application_id** | **str** |  | [optional] 
**thread_metadata** | [**ThreadMetadataResponse**](ThreadMetadataResponse.md) |  | [optional] 
**message_count** | **int** |  | 
**member_count** | **int** |  | 
**total_message_sent** | **int** |  | 
**applied_tags** | **List[str]** |  | [optional] 
**member** | [**ThreadMemberResponse**](ThreadMemberResponse.md) |  | [optional] 

## Example

```python
from dc_rest.models.get_channel200_response import GetChannel200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetChannel200Response from a JSON string
get_channel200_response_instance = GetChannel200Response.from_json(json)
# print the JSON string representation of the object
print(GetChannel200Response.to_json())

# convert the object into a dict
get_channel200_response_dict = get_channel200_response_instance.to_dict()
# create an instance of GetChannel200Response from a dict
get_channel200_response_from_dict = GetChannel200Response.from_dict(get_channel200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


