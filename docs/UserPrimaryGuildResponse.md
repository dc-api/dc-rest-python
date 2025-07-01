# UserPrimaryGuildResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identity_guild_id** | **str** |  | [optional] 
**identity_enabled** | **bool** |  | [optional] 
**tag** | **str** |  | [optional] 
**badge** | **str** |  | [optional] 

## Example

```python
from dc_rest.models.user_primary_guild_response import UserPrimaryGuildResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UserPrimaryGuildResponse from a JSON string
user_primary_guild_response_instance = UserPrimaryGuildResponse.from_json(json)
# print the JSON string representation of the object
print(UserPrimaryGuildResponse.to_json())

# convert the object into a dict
user_primary_guild_response_dict = user_primary_guild_response_instance.to_dict()
# create an instance of UserPrimaryGuildResponse from a dict
user_primary_guild_response_from_dict = UserPrimaryGuildResponse.from_dict(user_primary_guild_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


