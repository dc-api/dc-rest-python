# PinnedMessagesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[PinnedMessageResponse]**](PinnedMessageResponse.md) |  | [optional] 
**has_more** | **bool** |  | 

## Example

```python
from dc_rest.models.pinned_messages_response import PinnedMessagesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PinnedMessagesResponse from a JSON string
pinned_messages_response_instance = PinnedMessagesResponse.from_json(json)
# print the JSON string representation of the object
print(PinnedMessagesResponse.to_json())

# convert the object into a dict
pinned_messages_response_dict = pinned_messages_response_instance.to_dict()
# create an instance of PinnedMessagesResponse from a dict
pinned_messages_response_from_dict = PinnedMessagesResponse.from_dict(pinned_messages_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


