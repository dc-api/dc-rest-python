# BotPartnerSdkTokenRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**external_user_id** | **str** |  | 
**preferred_global_name** | **str** |  | [optional] 

## Example

```python
from dc_rest.models.bot_partner_sdk_token_request import BotPartnerSdkTokenRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BotPartnerSdkTokenRequest from a JSON string
bot_partner_sdk_token_request_instance = BotPartnerSdkTokenRequest.from_json(json)
# print the JSON string representation of the object
print(BotPartnerSdkTokenRequest.to_json())

# convert the object into a dict
bot_partner_sdk_token_request_dict = bot_partner_sdk_token_request_instance.to_dict()
# create an instance of BotPartnerSdkTokenRequest from a dict
bot_partner_sdk_token_request_from_dict = BotPartnerSdkTokenRequest.from_dict(bot_partner_sdk_token_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


