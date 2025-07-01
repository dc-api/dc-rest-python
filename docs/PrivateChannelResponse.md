# PrivateChannelResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**type** | **int** |  | 
**last_message_id** | **str** |  | [optional] 
**flags** | **int** |  | 
**last_pin_timestamp** | **datetime** |  | [optional] 
**recipients** | [**List[UserResponse]**](UserResponse.md) |  | 

## Example

```python
from dc_rest.models.private_channel_response import PrivateChannelResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PrivateChannelResponse from a JSON string
private_channel_response_instance = PrivateChannelResponse.from_json(json)
# print the JSON string representation of the object
print(PrivateChannelResponse.to_json())

# convert the object into a dict
private_channel_response_dict = private_channel_response_instance.to_dict()
# create an instance of PrivateChannelResponse from a dict
private_channel_response_from_dict = PrivateChannelResponse.from_dict(private_channel_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


