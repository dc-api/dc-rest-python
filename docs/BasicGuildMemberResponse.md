# BasicGuildMemberResponse


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
**collectibles** | [**UserCollectiblesResponse**](UserCollectiblesResponse.md) |  | [optional] 

## Example

```python
from dc_rest.models.basic_guild_member_response import BasicGuildMemberResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BasicGuildMemberResponse from a JSON string
basic_guild_member_response_instance = BasicGuildMemberResponse.from_json(json)
# print the JSON string representation of the object
print(BasicGuildMemberResponse.to_json())

# convert the object into a dict
basic_guild_member_response_dict = basic_guild_member_response_instance.to_dict()
# create an instance of BasicGuildMemberResponse from a dict
basic_guild_member_response_from_dict = BasicGuildMemberResponse.from_dict(basic_guild_member_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


