# UpdateGuildEmojiRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**roles** | **List[Optional[str]]** |  | [optional] 

## Example

```python
from dc_rest.models.update_guild_emoji_request import UpdateGuildEmojiRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateGuildEmojiRequest from a JSON string
update_guild_emoji_request_instance = UpdateGuildEmojiRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateGuildEmojiRequest.to_json())

# convert the object into a dict
update_guild_emoji_request_dict = update_guild_emoji_request_instance.to_dict()
# create an instance of UpdateGuildEmojiRequest from a dict
update_guild_emoji_request_from_dict = UpdateGuildEmojiRequest.from_dict(update_guild_emoji_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


