# ResourceChannelResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channel_id** | **str** |  | 
**title** | **str** |  | 
**emoji** | [**SettingsEmojiResponse**](SettingsEmojiResponse.md) |  | [optional] 
**icon** | **str** |  | [optional] 
**description** | **str** |  | 

## Example

```python
from dc_rest.models.resource_channel_response import ResourceChannelResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceChannelResponse from a JSON string
resource_channel_response_instance = ResourceChannelResponse.from_json(json)
# print the JSON string representation of the object
print(ResourceChannelResponse.to_json())

# convert the object into a dict
resource_channel_response_dict = resource_channel_response_instance.to_dict()
# create an instance of ResourceChannelResponse from a dict
resource_channel_response_from_dict = ResourceChannelResponse.from_dict(resource_channel_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


