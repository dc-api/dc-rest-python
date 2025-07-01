# ListAutoModerationRules200ResponseInner


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
from dc_rest.models.list_auto_moderation_rules200_response_inner import ListAutoModerationRules200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of ListAutoModerationRules200ResponseInner from a JSON string
list_auto_moderation_rules200_response_inner_instance = ListAutoModerationRules200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(ListAutoModerationRules200ResponseInner.to_json())

# convert the object into a dict
list_auto_moderation_rules200_response_inner_dict = list_auto_moderation_rules200_response_inner_instance.to_dict()
# create an instance of ListAutoModerationRules200ResponseInner from a dict
list_auto_moderation_rules200_response_inner_from_dict = ListAutoModerationRules200ResponseInner.from_dict(list_auto_moderation_rules200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


