# UpdateVoiceStateRequestPartial


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**suppress** | **bool** |  | [optional] 
**channel_id** | **str** |  | [optional] 

## Example

```python
from dc_rest.models.update_voice_state_request_partial import UpdateVoiceStateRequestPartial

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateVoiceStateRequestPartial from a JSON string
update_voice_state_request_partial_instance = UpdateVoiceStateRequestPartial.from_json(json)
# print the JSON string representation of the object
print(UpdateVoiceStateRequestPartial.to_json())

# convert the object into a dict
update_voice_state_request_partial_dict = update_voice_state_request_partial_instance.to_dict()
# create an instance of UpdateVoiceStateRequestPartial from a dict
update_voice_state_request_partial_from_dict = UpdateVoiceStateRequestPartial.from_dict(update_voice_state_request_partial_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


