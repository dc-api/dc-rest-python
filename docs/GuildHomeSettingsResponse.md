# GuildHomeSettingsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**guild_id** | **str** |  | 
**enabled** | **bool** |  | 
**welcome_message** | [**WelcomeMessageResponse**](WelcomeMessageResponse.md) |  | [optional] 
**new_member_actions** | [**List[Optional[NewMemberActionResponse]]**](NewMemberActionResponse.md) |  | [optional] 
**resource_channels** | [**List[Optional[ResourceChannelResponse]]**](ResourceChannelResponse.md) |  | [optional] 

## Example

```python
from dc_rest.models.guild_home_settings_response import GuildHomeSettingsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GuildHomeSettingsResponse from a JSON string
guild_home_settings_response_instance = GuildHomeSettingsResponse.from_json(json)
# print the JSON string representation of the object
print(GuildHomeSettingsResponse.to_json())

# convert the object into a dict
guild_home_settings_response_dict = guild_home_settings_response_instance.to_dict()
# create an instance of GuildHomeSettingsResponse from a dict
guild_home_settings_response_from_dict = GuildHomeSettingsResponse.from_dict(guild_home_settings_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


