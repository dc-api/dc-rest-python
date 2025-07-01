# GuildPatchRequestPartial


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**region** | **str** |  | [optional] 
**icon** | **str** |  | [optional] 
**verification_level** | **int** |  | [optional] 
**default_message_notifications** | **int** |  | [optional] 
**explicit_content_filter** | **int** |  | [optional] 
**preferred_locale** | **str** |  | [optional] 
**afk_timeout** | **int** |  | [optional] 
**afk_channel_id** | **str** |  | [optional] 
**system_channel_id** | **str** |  | [optional] 
**owner_id** | **str** |  | [optional] 
**splash** | **str** |  | [optional] 
**banner** | **str** |  | [optional] 
**system_channel_flags** | **int** |  | [optional] 
**features** | **List[Optional[str]]** |  | [optional] 
**discovery_splash** | **str** |  | [optional] 
**home_header** | **str** |  | [optional] 
**rules_channel_id** | **str** |  | [optional] 
**safety_alerts_channel_id** | **str** |  | [optional] 
**public_updates_channel_id** | **str** |  | [optional] 
**premium_progress_bar_enabled** | **bool** |  | [optional] 

## Example

```python
from dc_rest.models.guild_patch_request_partial import GuildPatchRequestPartial

# TODO update the JSON string below
json = "{}"
# create an instance of GuildPatchRequestPartial from a JSON string
guild_patch_request_partial_instance = GuildPatchRequestPartial.from_json(json)
# print the JSON string representation of the object
print(GuildPatchRequestPartial.to_json())

# convert the object into a dict
guild_patch_request_partial_dict = guild_patch_request_partial_instance.to_dict()
# create an instance of GuildPatchRequestPartial from a dict
guild_patch_request_partial_from_dict = GuildPatchRequestPartial.from_dict(guild_patch_request_partial_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


