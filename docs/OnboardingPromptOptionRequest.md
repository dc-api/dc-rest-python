# OnboardingPromptOptionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**title** | **str** |  | 
**description** | **str** |  | [optional] 
**emoji_id** | **str** |  | [optional] 
**emoji_name** | **str** |  | [optional] 
**emoji_animated** | **bool** |  | [optional] 
**role_ids** | **List[str]** |  | [optional] 
**channel_ids** | **List[str]** |  | [optional] 

## Example

```python
from dc_rest.models.onboarding_prompt_option_request import OnboardingPromptOptionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OnboardingPromptOptionRequest from a JSON string
onboarding_prompt_option_request_instance = OnboardingPromptOptionRequest.from_json(json)
# print the JSON string representation of the object
print(OnboardingPromptOptionRequest.to_json())

# convert the object into a dict
onboarding_prompt_option_request_dict = onboarding_prompt_option_request_instance.to_dict()
# create an instance of OnboardingPromptOptionRequest from a dict
onboarding_prompt_option_request_from_dict = OnboardingPromptOptionRequest.from_dict(onboarding_prompt_option_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


