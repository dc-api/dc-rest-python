# DefaultReactionEmojiResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**emoji_id** | **str** |  | [optional] 
**emoji_name** | **str** |  | [optional] 

## Example

```python
from dc_rest.models.default_reaction_emoji_response import DefaultReactionEmojiResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DefaultReactionEmojiResponse from a JSON string
default_reaction_emoji_response_instance = DefaultReactionEmojiResponse.from_json(json)
# print the JSON string representation of the object
print(DefaultReactionEmojiResponse.to_json())

# convert the object into a dict
default_reaction_emoji_response_dict = default_reaction_emoji_response_instance.to_dict()
# create an instance of DefaultReactionEmojiResponse from a dict
default_reaction_emoji_response_from_dict = DefaultReactionEmojiResponse.from_dict(default_reaction_emoji_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


