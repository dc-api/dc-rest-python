# GuildInviteResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **int** |  | [optional] 
**code** | **str** |  | 
**inviter** | [**UserResponse**](UserResponse.md) |  | [optional] 
**max_age** | **int** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**expires_at** | **datetime** |  | [optional] 
**is_contact** | **bool** |  | [optional] 
**flags** | **int** |  | [optional] 
**guild** | [**InviteGuildResponse**](InviteGuildResponse.md) |  | [optional] 
**guild_id** | **str** |  | [optional] 
**channel** | [**InviteChannelResponse**](InviteChannelResponse.md) |  | [optional] 
**target_type** | **int** |  | [optional] 
**target_user** | [**UserResponse**](UserResponse.md) |  | [optional] 
**target_application** | [**InviteApplicationResponse**](InviteApplicationResponse.md) |  | [optional] 
**guild_scheduled_event** | [**ScheduledEventResponse**](ScheduledEventResponse.md) |  | [optional] 
**uses** | **int** |  | [optional] 
**max_uses** | **int** |  | [optional] 
**temporary** | **bool** |  | [optional] 
**approximate_member_count** | **int** |  | [optional] 
**approximate_presence_count** | **int** |  | [optional] 
**is_nickname_changeable** | **bool** |  | [optional] 

## Example

```python
from dc_rest.models.guild_invite_response import GuildInviteResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GuildInviteResponse from a JSON string
guild_invite_response_instance = GuildInviteResponse.from_json(json)
# print the JSON string representation of the object
print(GuildInviteResponse.to_json())

# convert the object into a dict
guild_invite_response_dict = guild_invite_response_instance.to_dict()
# create an instance of GuildInviteResponse from a dict
guild_invite_response_from_dict = GuildInviteResponse.from_dict(guild_invite_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


