# PrivateGuildMemberResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**avatar** | **str** |  | [optional] 
**avatar_decoration_data** | [**UserAvatarDecorationResponse**](UserAvatarDecorationResponse.md) |  | [optional] 
**banner** | **str** |  | [optional] 
**communication_disabled_until** | **datetime** |  | [optional] 
**flags** | **int** |  | 
**joined_at** | **datetime** |  | 
**nick** | **str** |  | [optional] 
**pending** | **bool** |  | 
**premium_since** | **datetime** |  | [optional] 
**roles** | **List[str]** |  | 
**user** | [**UserResponse**](UserResponse.md) |  | 
**mute** | **bool** |  | 
**deaf** | **bool** |  | 

## Example

```python
from dc_rest.models.private_guild_member_response import PrivateGuildMemberResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PrivateGuildMemberResponse from a JSON string
private_guild_member_response_instance = PrivateGuildMemberResponse.from_json(json)
# print the JSON string representation of the object
print(PrivateGuildMemberResponse.to_json())

# convert the object into a dict
private_guild_member_response_dict = private_guild_member_response_instance.to_dict()
# create an instance of PrivateGuildMemberResponse from a dict
private_guild_member_response_from_dict = PrivateGuildMemberResponse.from_dict(private_guild_member_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


