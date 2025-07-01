# GuildBanResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user** | [**UserResponse**](UserResponse.md) |  | 
**reason** | **str** |  | [optional] 

## Example

```python
from dc_rest.models.guild_ban_response import GuildBanResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GuildBanResponse from a JSON string
guild_ban_response_instance = GuildBanResponse.from_json(json)
# print the JSON string representation of the object
print(GuildBanResponse.to_json())

# convert the object into a dict
guild_ban_response_dict = guild_ban_response_instance.to_dict()
# create an instance of GuildBanResponse from a dict
guild_ban_response_from_dict = GuildBanResponse.from_dict(guild_ban_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


