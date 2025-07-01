# MessageReferenceRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**guild_id** | **str** |  | [optional] 
**channel_id** | **str** |  | [optional] 
**message_id** | **str** |  | 
**fail_if_not_exists** | **bool** |  | [optional] 
**type** | **object** |  | [optional] 

## Example

```python
from dc_rest.models.message_reference_request import MessageReferenceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MessageReferenceRequest from a JSON string
message_reference_request_instance = MessageReferenceRequest.from_json(json)
# print the JSON string representation of the object
print(MessageReferenceRequest.to_json())

# convert the object into a dict
message_reference_request_dict = message_reference_request_instance.to_dict()
# create an instance of MessageReferenceRequest from a dict
message_reference_request_from_dict = MessageReferenceRequest.from_dict(message_reference_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


