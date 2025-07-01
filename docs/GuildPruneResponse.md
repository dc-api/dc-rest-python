# GuildPruneResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pruned** | **int** |  | [optional] 

## Example

```python
from dc_rest.models.guild_prune_response import GuildPruneResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GuildPruneResponse from a JSON string
guild_prune_response_instance = GuildPruneResponse.from_json(json)
# print the JSON string representation of the object
print(GuildPruneResponse.to_json())

# convert the object into a dict
guild_prune_response_dict = guild_prune_response_instance.to_dict()
# create an instance of GuildPruneResponse from a dict
guild_prune_response_from_dict = GuildPruneResponse.from_dict(guild_prune_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


