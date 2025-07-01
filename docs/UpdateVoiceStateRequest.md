# UpdateVoiceStateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**suppress** | **bool** |  | [optional] 
**channel_id** | **str** |  | [optional] 

## Example

```python
from dc_rest.models.update_voice_state_request import UpdateVoiceStateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateVoiceStateRequest from a JSON string
update_voice_state_request_instance = UpdateVoiceStateRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateVoiceStateRequest.to_json())

# convert the object into a dict
update_voice_state_request_dict = update_voice_state_request_instance.to_dict()
# create an instance of UpdateVoiceStateRequest from a dict
update_voice_state_request_from_dict = UpdateVoiceStateRequest.from_dict(update_voice_state_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


