# UpdateDefaultReactionEmojiRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**emoji_id** | **str** |  | [optional] 
**emoji_name** | **str** |  | [optional] 

## Example

```python
from dc_rest.models.update_default_reaction_emoji_request import UpdateDefaultReactionEmojiRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateDefaultReactionEmojiRequest from a JSON string
update_default_reaction_emoji_request_instance = UpdateDefaultReactionEmojiRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateDefaultReactionEmojiRequest.to_json())

# convert the object into a dict
update_default_reaction_emoji_request_dict = update_default_reaction_emoji_request_instance.to_dict()
# create an instance of UpdateDefaultReactionEmojiRequest from a dict
update_default_reaction_emoji_request_from_dict = UpdateDefaultReactionEmojiRequest.from_dict(update_default_reaction_emoji_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


