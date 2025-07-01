# OnboardingPromptOptionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**title** | **str** |  | 
**description** | **str** |  | 
**emoji** | [**SettingsEmojiResponse**](SettingsEmojiResponse.md) |  | 
**role_ids** | **List[str]** |  | 
**channel_ids** | **List[str]** |  | 

## Example

```python
from dc_rest.models.onboarding_prompt_option_response import OnboardingPromptOptionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of OnboardingPromptOptionResponse from a JSON string
onboarding_prompt_option_response_instance = OnboardingPromptOptionResponse.from_json(json)
# print the JSON string representation of the object
print(OnboardingPromptOptionResponse.to_json())

# convert the object into a dict
onboarding_prompt_option_response_dict = onboarding_prompt_option_response_instance.to_dict()
# create an instance of OnboardingPromptOptionResponse from a dict
onboarding_prompt_option_response_from_dict = OnboardingPromptOptionResponse.from_dict(onboarding_prompt_option_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


