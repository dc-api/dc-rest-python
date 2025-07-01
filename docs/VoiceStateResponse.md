# VoiceStateResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channel_id** | **str** |  | [optional] 
**deaf** | **bool** |  | 
**guild_id** | **str** |  | [optional] 
**member** | [**GuildMemberResponse**](GuildMemberResponse.md) |  | [optional] 
**mute** | **bool** |  | 
**request_to_speak_timestamp** | **datetime** |  | [optional] 
**suppress** | **bool** |  | 
**self_stream** | **bool** |  | [optional] 
**self_deaf** | **bool** |  | 
**self_mute** | **bool** |  | 
**self_video** | **bool** |  | 
**session_id** | **str** |  | 
**user_id** | **str** |  | 

## Example

```python
from dc_rest.models.voice_state_response import VoiceStateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of VoiceStateResponse from a JSON string
voice_state_response_instance = VoiceStateResponse.from_json(json)
# print the JSON string representation of the object
print(VoiceStateResponse.to_json())

# convert the object into a dict
voice_state_response_dict = voice_state_response_instance.to_dict()
# create an instance of VoiceStateResponse from a dict
voice_state_response_from_dict = VoiceStateResponse.from_dict(voice_state_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


