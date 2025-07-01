# GuildTemplateRoleResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 
**permissions** | **str** |  | 
**color** | **int** |  | 
**hoist** | **bool** |  | 
**mentionable** | **bool** |  | 
**icon** | **str** |  | [optional] 
**unicode_emoji** | **str** |  | [optional] 

## Example

```python
from dc_rest.models.guild_template_role_response import GuildTemplateRoleResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GuildTemplateRoleResponse from a JSON string
guild_template_role_response_instance = GuildTemplateRoleResponse.from_json(json)
# print the JSON string representation of the object
print(GuildTemplateRoleResponse.to_json())

# convert the object into a dict
guild_template_role_response_dict = guild_template_role_response_instance.to_dict()
# create an instance of GuildTemplateRoleResponse from a dict
guild_template_role_response_from_dict = GuildTemplateRoleResponse.from_dict(guild_template_role_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


