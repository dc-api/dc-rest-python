# LobbyMessageResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**type** | **int** |  | 
**content** | **str** |  | 
**lobby_id** | **str** |  | 
**channel_id** | **str** |  | 
**author** | [**UserResponse**](UserResponse.md) |  | 
**metadata** | **Dict[str, str]** |  | [optional] 
**flags** | **int** |  | 
**application_id** | **str** |  | [optional] 

## Example

```python
from dc_rest.models.lobby_message_response import LobbyMessageResponse

# TODO update the JSON string below
json = "{}"
# create an instance of LobbyMessageResponse from a JSON string
lobby_message_response_instance = LobbyMessageResponse.from_json(json)
# print the JSON string representation of the object
print(LobbyMessageResponse.to_json())

# convert the object into a dict
lobby_message_response_dict = lobby_message_response_instance.to_dict()
# create an instance of LobbyMessageResponse from a dict
lobby_message_response_from_dict = LobbyMessageResponse.from_dict(lobby_message_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


