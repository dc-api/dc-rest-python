# UpdateGuildMemberRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nick** | **str** |  | [optional] 
**roles** | **List[Optional[str]]** |  | [optional] 
**mute** | **bool** |  | [optional] 
**deaf** | **bool** |  | [optional] 
**channel_id** | **str** |  | [optional] 
**communication_disabled_until** | **datetime** |  | [optional] 
**flags** | **int** |  | [optional] 

## Example

```python
from dc_rest.models.update_guild_member_request import UpdateGuildMemberRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateGuildMemberRequest from a JSON string
update_guild_member_request_instance = UpdateGuildMemberRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateGuildMemberRequest.to_json())

# convert the object into a dict
update_guild_member_request_dict = update_guild_member_request_instance.to_dict()
# create an instance of UpdateGuildMemberRequest from a dict
update_guild_member_request_from_dict = UpdateGuildMemberRequest.from_dict(update_guild_member_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


