# GuildWelcomeChannel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channel_id** | **str** |  | 
**description** | **str** |  | 
**emoji_id** | **str** |  | [optional] 
**emoji_name** | **str** |  | [optional] 

## Example

```python
from dc_rest.models.guild_welcome_channel import GuildWelcomeChannel

# TODO update the JSON string below
json = "{}"
# create an instance of GuildWelcomeChannel from a JSON string
guild_welcome_channel_instance = GuildWelcomeChannel.from_json(json)
# print the JSON string representation of the object
print(GuildWelcomeChannel.to_json())

# convert the object into a dict
guild_welcome_channel_dict = guild_welcome_channel_instance.to_dict()
# create an instance of GuildWelcomeChannel from a dict
guild_welcome_channel_from_dict = GuildWelcomeChannel.from_dict(guild_welcome_channel_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


