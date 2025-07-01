# LobbyMemberResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**metadata** | **Dict[str, str]** |  | [optional] 
**flags** | **int** |  | 

## Example

```python
from dc_rest.models.lobby_member_response import LobbyMemberResponse

# TODO update the JSON string below
json = "{}"
# create an instance of LobbyMemberResponse from a JSON string
lobby_member_response_instance = LobbyMemberResponse.from_json(json)
# print the JSON string representation of the object
print(LobbyMemberResponse.to_json())

# convert the object into a dict
lobby_member_response_dict = lobby_member_response_instance.to_dict()
# create an instance of LobbyMemberResponse from a dict
lobby_member_response_from_dict = LobbyMemberResponse.from_dict(lobby_member_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


