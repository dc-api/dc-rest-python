# FlagToChannelActionMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channel_id** | **str** |  | 

## Example

```python
from dc_rest.models.flag_to_channel_action_metadata import FlagToChannelActionMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of FlagToChannelActionMetadata from a JSON string
flag_to_channel_action_metadata_instance = FlagToChannelActionMetadata.from_json(json)
# print the JSON string representation of the object
print(FlagToChannelActionMetadata.to_json())

# convert the object into a dict
flag_to_channel_action_metadata_dict = flag_to_channel_action_metadata_instance.to_dict()
# create an instance of FlagToChannelActionMetadata from a dict
flag_to_channel_action_metadata_from_dict = FlagToChannelActionMetadata.from_dict(flag_to_channel_action_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


