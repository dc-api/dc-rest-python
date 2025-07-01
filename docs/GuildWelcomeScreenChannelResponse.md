# GuildWelcomeScreenChannelResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channel_id** | **str** |  | 
**description** | **str** |  | 
**emoji_id** | **str** |  | [optional] 
**emoji_name** | **str** |  | [optional] 

## Example

```python
from dc_rest.models.guild_welcome_screen_channel_response import GuildWelcomeScreenChannelResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GuildWelcomeScreenChannelResponse from a JSON string
guild_welcome_screen_channel_response_instance = GuildWelcomeScreenChannelResponse.from_json(json)
# print the JSON string representation of the object
print(GuildWelcomeScreenChannelResponse.to_json())

# convert the object into a dict
guild_welcome_screen_channel_response_dict = guild_welcome_screen_channel_response_instance.to_dict()
# create an instance of GuildWelcomeScreenChannelResponse from a dict
guild_welcome_screen_channel_response_from_dict = GuildWelcomeScreenChannelResponse.from_dict(guild_welcome_screen_channel_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


