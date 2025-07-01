# UpdateSelfVoiceStateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_to_speak_timestamp** | **datetime** |  | [optional] 
**suppress** | **bool** |  | [optional] 
**channel_id** | **str** |  | [optional] 

## Example

```python
from dc_rest.models.update_self_voice_state_request import UpdateSelfVoiceStateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateSelfVoiceStateRequest from a JSON string
update_self_voice_state_request_instance = UpdateSelfVoiceStateRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateSelfVoiceStateRequest.to_json())

# convert the object into a dict
update_self_voice_state_request_dict = update_self_voice_state_request_instance.to_dict()
# create an instance of UpdateSelfVoiceStateRequest from a dict
update_self_voice_state_request_from_dict = UpdateSelfVoiceStateRequest.from_dict(update_self_voice_state_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


