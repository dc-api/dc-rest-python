# GuildRoleResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**description** | **str** |  | [optional] 
**permissions** | **str** |  | 
**position** | **int** |  | 
**color** | **int** |  | 
**colors** | [**GuildRoleColorsResponse**](GuildRoleColorsResponse.md) |  | [optional] 
**hoist** | **bool** |  | 
**managed** | **bool** |  | 
**mentionable** | **bool** |  | 
**icon** | **str** |  | [optional] 
**unicode_emoji** | **str** |  | [optional] 
**tags** | [**GuildRoleTagsResponse**](GuildRoleTagsResponse.md) |  | [optional] 
**flags** | **int** |  | 

## Example

```python
from dc_rest.models.guild_role_response import GuildRoleResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GuildRoleResponse from a JSON string
guild_role_response_instance = GuildRoleResponse.from_json(json)
# print the JSON string representation of the object
print(GuildRoleResponse.to_json())

# convert the object into a dict
guild_role_response_dict = guild_role_response_instance.to_dict()
# create an instance of GuildRoleResponse from a dict
guild_role_response_from_dict = GuildRoleResponse.from_dict(guild_role_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


