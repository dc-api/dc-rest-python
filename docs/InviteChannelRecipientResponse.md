# InviteChannelRecipientResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** |  | 

## Example

```python
from dc_rest.models.invite_channel_recipient_response import InviteChannelRecipientResponse

# TODO update the JSON string below
json = "{}"
# create an instance of InviteChannelRecipientResponse from a JSON string
invite_channel_recipient_response_instance = InviteChannelRecipientResponse.from_json(json)
# print the JSON string representation of the object
print(InviteChannelRecipientResponse.to_json())

# convert the object into a dict
invite_channel_recipient_response_dict = invite_channel_recipient_response_instance.to_dict()
# create an instance of InviteChannelRecipientResponse from a dict
invite_channel_recipient_response_from_dict = InviteChannelRecipientResponse.from_dict(invite_channel_recipient_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


