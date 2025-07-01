# MentionSpamRuleResponse


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
**trigger_metadata** | [**MentionSpamTriggerMetadataResponse**](MentionSpamTriggerMetadataResponse.md) |  | 

## Example

```python
from dc_rest.models.mention_spam_rule_response import MentionSpamRuleResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MentionSpamRuleResponse from a JSON string
mention_spam_rule_response_instance = MentionSpamRuleResponse.from_json(json)
# print the JSON string representation of the object
print(MentionSpamRuleResponse.to_json())

# convert the object into a dict
mention_spam_rule_response_dict = mention_spam_rule_response_instance.to_dict()
# create an instance of MentionSpamRuleResponse from a dict
mention_spam_rule_response_from_dict = MentionSpamRuleResponse.from_dict(mention_spam_rule_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


