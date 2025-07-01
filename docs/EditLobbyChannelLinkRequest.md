# EditLobbyChannelLinkRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channel_id** | **str** |  | [optional] 

## Example

```python
from dc_rest.models.edit_lobby_channel_link_request import EditLobbyChannelLinkRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EditLobbyChannelLinkRequest from a JSON string
edit_lobby_channel_link_request_instance = EditLobbyChannelLinkRequest.from_json(json)
# print the JSON string representation of the object
print(EditLobbyChannelLinkRequest.to_json())

# convert the object into a dict
edit_lobby_channel_link_request_dict = edit_lobby_channel_link_request_instance.to_dict()
# create an instance of EditLobbyChannelLinkRequest from a dict
edit_lobby_channel_link_request_from_dict = EditLobbyChannelLinkRequest.from_dict(edit_lobby_channel_link_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


