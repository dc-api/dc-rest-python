# MessageReactionCountDetailsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**burst** | **int** |  | 
**normal** | **int** |  | 

## Example

```python
from dc_rest.models.message_reaction_count_details_response import MessageReactionCountDetailsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MessageReactionCountDetailsResponse from a JSON string
message_reaction_count_details_response_instance = MessageReactionCountDetailsResponse.from_json(json)
# print the JSON string representation of the object
print(MessageReactionCountDetailsResponse.to_json())

# convert the object into a dict
message_reaction_count_details_response_dict = message_reaction_count_details_response_instance.to_dict()
# create an instance of MessageReactionCountDetailsResponse from a dict
message_reaction_count_details_response_from_dict = MessageReactionCountDetailsResponse.from_dict(message_reaction_count_details_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


