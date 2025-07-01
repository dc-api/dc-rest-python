# LobbyResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**application_id** | **str** |  | 
**metadata** | **Dict[str, str]** |  | [optional] 
**members** | [**List[LobbyMemberResponse]**](LobbyMemberResponse.md) |  | [optional] 
**linked_channel** | [**GuildChannelResponse**](GuildChannelResponse.md) |  | [optional] 

## Example

```python
from dc_rest.models.lobby_response import LobbyResponse

# TODO update the JSON string below
json = "{}"
# create an instance of LobbyResponse from a JSON string
lobby_response_instance = LobbyResponse.from_json(json)
# print the JSON string representation of the object
print(LobbyResponse.to_json())

# convert the object into a dict
lobby_response_dict = lobby_response_instance.to_dict()
# create an instance of LobbyResponse from a dict
lobby_response_from_dict = LobbyResponse.from_dict(lobby_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


