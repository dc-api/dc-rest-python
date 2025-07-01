# BotAccountPatchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** |  | 
**avatar** | **str** |  | [optional] 
**banner** | **str** |  | [optional] 

## Example

```python
from dc_rest.models.bot_account_patch_request import BotAccountPatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BotAccountPatchRequest from a JSON string
bot_account_patch_request_instance = BotAccountPatchRequest.from_json(json)
# print the JSON string representation of the object
print(BotAccountPatchRequest.to_json())

# convert the object into a dict
bot_account_patch_request_dict = bot_account_patch_request_instance.to_dict()
# create an instance of BotAccountPatchRequest from a dict
bot_account_patch_request_from_dict = BotAccountPatchRequest.from_dict(bot_account_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


