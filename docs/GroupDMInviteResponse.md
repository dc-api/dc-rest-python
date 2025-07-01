# GroupDMInviteResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **int** |  | [optional] 
**code** | **str** |  | 
**inviter** | [**UserResponse**](UserResponse.md) |  | [optional] 
**max_age** | **int** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**expires_at** | **datetime** |  | [optional] 
**channel** | [**InviteChannelResponse**](InviteChannelResponse.md) |  | [optional] 
**approximate_member_count** | **int** |  | [optional] 

## Example

```python
from dc_rest.models.group_dm_invite_response import GroupDMInviteResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GroupDMInviteResponse from a JSON string
group_dm_invite_response_instance = GroupDMInviteResponse.from_json(json)
# print the JSON string representation of the object
print(GroupDMInviteResponse.to_json())

# convert the object into a dict
group_dm_invite_response_dict = group_dm_invite_response_instance.to_dict()
# create an instance of GroupDMInviteResponse from a dict
group_dm_invite_response_from_dict = GroupDMInviteResponse.from_dict(group_dm_invite_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


