# CreateAutoModerationRuleRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**event_type** | **int** |  | 
**actions** | [**List[DefaultKeywordListUpsertRequestActionsInner]**](DefaultKeywordListUpsertRequestActionsInner.md) |  | [optional] 
**enabled** | **bool** |  | [optional] 
**exempt_roles** | **List[str]** |  | [optional] 
**exempt_channels** | **List[str]** |  | [optional] 
**trigger_type** | **int** |  | 
**trigger_metadata** | [**MentionSpamTriggerMetadata**](MentionSpamTriggerMetadata.md) |  | 

## Example

```python
from dc_rest.models.create_auto_moderation_rule_request import CreateAutoModerationRuleRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAutoModerationRuleRequest from a JSON string
create_auto_moderation_rule_request_instance = CreateAutoModerationRuleRequest.from_json(json)
# print the JSON string representation of the object
print(CreateAutoModerationRuleRequest.to_json())

# convert the object into a dict
create_auto_moderation_rule_request_dict = create_auto_moderation_rule_request_instance.to_dict()
# create an instance of CreateAutoModerationRuleRequest from a dict
create_auto_moderation_rule_request_from_dict = CreateAutoModerationRuleRequest.from_dict(create_auto_moderation_rule_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


