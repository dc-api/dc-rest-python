# BulkBanUsersResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**banned_users** | **List[str]** |  | 
**failed_users** | **List[str]** |  | 

## Example

```python
from dc_rest.models.bulk_ban_users_response import BulkBanUsersResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BulkBanUsersResponse from a JSON string
bulk_ban_users_response_instance = BulkBanUsersResponse.from_json(json)
# print the JSON string representation of the object
print(BulkBanUsersResponse.to_json())

# convert the object into a dict
bulk_ban_users_response_dict = bulk_ban_users_response_instance.to_dict()
# create an instance of BulkBanUsersResponse from a dict
bulk_ban_users_response_from_dict = BulkBanUsersResponse.from_dict(bulk_ban_users_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


