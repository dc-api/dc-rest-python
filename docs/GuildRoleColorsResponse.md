# GuildRoleColorsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**primary_color** | **int** |  | [optional] 
**secondary_color** | **int** |  | [optional] 
**tertiary_color** | **int** |  | [optional] 

## Example

```python
from dc_rest.models.guild_role_colors_response import GuildRoleColorsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GuildRoleColorsResponse from a JSON string
guild_role_colors_response_instance = GuildRoleColorsResponse.from_json(json)
# print the JSON string representation of the object
print(GuildRoleColorsResponse.to_json())

# convert the object into a dict
guild_role_colors_response_dict = guild_role_colors_response_instance.to_dict()
# create an instance of GuildRoleColorsResponse from a dict
guild_role_colors_response_from_dict = GuildRoleColorsResponse.from_dict(guild_role_colors_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


