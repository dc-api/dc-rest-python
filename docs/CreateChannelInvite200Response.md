# CreateChannelInvite200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **int** |  | 
**code** | **str** |  | 
**inviter** | [**UserResponse**](UserResponse.md) |  | [optional] 
**max_age** | **int** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**expires_at** | **datetime** |  | [optional] 
**friends_count** | **int** |  | [optional] 
**channel** | [**InviteChannelResponse**](InviteChannelResponse.md) |  | 
**is_contact** | **bool** |  | [optional] 
**uses** | **int** |  | [optional] 
**max_uses** | **int** |  | [optional] 
**flags** | **int** |  | [optional] 
**approximate_member_count** | **int** |  | [optional] 
**guild** | [**InviteGuildResponse**](InviteGuildResponse.md) |  | 
**guild_id** | **str** |  | 
**target_type** | **int** |  | [optional] 
**target_user** | [**UserResponse**](UserResponse.md) |  | [optional] 
**target_application** | [**InviteApplicationResponse**](InviteApplicationResponse.md) |  | [optional] 
**guild_scheduled_event** | [**ScheduledEventResponse**](ScheduledEventResponse.md) |  | [optional] 
**temporary** | **bool** |  | [optional] 
**approximate_presence_count** | **int** |  | [optional] 
**is_nickname_changeable** | **bool** |  | [optional] 

## Example

```python
from dc_rest.models.create_channel_invite200_response import CreateChannelInvite200Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateChannelInvite200Response from a JSON string
create_channel_invite200_response_instance = CreateChannelInvite200Response.from_json(json)
# print the JSON string representation of the object
print(CreateChannelInvite200Response.to_json())

# convert the object into a dict
create_channel_invite200_response_dict = create_channel_invite200_response_instance.to_dict()
# create an instance of CreateChannelInvite200Response from a dict
create_channel_invite200_response_from_dict = CreateChannelInvite200Response.from_dict(create_channel_invite200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


