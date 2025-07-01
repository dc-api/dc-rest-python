# SoundboardPatchRequestPartial


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**volume** | **float** |  | [optional] 
**emoji_id** | **str** |  | [optional] 
**emoji_name** | **str** |  | [optional] 

## Example

```python
from dc_rest.models.soundboard_patch_request_partial import SoundboardPatchRequestPartial

# TODO update the JSON string below
json = "{}"
# create an instance of SoundboardPatchRequestPartial from a JSON string
soundboard_patch_request_partial_instance = SoundboardPatchRequestPartial.from_json(json)
# print the JSON string representation of the object
print(SoundboardPatchRequestPartial.to_json())

# convert the object into a dict
soundboard_patch_request_partial_dict = soundboard_patch_request_partial_instance.to_dict()
# create an instance of SoundboardPatchRequestPartial from a dict
soundboard_patch_request_partial_from_dict = SoundboardPatchRequestPartial.from_dict(soundboard_patch_request_partial_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


