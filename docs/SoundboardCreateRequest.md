# SoundboardCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**volume** | **float** |  | [optional] 
**emoji_id** | **str** |  | [optional] 
**emoji_name** | **str** |  | [optional] 
**sound** | **str** |  | 

## Example

```python
from dc_rest.models.soundboard_create_request import SoundboardCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SoundboardCreateRequest from a JSON string
soundboard_create_request_instance = SoundboardCreateRequest.from_json(json)
# print the JSON string representation of the object
print(SoundboardCreateRequest.to_json())

# convert the object into a dict
soundboard_create_request_dict = soundboard_create_request_instance.to_dict()
# create an instance of SoundboardCreateRequest from a dict
soundboard_create_request_from_dict = SoundboardCreateRequest.from_dict(soundboard_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


