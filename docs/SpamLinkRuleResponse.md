# SpamLinkRuleResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**guild_id** | **str** |  | 
**creator_id** | **str** |  | 
**name** | **str** |  | 
**event_type** | **int** |  | 
**actions** | [**List[DefaultKeywordRuleResponseActionsInner]**](DefaultKeywordRuleResponseActionsInner.md) |  | 
**trigger_type** | **int** |  | 
**enabled** | **bool** |  | [optional] 
**exempt_roles** | **List[str]** |  | [optional] 
**exempt_channels** | **List[str]** |  | [optional] 
**trigger_metadata** | **object** |  | 

## Example

```python
from dc_rest.models.spam_link_rule_response import SpamLinkRuleResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SpamLinkRuleResponse from a JSON string
spam_link_rule_response_instance = SpamLinkRuleResponse.from_json(json)
# print the JSON string representation of the object
print(SpamLinkRuleResponse.to_json())

# convert the object into a dict
spam_link_rule_response_dict = spam_link_rule_response_instance.to_dict()
# create an instance of SpamLinkRuleResponse from a dict
spam_link_rule_response_from_dict = SpamLinkRuleResponse.from_dict(spam_link_rule_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


