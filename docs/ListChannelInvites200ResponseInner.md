# ListChannelInvites200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **int** |  | [optional] 
**code** | **str** |  | 
**inviter** | [**UserResponse**](UserResponse.md) |  | [optional] 
**max_age** | **int** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**expires_at** | **datetime** |  | [optional] 
**friends_count** | **int** |  | [optional] 
**channel** | [**InviteChannelResponse**](InviteChannelResponse.md) |  | [optional] 
**is_contact** | **bool** |  | [optional] 
**uses** | **int** |  | [optional] 
**max_uses** | **int** |  | [optional] 
**flags** | **int** |  | [optional] 
**approximate_member_count** | **int** |  | [optional] 
**guild** | [**InviteGuildResponse**](InviteGuildResponse.md) |  | [optional] 
**guild_id** | **str** |  | [optional] 
**target_type** | **int** |  | [optional] 
**target_user** | [**UserResponse**](UserResponse.md) |  | [optional] 
**target_application** | [**InviteApplicationResponse**](InviteApplicationResponse.md) |  | [optional] 
**guild_scheduled_event** | [**ScheduledEventResponse**](ScheduledEventResponse.md) |  | [optional] 
**temporary** | **bool** |  | [optional] 
**approximate_presence_count** | **int** |  | [optional] 
**is_nickname_changeable** | **bool** |  | [optional] 

## Example

```python
from dc_rest.models.list_channel_invites200_response_inner import ListChannelInvites200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of ListChannelInvites200ResponseInner from a JSON string
list_channel_invites200_response_inner_instance = ListChannelInvites200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(ListChannelInvites200ResponseInner.to_json())

# convert the object into a dict
list_channel_invites200_response_inner_dict = list_channel_invites200_response_inner_instance.to_dict()
# create an instance of ListChannelInvites200ResponseInner from a dict
list_channel_invites200_response_inner_from_dict = ListChannelInvites200ResponseInner.from_dict(list_channel_invites200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


