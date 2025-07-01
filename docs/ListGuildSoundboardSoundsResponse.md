# ListGuildSoundboardSoundsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[SoundboardSoundResponse]**](SoundboardSoundResponse.md) |  | 

## Example

```python
from dc_rest.models.list_guild_soundboard_sounds_response import ListGuildSoundboardSoundsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListGuildSoundboardSoundsResponse from a JSON string
list_guild_soundboard_sounds_response_instance = ListGuildSoundboardSoundsResponse.from_json(json)
# print the JSON string representation of the object
print(ListGuildSoundboardSoundsResponse.to_json())

# convert the object into a dict
list_guild_soundboard_sounds_response_dict = list_guild_soundboard_sounds_response_instance.to_dict()
# create an instance of ListGuildSoundboardSoundsResponse from a dict
list_guild_soundboard_sounds_response_from_dict = ListGuildSoundboardSoundsResponse.from_dict(list_guild_soundboard_sounds_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


