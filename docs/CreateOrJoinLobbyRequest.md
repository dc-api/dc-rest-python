# CreateOrJoinLobbyRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**idle_timeout_seconds** | **int** |  | [optional] 
**lobby_metadata** | **Dict[str, str]** |  | [optional] 
**member_metadata** | **Dict[str, str]** |  | [optional] 
**secret** | **str** |  | 

## Example

```python
from dc_rest.models.create_or_join_lobby_request import CreateOrJoinLobbyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateOrJoinLobbyRequest from a JSON string
create_or_join_lobby_request_instance = CreateOrJoinLobbyRequest.from_json(json)
# print the JSON string representation of the object
print(CreateOrJoinLobbyRequest.to_json())

# convert the object into a dict
create_or_join_lobby_request_dict = create_or_join_lobby_request_instance.to_dict()
# create an instance of CreateOrJoinLobbyRequest from a dict
create_or_join_lobby_request_from_dict = CreateOrJoinLobbyRequest.from_dict(create_or_join_lobby_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


