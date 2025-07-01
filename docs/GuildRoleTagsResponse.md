# GuildRoleTagsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**premium_subscriber** | **object** |  | [optional] 
**bot_id** | **str** |  | [optional] 
**integration_id** | **str** |  | [optional] 
**subscription_listing_id** | **str** |  | [optional] 
**available_for_purchase** | **object** |  | [optional] 
**guild_connections** | **object** |  | [optional] 

## Example

```python
from dc_rest.models.guild_role_tags_response import GuildRoleTagsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GuildRoleTagsResponse from a JSON string
guild_role_tags_response_instance = GuildRoleTagsResponse.from_json(json)
# print the JSON string representation of the object
print(GuildRoleTagsResponse.to_json())

# convert the object into a dict
guild_role_tags_response_dict = guild_role_tags_response_instance.to_dict()
# create an instance of GuildRoleTagsResponse from a dict
guild_role_tags_response_from_dict = GuildRoleTagsResponse.from_dict(guild_role_tags_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


