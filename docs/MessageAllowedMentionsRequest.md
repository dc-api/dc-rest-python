# MessageAllowedMentionsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**parse** | **List[Optional[str]]** |  | [optional] 
**users** | **List[Optional[str]]** |  | [optional] 
**roles** | **List[Optional[str]]** |  | [optional] 
**replied_user** | **bool** |  | [optional] 

## Example

```python
from dc_rest.models.message_allowed_mentions_request import MessageAllowedMentionsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MessageAllowedMentionsRequest from a JSON string
message_allowed_mentions_request_instance = MessageAllowedMentionsRequest.from_json(json)
# print the JSON string representation of the object
print(MessageAllowedMentionsRequest.to_json())

# convert the object into a dict
message_allowed_mentions_request_dict = message_allowed_mentions_request_instance.to_dict()
# create an instance of MessageAllowedMentionsRequest from a dict
message_allowed_mentions_request_from_dict = MessageAllowedMentionsRequest.from_dict(message_allowed_mentions_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


