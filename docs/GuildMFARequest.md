# GuildMFARequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**level** | **int** |  | 

## Example

```python
from dc_rest.models.guild_mfa_request import GuildMFARequest

# TODO update the JSON string below
json = "{}"
# create an instance of GuildMFARequest from a JSON string
guild_mfa_request_instance = GuildMFARequest.from_json(json)
# print the JSON string representation of the object
print(GuildMFARequest.to_json())

# convert the object into a dict
guild_mfa_request_dict = guild_mfa_request_instance.to_dict()
# create an instance of GuildMFARequest from a dict
guild_mfa_request_from_dict = GuildMFARequest.from_dict(guild_mfa_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


