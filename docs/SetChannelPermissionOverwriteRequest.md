# SetChannelPermissionOverwriteRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **int** |  | [optional] 
**allow** | **int** |  | [optional] 
**deny** | **int** |  | [optional] 

## Example

```python
from dc_rest.models.set_channel_permission_overwrite_request import SetChannelPermissionOverwriteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SetChannelPermissionOverwriteRequest from a JSON string
set_channel_permission_overwrite_request_instance = SetChannelPermissionOverwriteRequest.from_json(json)
# print the JSON string representation of the object
print(SetChannelPermissionOverwriteRequest.to_json())

# convert the object into a dict
set_channel_permission_overwrite_request_dict = set_channel_permission_overwrite_request_instance.to_dict()
# create an instance of SetChannelPermissionOverwriteRequest from a dict
set_channel_permission_overwrite_request_from_dict = SetChannelPermissionOverwriteRequest.from_dict(set_channel_permission_overwrite_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


