# VoiceScheduledEventPatchRequestPartial


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**image** | **str** |  | [optional] 
**scheduled_start_time** | **datetime** |  | [optional] 
**scheduled_end_time** | **datetime** |  | [optional] 
**entity_type** | **int** |  | [optional] 
**privacy_level** | **object** |  | [optional] 
**channel_id** | **str** |  | [optional] 
**entity_metadata** | **object** |  | [optional] 

## Example

```python
from dc_rest.models.voice_scheduled_event_patch_request_partial import VoiceScheduledEventPatchRequestPartial

# TODO update the JSON string below
json = "{}"
# create an instance of VoiceScheduledEventPatchRequestPartial from a JSON string
voice_scheduled_event_patch_request_partial_instance = VoiceScheduledEventPatchRequestPartial.from_json(json)
# print the JSON string representation of the object
print(VoiceScheduledEventPatchRequestPartial.to_json())

# convert the object into a dict
voice_scheduled_event_patch_request_partial_dict = voice_scheduled_event_patch_request_partial_instance.to_dict()
# create an instance of VoiceScheduledEventPatchRequestPartial from a dict
voice_scheduled_event_patch_request_partial_from_dict = VoiceScheduledEventPatchRequestPartial.from_dict(voice_scheduled_event_patch_request_partial_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


