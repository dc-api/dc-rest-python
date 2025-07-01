# GuildTemplateSnapshotResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**description** | **str** |  | [optional] 
**region** | **str** |  | [optional] 
**verification_level** | **int** |  | 
**default_message_notifications** | **int** |  | 
**explicit_content_filter** | **int** |  | 
**preferred_locale** | **str** |  | 
**afk_channel_id** | **str** |  | [optional] 
**afk_timeout** | **int** |  | 
**system_channel_id** | **str** |  | [optional] 
**system_channel_flags** | **int** |  | 
**roles** | [**List[GuildTemplateRoleResponse]**](GuildTemplateRoleResponse.md) |  | 
**channels** | [**List[GuildTemplateChannelResponse]**](GuildTemplateChannelResponse.md) |  | 

## Example

```python
from dc_rest.models.guild_template_snapshot_response import GuildTemplateSnapshotResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GuildTemplateSnapshotResponse from a JSON string
guild_template_snapshot_response_instance = GuildTemplateSnapshotResponse.from_json(json)
# print the JSON string representation of the object
print(GuildTemplateSnapshotResponse.to_json())

# convert the object into a dict
guild_template_snapshot_response_dict = guild_template_snapshot_response_instance.to_dict()
# create an instance of GuildTemplateSnapshotResponse from a dict
guild_template_snapshot_response_from_dict = GuildTemplateSnapshotResponse.from_dict(guild_template_snapshot_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


