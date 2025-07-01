# UpdateGuildOnboardingRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**prompts** | [**List[UpdateOnboardingPromptRequest]**](UpdateOnboardingPromptRequest.md) |  | [optional] 
**enabled** | **bool** |  | [optional] 
**default_channel_ids** | **List[str]** |  | [optional] 
**mode** | **int** |  | [optional] 

## Example

```python
from dc_rest.models.update_guild_onboarding_request import UpdateGuildOnboardingRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateGuildOnboardingRequest from a JSON string
update_guild_onboarding_request_instance = UpdateGuildOnboardingRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateGuildOnboardingRequest.to_json())

# convert the object into a dict
update_guild_onboarding_request_dict = update_guild_onboarding_request_instance.to_dict()
# create an instance of UpdateGuildOnboardingRequest from a dict
update_guild_onboarding_request_from_dict = UpdateGuildOnboardingRequest.from_dict(update_guild_onboarding_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


