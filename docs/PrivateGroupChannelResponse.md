# PrivateGroupChannelResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**type** | **int** |  | 
**last_message_id** | **str** |  | [optional] 
**flags** | **int** |  | 
**last_pin_timestamp** | **datetime** |  | [optional] 
**recipients** | [**List[UserResponse]**](UserResponse.md) |  | 
**name** | **str** |  | [optional] 
**icon** | **str** |  | [optional] 
**owner_id** | **str** |  | [optional] 
**managed** | **bool** |  | [optional] 
**application_id** | **str** |  | [optional] 

## Example

```python
from dc_rest.models.private_group_channel_response import PrivateGroupChannelResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PrivateGroupChannelResponse from a JSON string
private_group_channel_response_instance = PrivateGroupChannelResponse.from_json(json)
# print the JSON string representation of the object
print(PrivateGroupChannelResponse.to_json())

# convert the object into a dict
private_group_channel_response_dict = private_group_channel_response_instance.to_dict()
# create an instance of PrivateGroupChannelResponse from a dict
private_group_channel_response_from_dict = PrivateGroupChannelResponse.from_dict(private_group_channel_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


