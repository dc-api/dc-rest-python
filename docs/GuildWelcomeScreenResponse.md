# GuildWelcomeScreenResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**welcome_channels** | [**List[GuildWelcomeScreenChannelResponse]**](GuildWelcomeScreenChannelResponse.md) |  | 

## Example

```python
from dc_rest.models.guild_welcome_screen_response import GuildWelcomeScreenResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GuildWelcomeScreenResponse from a JSON string
guild_welcome_screen_response_instance = GuildWelcomeScreenResponse.from_json(json)
# print the JSON string representation of the object
print(GuildWelcomeScreenResponse.to_json())

# convert the object into a dict
guild_welcome_screen_response_dict = guild_welcome_screen_response_instance.to_dict()
# create an instance of GuildWelcomeScreenResponse from a dict
guild_welcome_screen_response_from_dict = GuildWelcomeScreenResponse.from_dict(guild_welcome_screen_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


