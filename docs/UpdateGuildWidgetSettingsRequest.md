# UpdateGuildWidgetSettingsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channel_id** | **str** |  | [optional] 
**enabled** | **bool** |  | [optional] 

## Example

```python
from dc_rest.models.update_guild_widget_settings_request import UpdateGuildWidgetSettingsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateGuildWidgetSettingsRequest from a JSON string
update_guild_widget_settings_request_instance = UpdateGuildWidgetSettingsRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateGuildWidgetSettingsRequest.to_json())

# convert the object into a dict
update_guild_widget_settings_request_dict = update_guild_widget_settings_request_instance.to_dict()
# create an instance of UpdateGuildWidgetSettingsRequest from a dict
update_guild_widget_settings_request_from_dict = UpdateGuildWidgetSettingsRequest.from_dict(update_guild_widget_settings_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


