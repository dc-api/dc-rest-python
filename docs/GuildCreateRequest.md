# GuildCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**name** | **str** |  | 
**region** | **str** |  | [optional] 
**icon** | **str** |  | [optional] 
**verification_level** | **int** |  | [optional] 
**default_message_notifications** | **int** |  | [optional] 
**explicit_content_filter** | **int** |  | [optional] 
**preferred_locale** | **str** |  | [optional] 
**afk_timeout** | **int** |  | [optional] 
**roles** | [**List[CreateGuildRequestRoleItem]**](CreateGuildRequestRoleItem.md) |  | [optional] 
**channels** | [**List[CreateGuildRequestChannelItem]**](CreateGuildRequestChannelItem.md) |  | [optional] 
**afk_channel_id** | **str** |  | [optional] 
**system_channel_id** | **str** |  | [optional] 
**system_channel_flags** | **int** |  | [optional] 

## Example

```python
from dc_rest.models.guild_create_request import GuildCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GuildCreateRequest from a JSON string
guild_create_request_instance = GuildCreateRequest.from_json(json)
# print the JSON string representation of the object
print(GuildCreateRequest.to_json())

# convert the object into a dict
guild_create_request_dict = guild_create_request_instance.to_dict()
# create an instance of GuildCreateRequest from a dict
guild_create_request_from_dict = GuildCreateRequest.from_dict(guild_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


