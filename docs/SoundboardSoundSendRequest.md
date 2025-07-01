# SoundboardSoundSendRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sound_id** | **str** |  | 
**source_guild_id** | **str** |  | [optional] 

## Example

```python
from dc_rest.models.soundboard_sound_send_request import SoundboardSoundSendRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SoundboardSoundSendRequest from a JSON string
soundboard_sound_send_request_instance = SoundboardSoundSendRequest.from_json(json)
# print the JSON string representation of the object
print(SoundboardSoundSendRequest.to_json())

# convert the object into a dict
soundboard_sound_send_request_dict = soundboard_sound_send_request_instance.to_dict()
# create an instance of SoundboardSoundSendRequest from a dict
soundboard_sound_send_request_from_dict = SoundboardSoundSendRequest.from_dict(soundboard_sound_send_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


