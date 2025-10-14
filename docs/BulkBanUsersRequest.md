# BulkBanUsersRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_ids** | **List[str]** |  | 
**delete_message_seconds** | **int** |  | [optional] 

## Example

```python
from dc_rest.models.bulk_ban_users_request import BulkBanUsersRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BulkBanUsersRequest from a JSON string
bulk_ban_users_request_instance = BulkBanUsersRequest.from_json(json)
# print the JSON string representation of the object
print(BulkBanUsersRequest.to_json())

# convert the object into a dict
bulk_ban_users_request_dict = bulk_ban_users_request_instance.to_dict()
# create an instance of BulkBanUsersRequest from a dict
bulk_ban_users_request_from_dict = BulkBanUsersRequest.from_dict(bulk_ban_users_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


