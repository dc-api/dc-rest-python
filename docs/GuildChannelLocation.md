# GuildChannelLocation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**kind** | **str** |  | 
**channel_id** | **str** |  | 
**guild_id** | **str** |  | 

## Example

```python
from dc_rest.models.guild_channel_location import GuildChannelLocation

# TODO update the JSON string below
json = "{}"
# create an instance of GuildChannelLocation from a JSON string
guild_channel_location_instance = GuildChannelLocation.from_json(json)
# print the JSON string representation of the object
print(GuildChannelLocation.to_json())

# convert the object into a dict
guild_channel_location_dict = guild_channel_location_instance.to_dict()
# create an instance of GuildChannelLocation from a dict
guild_channel_location_from_dict = GuildChannelLocation.from_dict(guild_channel_location_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


