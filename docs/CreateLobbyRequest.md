# CreateLobbyRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**idle_timeout_seconds** | **int** |  | [optional] 
**members** | [**List[LobbyMemberRequest]**](LobbyMemberRequest.md) |  | [optional] 
**metadata** | **Dict[str, str]** |  | [optional] 

## Example

```python
from dc_rest.models.create_lobby_request import CreateLobbyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateLobbyRequest from a JSON string
create_lobby_request_instance = CreateLobbyRequest.from_json(json)
# print the JSON string representation of the object
print(CreateLobbyRequest.to_json())

# convert the object into a dict
create_lobby_request_dict = create_lobby_request_instance.to_dict()
# create an instance of CreateLobbyRequest from a dict
create_lobby_request_from_dict = CreateLobbyRequest.from_dict(create_lobby_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


