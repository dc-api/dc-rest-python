# ChannelSelectComponentForModalRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **int** |  | 
**id** | **int** |  | [optional] 
**custom_id** | **str** |  | 
**placeholder** | **str** |  | [optional] 
**min_values** | **int** |  | [optional] 
**max_values** | **int** |  | [optional] 
**disabled** | **bool** |  | [optional] 
**required** | **bool** |  | [optional] 
**default_values** | [**List[ChannelSelectDefaultValue]**](ChannelSelectDefaultValue.md) |  | [optional] 
**channel_types** | **List[int]** |  | [optional] 

## Example

```python
from dc_rest.models.channel_select_component_for_modal_request import ChannelSelectComponentForModalRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ChannelSelectComponentForModalRequest from a JSON string
channel_select_component_for_modal_request_instance = ChannelSelectComponentForModalRequest.from_json(json)
# print the JSON string representation of the object
print(ChannelSelectComponentForModalRequest.to_json())

# convert the object into a dict
channel_select_component_for_modal_request_dict = channel_select_component_for_modal_request_instance.to_dict()
# create an instance of ChannelSelectComponentForModalRequest from a dict
channel_select_component_for_modal_request_from_dict = ChannelSelectComponentForModalRequest.from_dict(channel_select_component_for_modal_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


