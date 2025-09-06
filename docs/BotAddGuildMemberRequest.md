# BotAddGuildMemberRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nick** | **str** |  | [optional] 
**roles** | **List[str]** |  | [optional] 
**mute** | **bool** |  | [optional] 
**deaf** | **bool** |  | [optional] 
**access_token** | **str** |  | 
**flags** | **int** |  | [optional] 

## Example

```python
from dc_rest.models.bot_add_guild_member_request import BotAddGuildMemberRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BotAddGuildMemberRequest from a JSON string
bot_add_guild_member_request_instance = BotAddGuildMemberRequest.from_json(json)
# print the JSON string representation of the object
print(BotAddGuildMemberRequest.to_json())

# convert the object into a dict
bot_add_guild_member_request_dict = bot_add_guild_member_request_instance.to_dict()
# create an instance of BotAddGuildMemberRequest from a dict
bot_add_guild_member_request_from_dict = BotAddGuildMemberRequest.from_dict(bot_add_guild_member_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


