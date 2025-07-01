# ChannelSelectDefaultValueResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**id** | **str** |  | 

## Example

```python
from dc_rest.models.channel_select_default_value_response import ChannelSelectDefaultValueResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ChannelSelectDefaultValueResponse from a JSON string
channel_select_default_value_response_instance = ChannelSelectDefaultValueResponse.from_json(json)
# print the JSON string representation of the object
print(ChannelSelectDefaultValueResponse.to_json())

# convert the object into a dict
channel_select_default_value_response_dict = channel_select_default_value_response_instance.to_dict()
# create an instance of ChannelSelectDefaultValueResponse from a dict
channel_select_default_value_response_from_dict = ChannelSelectDefaultValueResponse.from_dict(channel_select_default_value_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


