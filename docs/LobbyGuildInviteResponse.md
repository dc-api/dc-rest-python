# LobbyGuildInviteResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | 

## Example

```python
from dc_rest.models.lobby_guild_invite_response import LobbyGuildInviteResponse

# TODO update the JSON string below
json = "{}"
# create an instance of LobbyGuildInviteResponse from a JSON string
lobby_guild_invite_response_instance = LobbyGuildInviteResponse.from_json(json)
# print the JSON string representation of the object
print(LobbyGuildInviteResponse.to_json())

# convert the object into a dict
lobby_guild_invite_response_dict = lobby_guild_invite_response_instance.to_dict()
# create an instance of LobbyGuildInviteResponse from a dict
lobby_guild_invite_response_from_dict = LobbyGuildInviteResponse.from_dict(lobby_guild_invite_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


