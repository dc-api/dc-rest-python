# GuildTemplateRoleColorsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**primary_color** | **int** |  | 
**secondary_color** | **int** |  | [optional] 
**tertiary_color** | **int** |  | [optional] 

## Example

```python
from dc_rest.models.guild_template_role_colors_response import GuildTemplateRoleColorsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GuildTemplateRoleColorsResponse from a JSON string
guild_template_role_colors_response_instance = GuildTemplateRoleColorsResponse.from_json(json)
# print the JSON string representation of the object
print(GuildTemplateRoleColorsResponse.to_json())

# convert the object into a dict
guild_template_role_colors_response_dict = guild_template_role_colors_response_instance.to_dict()
# create an instance of GuildTemplateRoleColorsResponse from a dict
guild_template_role_colors_response_from_dict = GuildTemplateRoleColorsResponse.from_dict(guild_template_role_colors_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


