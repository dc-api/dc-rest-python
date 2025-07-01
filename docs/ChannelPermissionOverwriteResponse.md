# ChannelPermissionOverwriteResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**type** | **int** |  | 
**allow** | **str** |  | 
**deny** | **str** |  | 

## Example

```python
from dc_rest.models.channel_permission_overwrite_response import ChannelPermissionOverwriteResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ChannelPermissionOverwriteResponse from a JSON string
channel_permission_overwrite_response_instance = ChannelPermissionOverwriteResponse.from_json(json)
# print the JSON string representation of the object
print(ChannelPermissionOverwriteResponse.to_json())

# convert the object into a dict
channel_permission_overwrite_response_dict = channel_permission_overwrite_response_instance.to_dict()
# create an instance of ChannelPermissionOverwriteResponse from a dict
channel_permission_overwrite_response_from_dict = ChannelPermissionOverwriteResponse.from_dict(channel_permission_overwrite_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


