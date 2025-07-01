# BanUserFromGuildRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**delete_message_seconds** | **int** |  | [optional] 
**delete_message_days** | **int** |  | [optional] 

## Example

```python
from dc_rest.models.ban_user_from_guild_request import BanUserFromGuildRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BanUserFromGuildRequest from a JSON string
ban_user_from_guild_request_instance = BanUserFromGuildRequest.from_json(json)
# print the JSON string representation of the object
print(BanUserFromGuildRequest.to_json())

# convert the object into a dict
ban_user_from_guild_request_dict = ban_user_from_guild_request_instance.to_dict()
# create an instance of BanUserFromGuildRequest from a dict
ban_user_from_guild_request_from_dict = BanUserFromGuildRequest.from_dict(ban_user_from_guild_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


