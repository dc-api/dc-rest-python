# LobbyMemberRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**metadata** | **Dict[str, str]** |  | [optional] 
**flags** | **int** |  | [optional] 

## Example

```python
from dc_rest.models.lobby_member_request import LobbyMemberRequest

# TODO update the JSON string below
json = "{}"
# create an instance of LobbyMemberRequest from a JSON string
lobby_member_request_instance = LobbyMemberRequest.from_json(json)
# print the JSON string representation of the object
print(LobbyMemberRequest.to_json())

# convert the object into a dict
lobby_member_request_dict = lobby_member_request_instance.to_dict()
# create an instance of LobbyMemberRequest from a dict
lobby_member_request_from_dict = LobbyMemberRequest.from_dict(lobby_member_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


