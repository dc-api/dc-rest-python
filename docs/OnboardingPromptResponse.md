# OnboardingPromptResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**title** | **str** |  | 
**options** | [**List[OnboardingPromptOptionResponse]**](OnboardingPromptOptionResponse.md) |  | 
**single_select** | **bool** |  | 
**required** | **bool** |  | 
**in_onboarding** | **bool** |  | 
**type** | **int** |  | 

## Example

```python
from dc_rest.models.onboarding_prompt_response import OnboardingPromptResponse

# TODO update the JSON string below
json = "{}"
# create an instance of OnboardingPromptResponse from a JSON string
onboarding_prompt_response_instance = OnboardingPromptResponse.from_json(json)
# print the JSON string representation of the object
print(OnboardingPromptResponse.to_json())

# convert the object into a dict
onboarding_prompt_response_dict = onboarding_prompt_response_instance.to_dict()
# create an instance of OnboardingPromptResponse from a dict
onboarding_prompt_response_from_dict = OnboardingPromptResponse.from_dict(onboarding_prompt_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


