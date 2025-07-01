# WidgetSettingsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** |  | 
**channel_id** | **str** |  | [optional] 

## Example

```python
from dc_rest.models.widget_settings_response import WidgetSettingsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of WidgetSettingsResponse from a JSON string
widget_settings_response_instance = WidgetSettingsResponse.from_json(json)
# print the JSON string representation of the object
print(WidgetSettingsResponse.to_json())

# convert the object into a dict
widget_settings_response_dict = widget_settings_response_instance.to_dict()
# create an instance of WidgetSettingsResponse from a dict
widget_settings_response_from_dict = WidgetSettingsResponse.from_dict(widget_settings_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


