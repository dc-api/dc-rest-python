# UpdateOnboardingPromptRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | 
**options** | [**List[OnboardingPromptOptionRequest]**](OnboardingPromptOptionRequest.md) |  | 
**single_select** | **bool** |  | [optional] 
**required** | **bool** |  | [optional] 
**in_onboarding** | **bool** |  | [optional] 
**type** | **int** |  | [optional] 
**id** | **str** |  | 

## Example

```python
from dc_rest.models.update_onboarding_prompt_request import UpdateOnboardingPromptRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateOnboardingPromptRequest from a JSON string
update_onboarding_prompt_request_instance = UpdateOnboardingPromptRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateOnboardingPromptRequest.to_json())

# convert the object into a dict
update_onboarding_prompt_request_dict = update_onboarding_prompt_request_instance.to_dict()
# create an instance of UpdateOnboardingPromptRequest from a dict
update_onboarding_prompt_request_from_dict = UpdateOnboardingPromptRequest.from_dict(update_onboarding_prompt_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


