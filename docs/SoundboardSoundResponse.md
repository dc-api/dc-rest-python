# SoundboardSoundResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**sound_id** | **str** |  | 
**volume** | **float** |  | 
**emoji_id** | **str** |  | [optional] 
**emoji_name** | **str** |  | [optional] 
**guild_id** | **str** |  | [optional] 
**available** | **bool** |  | 
**user** | [**UserResponse**](UserResponse.md) |  | [optional] 

## Example

```python
from dc_rest.models.soundboard_sound_response import SoundboardSoundResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SoundboardSoundResponse from a JSON string
soundboard_sound_response_instance = SoundboardSoundResponse.from_json(json)
# print the JSON string representation of the object
print(SoundboardSoundResponse.to_json())

# convert the object into a dict
soundboard_sound_response_dict = soundboard_sound_response_instance.to_dict()
# create an instance of SoundboardSoundResponse from a dict
soundboard_sound_response_from_dict = SoundboardSoundResponse.from_dict(soundboard_sound_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


