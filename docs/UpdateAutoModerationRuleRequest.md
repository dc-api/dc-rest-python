# UpdateAutoModerationRuleRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**event_type** | **int** |  | [optional] 
**actions** | [**List[DefaultKeywordListUpsertRequestActionsInner]**](DefaultKeywordListUpsertRequestActionsInner.md) |  | [optional] 
**enabled** | **bool** |  | [optional] 
**exempt_roles** | **List[str]** |  | [optional] 
**exempt_channels** | **List[str]** |  | [optional] 
**trigger_type** | **int** |  | [optional] 
**trigger_metadata** | [**MentionSpamTriggerMetadata**](MentionSpamTriggerMetadata.md) |  | [optional] 

## Example

```python
from dc_rest.models.update_auto_moderation_rule_request import UpdateAutoModerationRuleRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateAutoModerationRuleRequest from a JSON string
update_auto_moderation_rule_request_instance = UpdateAutoModerationRuleRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateAutoModerationRuleRequest.to_json())

# convert the object into a dict
update_auto_moderation_rule_request_dict = update_auto_moderation_rule_request_instance.to_dict()
# create an instance of UpdateAutoModerationRuleRequest from a dict
update_auto_moderation_rule_request_from_dict = UpdateAutoModerationRuleRequest.from_dict(update_auto_moderation_rule_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


