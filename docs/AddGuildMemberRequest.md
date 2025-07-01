# AddGuildMemberRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nick** | **str** |  | [optional] 
**roles** | **List[Optional[str]]** |  | [optional] 
**mute** | **bool** |  | [optional] 
**deaf** | **bool** |  | [optional] 
**access_token** | **str** |  | 
**flags** | **int** |  | [optional] 

## Example

```python
from dc_rest.models.add_guild_member_request import AddGuildMemberRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddGuildMemberRequest from a JSON string
add_guild_member_request_instance = AddGuildMemberRequest.from_json(json)
# print the JSON string representation of the object
print(AddGuildMemberRequest.to_json())

# convert the object into a dict
add_guild_member_request_dict = add_guild_member_request_instance.to_dict()
# create an instance of AddGuildMemberRequest from a dict
add_guild_member_request_from_dict = AddGuildMemberRequest.from_dict(add_guild_member_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


