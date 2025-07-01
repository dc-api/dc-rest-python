# InviteChannelResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**type** | **int** |  | 
**name** | **str** |  | [optional] 
**icon** | **str** |  | [optional] 
**recipients** | [**List[InviteChannelRecipientResponse]**](InviteChannelRecipientResponse.md) |  | [optional] 

## Example

```python
from dc_rest.models.invite_channel_response import InviteChannelResponse

# TODO update the JSON string below
json = "{}"
# create an instance of InviteChannelResponse from a JSON string
invite_channel_response_instance = InviteChannelResponse.from_json(json)
# print the JSON string representation of the object
print(InviteChannelResponse.to_json())

# convert the object into a dict
invite_channel_response_dict = invite_channel_response_instance.to_dict()
# create an instance of InviteChannelResponse from a dict
invite_channel_response_from_dict = InviteChannelResponse.from_dict(invite_channel_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


