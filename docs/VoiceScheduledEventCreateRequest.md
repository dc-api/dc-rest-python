# VoiceScheduledEventCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**description** | **str** |  | [optional] 
**image** | **str** |  | [optional] 
**scheduled_start_time** | **datetime** |  | 
**scheduled_end_time** | **datetime** |  | [optional] 
**privacy_level** | **object** |  | 
**entity_type** | **int** |  | 
**channel_id** | **str** |  | [optional] 
**entity_metadata** | **object** |  | [optional] 

## Example

```python
from dc_rest.models.voice_scheduled_event_create_request import VoiceScheduledEventCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of VoiceScheduledEventCreateRequest from a JSON string
voice_scheduled_event_create_request_instance = VoiceScheduledEventCreateRequest.from_json(json)
# print the JSON string representation of the object
print(VoiceScheduledEventCreateRequest.to_json())

# convert the object into a dict
voice_scheduled_event_create_request_dict = voice_scheduled_event_create_request_instance.to_dict()
# create an instance of VoiceScheduledEventCreateRequest from a dict
voice_scheduled_event_create_request_from_dict = VoiceScheduledEventCreateRequest.from_dict(voice_scheduled_event_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


