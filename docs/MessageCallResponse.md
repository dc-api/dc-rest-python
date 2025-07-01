# MessageCallResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ended_timestamp** | **datetime** |  | [optional] 
**participants** | **List[str]** |  | 

## Example

```python
from dc_rest.models.message_call_response import MessageCallResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MessageCallResponse from a JSON string
message_call_response_instance = MessageCallResponse.from_json(json)
# print the JSON string representation of the object
print(MessageCallResponse.to_json())

# convert the object into a dict
message_call_response_dict = message_call_response_instance.to_dict()
# create an instance of MessageCallResponse from a dict
message_call_response_from_dict = MessageCallResponse.from_dict(message_call_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


