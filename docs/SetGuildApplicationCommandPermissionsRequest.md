# SetGuildApplicationCommandPermissionsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**permissions** | [**List[ApplicationCommandPermission]**](ApplicationCommandPermission.md) |  | [optional] 

## Example

```python
from dc_rest.models.set_guild_application_command_permissions_request import SetGuildApplicationCommandPermissionsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SetGuildApplicationCommandPermissionsRequest from a JSON string
set_guild_application_command_permissions_request_instance = SetGuildApplicationCommandPermissionsRequest.from_json(json)
# print the JSON string representation of the object
print(SetGuildApplicationCommandPermissionsRequest.to_json())

# convert the object into a dict
set_guild_application_command_permissions_request_dict = set_guild_application_command_permissions_request_instance.to_dict()
# create an instance of SetGuildApplicationCommandPermissionsRequest from a dict
set_guild_application_command_permissions_request_from_dict = SetGuildApplicationCommandPermissionsRequest.from_dict(set_guild_application_command_permissions_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


