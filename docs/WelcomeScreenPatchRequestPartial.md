# WelcomeScreenPatchRequestPartial


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**welcome_channels** | [**List[GuildWelcomeChannel]**](GuildWelcomeChannel.md) |  | [optional] 
**enabled** | **bool** |  | [optional] 

## Example

```python
from dc_rest.models.welcome_screen_patch_request_partial import WelcomeScreenPatchRequestPartial

# TODO update the JSON string below
json = "{}"
# create an instance of WelcomeScreenPatchRequestPartial from a JSON string
welcome_screen_patch_request_partial_instance = WelcomeScreenPatchRequestPartial.from_json(json)
# print the JSON string representation of the object
print(WelcomeScreenPatchRequestPartial.to_json())

# convert the object into a dict
welcome_screen_patch_request_partial_dict = welcome_screen_patch_request_partial_instance.to_dict()
# create an instance of WelcomeScreenPatchRequestPartial from a dict
welcome_screen_patch_request_partial_from_dict = WelcomeScreenPatchRequestPartial.from_dict(welcome_screen_patch_request_partial_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


