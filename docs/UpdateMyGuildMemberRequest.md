# UpdateMyGuildMemberRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nick** | **str** |  | [optional] 

## Example

```python
from dc_rest.models.update_my_guild_member_request import UpdateMyGuildMemberRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateMyGuildMemberRequest from a JSON string
update_my_guild_member_request_instance = UpdateMyGuildMemberRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateMyGuildMemberRequest.to_json())

# convert the object into a dict
update_my_guild_member_request_dict = update_my_guild_member_request_instance.to_dict()
# create an instance of UpdateMyGuildMemberRequest from a dict
update_my_guild_member_request_from_dict = UpdateMyGuildMemberRequest.from_dict(update_my_guild_member_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


