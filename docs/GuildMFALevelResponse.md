# GuildMFALevelResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**level** | **int** |  | 

## Example

```python
from dc_rest.models.guild_mfa_level_response import GuildMFALevelResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GuildMFALevelResponse from a JSON string
guild_mfa_level_response_instance = GuildMFALevelResponse.from_json(json)
# print the JSON string representation of the object
print(GuildMFALevelResponse.to_json())

# convert the object into a dict
guild_mfa_level_response_dict = guild_mfa_level_response_instance.to_dict()
# create an instance of GuildMFALevelResponse from a dict
guild_mfa_level_response_from_dict = GuildMFALevelResponse.from_dict(guild_mfa_level_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


