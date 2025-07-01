# GuildTemplateResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | 
**name** | **str** |  | 
**description** | **str** |  | [optional] 
**usage_count** | **int** |  | 
**creator_id** | **str** |  | 
**creator** | [**UserResponse**](UserResponse.md) |  | [optional] 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**source_guild_id** | **str** |  | 
**serialized_source_guild** | [**GuildTemplateSnapshotResponse**](GuildTemplateSnapshotResponse.md) |  | 
**is_dirty** | **bool** |  | [optional] 

## Example

```python
from dc_rest.models.guild_template_response import GuildTemplateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GuildTemplateResponse from a JSON string
guild_template_response_instance = GuildTemplateResponse.from_json(json)
# print the JSON string representation of the object
print(GuildTemplateResponse.to_json())

# convert the object into a dict
guild_template_response_dict = guild_template_response_instance.to_dict()
# create an instance of GuildTemplateResponse from a dict
guild_template_response_from_dict = GuildTemplateResponse.from_dict(guild_template_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


