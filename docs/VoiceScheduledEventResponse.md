# VoiceScheduledEventResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**guild_id** | **str** |  | 
**name** | **str** |  | 
**description** | **str** |  | [optional] 
**channel_id** | **str** |  | [optional] 
**creator_id** | **str** |  | [optional] 
**creator** | [**UserResponse**](UserResponse.md) |  | [optional] 
**image** | **str** |  | [optional] 
**scheduled_start_time** | **datetime** |  | 
**scheduled_end_time** | **datetime** |  | [optional] 
**status** | **int** |  | 
**entity_type** | **int** |  | 
**entity_id** | **str** |  | [optional] 
**user_count** | **int** |  | [optional] 
**privacy_level** | **object** |  | 
**user_rsvp** | [**ScheduledEventUserResponse**](ScheduledEventUserResponse.md) |  | [optional] 
**entity_metadata** | **object** |  | [optional] 

## Example

```python
from dc_rest.models.voice_scheduled_event_response import VoiceScheduledEventResponse

# TODO update the JSON string below
json = "{}"
# create an instance of VoiceScheduledEventResponse from a JSON string
voice_scheduled_event_response_instance = VoiceScheduledEventResponse.from_json(json)
# print the JSON string representation of the object
print(VoiceScheduledEventResponse.to_json())

# convert the object into a dict
voice_scheduled_event_response_dict = voice_scheduled_event_response_instance.to_dict()
# create an instance of VoiceScheduledEventResponse from a dict
voice_scheduled_event_response_from_dict = VoiceScheduledEventResponse.from_dict(voice_scheduled_event_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


