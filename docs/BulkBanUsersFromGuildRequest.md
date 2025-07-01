# BulkBanUsersFromGuildRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_ids** | **List[str]** |  | 
**delete_message_seconds** | **int** |  | [optional] 

## Example

```python
from dc_rest.models.bulk_ban_users_from_guild_request import BulkBanUsersFromGuildRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BulkBanUsersFromGuildRequest from a JSON string
bulk_ban_users_from_guild_request_instance = BulkBanUsersFromGuildRequest.from_json(json)
# print the JSON string representation of the object
print(BulkBanUsersFromGuildRequest.to_json())

# convert the object into a dict
bulk_ban_users_from_guild_request_dict = bulk_ban_users_from_guild_request_instance.to_dict()
# create an instance of BulkBanUsersFromGuildRequest from a dict
bulk_ban_users_from_guild_request_from_dict = BulkBanUsersFromGuildRequest.from_dict(bulk_ban_users_from_guild_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


