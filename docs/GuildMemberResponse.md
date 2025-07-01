# GuildMemberResponse


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
from dc_rest.models.guild_member_response import GuildMemberResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GuildMemberResponse from a JSON string
guild_member_response_instance = GuildMemberResponse.from_json(json)
# print the JSON string representation of the object
print(GuildMemberResponse.to_json())

# convert the object into a dict
guild_member_response_dict = guild_member_response_instance.to_dict()
# create an instance of GuildMemberResponse from a dict
guild_member_response_from_dict = GuildMemberResponse.from_dict(guild_member_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


