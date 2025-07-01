# FollowChannelRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**webhook_channel_id** | **str** |  | 

## Example

```python
from dc_rest.models.follow_channel_request import FollowChannelRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FollowChannelRequest from a JSON string
follow_channel_request_instance = FollowChannelRequest.from_json(json)
# print the JSON string representation of the object
print(FollowChannelRequest.to_json())

# convert the object into a dict
follow_channel_request_dict = follow_channel_request_instance.to_dict()
# create an instance of FollowChannelRequest from a dict
follow_channel_request_from_dict = FollowChannelRequest.from_dict(follow_channel_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


