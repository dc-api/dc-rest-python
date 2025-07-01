# MessageReferenceResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **object** |  | [optional] 
**channel_id** | **str** |  | 
**message_id** | **str** |  | [optional] 
**guild_id** | **str** |  | [optional] 

## Example

```python
from dc_rest.models.message_reference_response import MessageReferenceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MessageReferenceResponse from a JSON string
message_reference_response_instance = MessageReferenceResponse.from_json(json)
# print the JSON string representation of the object
print(MessageReferenceResponse.to_json())

# convert the object into a dict
message_reference_response_dict = message_reference_response_instance.to_dict()
# create an instance of MessageReferenceResponse from a dict
message_reference_response_from_dict = MessageReferenceResponse.from_dict(message_reference_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


