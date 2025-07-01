# ChannelSelectComponentResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **int** |  | 
**id** | **int** |  | 
**custom_id** | **str** |  | 
**placeholder** | **str** |  | [optional] 
**min_values** | **int** |  | [optional] 
**max_values** | **int** |  | [optional] 
**disabled** | **bool** |  | [optional] 
**channel_types** | **List[int]** |  | [optional] 
**default_values** | [**List[ChannelSelectDefaultValueResponse]**](ChannelSelectDefaultValueResponse.md) |  | [optional] 

## Example

```python
from dc_rest.models.channel_select_component_response import ChannelSelectComponentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ChannelSelectComponentResponse from a JSON string
channel_select_component_response_instance = ChannelSelectComponentResponse.from_json(json)
# print the JSON string representation of the object
print(ChannelSelectComponentResponse.to_json())

# convert the object into a dict
channel_select_component_response_dict = channel_select_component_response_instance.to_dict()
# create an instance of ChannelSelectComponentResponse from a dict
channel_select_component_response_from_dict = ChannelSelectComponentResponse.from_dict(channel_select_component_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


