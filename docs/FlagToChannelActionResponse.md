# FlagToChannelActionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **int** |  | 
**metadata** | [**FlagToChannelActionMetadataResponse**](FlagToChannelActionMetadataResponse.md) |  | 

## Example

```python
from dc_rest.models.flag_to_channel_action_response import FlagToChannelActionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FlagToChannelActionResponse from a JSON string
flag_to_channel_action_response_instance = FlagToChannelActionResponse.from_json(json)
# print the JSON string representation of the object
print(FlagToChannelActionResponse.to_json())

# convert the object into a dict
flag_to_channel_action_response_dict = flag_to_channel_action_response_instance.to_dict()
# create an instance of FlagToChannelActionResponse from a dict
flag_to_channel_action_response_from_dict = FlagToChannelActionResponse.from_dict(flag_to_channel_action_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


