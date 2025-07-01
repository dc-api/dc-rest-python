# FlagToChannelAction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **int** |  | 
**metadata** | [**FlagToChannelActionMetadata**](FlagToChannelActionMetadata.md) |  | 

## Example

```python
from dc_rest.models.flag_to_channel_action import FlagToChannelAction

# TODO update the JSON string below
json = "{}"
# create an instance of FlagToChannelAction from a JSON string
flag_to_channel_action_instance = FlagToChannelAction.from_json(json)
# print the JSON string representation of the object
print(FlagToChannelAction.to_json())

# convert the object into a dict
flag_to_channel_action_dict = flag_to_channel_action_instance.to_dict()
# create an instance of FlagToChannelAction from a dict
flag_to_channel_action_from_dict = FlagToChannelAction.from_dict(flag_to_channel_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


