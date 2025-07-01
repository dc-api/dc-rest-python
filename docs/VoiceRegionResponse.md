# VoiceRegionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**custom** | **bool** |  | 
**deprecated** | **bool** |  | 
**optimal** | **bool** |  | 

## Example

```python
from dc_rest.models.voice_region_response import VoiceRegionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of VoiceRegionResponse from a JSON string
voice_region_response_instance = VoiceRegionResponse.from_json(json)
# print the JSON string representation of the object
print(VoiceRegionResponse.to_json())

# convert the object into a dict
voice_region_response_dict = voice_region_response_instance.to_dict()
# create an instance of VoiceRegionResponse from a dict
voice_region_response_from_dict = VoiceRegionResponse.from_dict(voice_region_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


