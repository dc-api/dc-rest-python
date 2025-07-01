# ChannelFollowerResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channel_id** | **str** |  | 
**webhook_id** | **str** |  | 

## Example

```python
from dc_rest.models.channel_follower_response import ChannelFollowerResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ChannelFollowerResponse from a JSON string
channel_follower_response_instance = ChannelFollowerResponse.from_json(json)
# print the JSON string representation of the object
print(ChannelFollowerResponse.to_json())

# convert the object into a dict
channel_follower_response_dict = channel_follower_response_instance.to_dict()
# create an instance of ChannelFollowerResponse from a dict
channel_follower_response_from_dict = ChannelFollowerResponse.from_dict(channel_follower_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


