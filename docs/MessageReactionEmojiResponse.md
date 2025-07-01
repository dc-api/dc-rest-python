# MessageReactionEmojiResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**animated** | **bool** |  | [optional] 

## Example

```python
from dc_rest.models.message_reaction_emoji_response import MessageReactionEmojiResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MessageReactionEmojiResponse from a JSON string
message_reaction_emoji_response_instance = MessageReactionEmojiResponse.from_json(json)
# print the JSON string representation of the object
print(MessageReactionEmojiResponse.to_json())

# convert the object into a dict
message_reaction_emoji_response_dict = message_reaction_emoji_response_instance.to_dict()
# create an instance of MessageReactionEmojiResponse from a dict
message_reaction_emoji_response_from_dict = MessageReactionEmojiResponse.from_dict(message_reaction_emoji_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


