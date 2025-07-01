# SettingsEmojiResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**animated** | **bool** |  | [optional] 

## Example

```python
from dc_rest.models.settings_emoji_response import SettingsEmojiResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SettingsEmojiResponse from a JSON string
settings_emoji_response_instance = SettingsEmojiResponse.from_json(json)
# print the JSON string representation of the object
print(SettingsEmojiResponse.to_json())

# convert the object into a dict
settings_emoji_response_dict = settings_emoji_response_instance.to_dict()
# create an instance of SettingsEmojiResponse from a dict
settings_emoji_response_from_dict = SettingsEmojiResponse.from_dict(settings_emoji_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


