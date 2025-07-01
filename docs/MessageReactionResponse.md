# MessageReactionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**emoji** | [**MessageReactionEmojiResponse**](MessageReactionEmojiResponse.md) |  | 
**count** | **int** |  | 
**count_details** | [**MessageReactionCountDetailsResponse**](MessageReactionCountDetailsResponse.md) |  | 
**burst_colors** | **List[str]** |  | 
**me_burst** | **bool** |  | 
**me** | **bool** |  | 

## Example

```python
from dc_rest.models.message_reaction_response import MessageReactionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MessageReactionResponse from a JSON string
message_reaction_response_instance = MessageReactionResponse.from_json(json)
# print the JSON string representation of the object
print(MessageReactionResponse.to_json())

# convert the object into a dict
message_reaction_response_dict = message_reaction_response_instance.to_dict()
# create an instance of MessageReactionResponse from a dict
message_reaction_response_from_dict = MessageReactionResponse.from_dict(message_reaction_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


