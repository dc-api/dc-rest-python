# PinnedMessageResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pinned_at** | **datetime** |  | 
**message** | [**MessageResponse**](MessageResponse.md) |  | 

## Example

```python
from dc_rest.models.pinned_message_response import PinnedMessageResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PinnedMessageResponse from a JSON string
pinned_message_response_instance = PinnedMessageResponse.from_json(json)
# print the JSON string representation of the object
print(PinnedMessageResponse.to_json())

# convert the object into a dict
pinned_message_response_dict = pinned_message_response_instance.to_dict()
# create an instance of PinnedMessageResponse from a dict
pinned_message_response_from_dict = PinnedMessageResponse.from_dict(pinned_message_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


