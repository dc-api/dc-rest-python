# BulkLobbyMemberRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**metadata** | **Dict[str, str]** |  | [optional] 
**flags** | **int** |  | [optional] 
**remove_member** | **bool** |  | [optional] 

## Example

```python
from dc_rest.models.bulk_lobby_member_request import BulkLobbyMemberRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BulkLobbyMemberRequest from a JSON string
bulk_lobby_member_request_instance = BulkLobbyMemberRequest.from_json(json)
# print the JSON string representation of the object
print(BulkLobbyMemberRequest.to_json())

# convert the object into a dict
bulk_lobby_member_request_dict = bulk_lobby_member_request_instance.to_dict()
# create an instance of BulkLobbyMemberRequest from a dict
bulk_lobby_member_request_from_dict = BulkLobbyMemberRequest.from_dict(bulk_lobby_member_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


