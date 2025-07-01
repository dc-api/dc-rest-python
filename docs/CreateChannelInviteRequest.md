# CreateChannelInviteRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_age** | **int** |  | [optional] 
**temporary** | **bool** |  | [optional] 
**max_uses** | **int** |  | [optional] 
**unique** | **bool** |  | [optional] 
**target_user_id** | **str** |  | [optional] 
**target_application_id** | **str** |  | [optional] 
**target_type** | **int** |  | [optional] 

## Example

```python
from dc_rest.models.create_channel_invite_request import CreateChannelInviteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateChannelInviteRequest from a JSON string
create_channel_invite_request_instance = CreateChannelInviteRequest.from_json(json)
# print the JSON string representation of the object
print(CreateChannelInviteRequest.to_json())

# convert the object into a dict
create_channel_invite_request_dict = create_channel_invite_request_instance.to_dict()
# create an instance of CreateChannelInviteRequest from a dict
create_channel_invite_request_from_dict = CreateChannelInviteRequest.from_dict(create_channel_invite_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


