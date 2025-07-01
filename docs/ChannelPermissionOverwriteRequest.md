# ChannelPermissionOverwriteRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**type** | **int** |  | [optional] 
**allow** | **int** |  | [optional] 
**deny** | **int** |  | [optional] 

## Example

```python
from dc_rest.models.channel_permission_overwrite_request import ChannelPermissionOverwriteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ChannelPermissionOverwriteRequest from a JSON string
channel_permission_overwrite_request_instance = ChannelPermissionOverwriteRequest.from_json(json)
# print the JSON string representation of the object
print(ChannelPermissionOverwriteRequest.to_json())

# convert the object into a dict
channel_permission_overwrite_request_dict = channel_permission_overwrite_request_instance.to_dict()
# create an instance of ChannelPermissionOverwriteRequest from a dict
channel_permission_overwrite_request_from_dict = ChannelPermissionOverwriteRequest.from_dict(channel_permission_overwrite_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


