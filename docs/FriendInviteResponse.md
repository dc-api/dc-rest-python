# FriendInviteResponse


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

## Example

```python
from dc_rest.models.friend_invite_response import FriendInviteResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FriendInviteResponse from a JSON string
friend_invite_response_instance = FriendInviteResponse.from_json(json)
# print the JSON string representation of the object
print(FriendInviteResponse.to_json())

# convert the object into a dict
friend_invite_response_dict = friend_invite_response_instance.to_dict()
# create an instance of FriendInviteResponse from a dict
friend_invite_response_from_dict = FriendInviteResponse.from_dict(friend_invite_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


