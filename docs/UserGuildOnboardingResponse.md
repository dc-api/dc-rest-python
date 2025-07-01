# UserGuildOnboardingResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**guild_id** | **str** |  | 
**prompts** | [**List[OnboardingPromptResponse]**](OnboardingPromptResponse.md) |  | 
**default_channel_ids** | **List[str]** |  | 
**enabled** | **bool** |  | 

## Example

```python
from dc_rest.models.user_guild_onboarding_response import UserGuildOnboardingResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UserGuildOnboardingResponse from a JSON string
user_guild_onboarding_response_instance = UserGuildOnboardingResponse.from_json(json)
# print the JSON string representation of the object
print(UserGuildOnboardingResponse.to_json())

# convert the object into a dict
user_guild_onboarding_response_dict = user_guild_onboarding_response_instance.to_dict()
# create an instance of UserGuildOnboardingResponse from a dict
user_guild_onboarding_response_from_dict = UserGuildOnboardingResponse.from_dict(user_guild_onboarding_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


