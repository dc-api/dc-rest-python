# AddLobbyMemberRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | **Dict[str, str]** |  | [optional] 
**flags** | **int** |  | [optional] 

## Example

```python
from dc_rest.models.add_lobby_member_request import AddLobbyMemberRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddLobbyMemberRequest from a JSON string
add_lobby_member_request_instance = AddLobbyMemberRequest.from_json(json)
# print the JSON string representation of the object
print(AddLobbyMemberRequest.to_json())

# convert the object into a dict
add_lobby_member_request_dict = add_lobby_member_request_instance.to_dict()
# create an instance of AddLobbyMemberRequest from a dict
add_lobby_member_request_from_dict = AddLobbyMemberRequest.from_dict(add_lobby_member_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


