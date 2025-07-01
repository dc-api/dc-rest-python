# CreateGuildEmojiRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**image** | **str** |  | 
**roles** | **List[Optional[str]]** |  | [optional] 

## Example

```python
from dc_rest.models.create_guild_emoji_request import CreateGuildEmojiRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateGuildEmojiRequest from a JSON string
create_guild_emoji_request_instance = CreateGuildEmojiRequest.from_json(json)
# print the JSON string representation of the object
print(CreateGuildEmojiRequest.to_json())

# convert the object into a dict
create_guild_emoji_request_dict = create_guild_emoji_request_instance.to_dict()
# create an instance of CreateGuildEmojiRequest from a dict
create_guild_emoji_request_from_dict = CreateGuildEmojiRequest.from_dict(create_guild_emoji_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


