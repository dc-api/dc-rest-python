# GuildOnboardingResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**guild_id** | **str** |  | 
**prompts** | [**List[OnboardingPromptResponse]**](OnboardingPromptResponse.md) |  | 
**default_channel_ids** | **List[str]** |  | 
**enabled** | **bool** |  | 

## Example

```python
from dc_rest.models.guild_onboarding_response import GuildOnboardingResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GuildOnboardingResponse from a JSON string
guild_onboarding_response_instance = GuildOnboardingResponse.from_json(json)
# print the JSON string representation of the object
print(GuildOnboardingResponse.to_json())

# convert the object into a dict
guild_onboarding_response_dict = guild_onboarding_response_instance.to_dict()
# create an instance of GuildOnboardingResponse from a dict
guild_onboarding_response_from_dict = GuildOnboardingResponse.from_dict(guild_onboarding_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


