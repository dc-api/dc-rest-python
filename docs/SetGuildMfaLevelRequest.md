# SetGuildMfaLevelRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**level** | **int** |  | 

## Example

```python
from dc_rest.models.set_guild_mfa_level_request import SetGuildMfaLevelRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SetGuildMfaLevelRequest from a JSON string
set_guild_mfa_level_request_instance = SetGuildMfaLevelRequest.from_json(json)
# print the JSON string representation of the object
print(SetGuildMfaLevelRequest.to_json())

# convert the object into a dict
set_guild_mfa_level_request_dict = set_guild_mfa_level_request_instance.to_dict()
# create an instance of SetGuildMfaLevelRequest from a dict
set_guild_mfa_level_request_from_dict = SetGuildMfaLevelRequest.from_dict(set_guild_mfa_level_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


