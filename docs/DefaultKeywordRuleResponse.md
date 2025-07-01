# DefaultKeywordRuleResponse


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
**trigger_metadata** | [**DefaultKeywordListTriggerMetadataResponse**](DefaultKeywordListTriggerMetadataResponse.md) |  | 

## Example

```python
from dc_rest.models.default_keyword_rule_response import DefaultKeywordRuleResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DefaultKeywordRuleResponse from a JSON string
default_keyword_rule_response_instance = DefaultKeywordRuleResponse.from_json(json)
# print the JSON string representation of the object
print(DefaultKeywordRuleResponse.to_json())

# convert the object into a dict
default_keyword_rule_response_dict = default_keyword_rule_response_instance.to_dict()
# create an instance of DefaultKeywordRuleResponse from a dict
default_keyword_rule_response_from_dict = DefaultKeywordRuleResponse.from_dict(default_keyword_rule_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


