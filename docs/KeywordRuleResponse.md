# KeywordRuleResponse


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
**trigger_metadata** | [**KeywordTriggerMetadataResponse**](KeywordTriggerMetadataResponse.md) |  | 

## Example

```python
from dc_rest.models.keyword_rule_response import KeywordRuleResponse

# TODO update the JSON string below
json = "{}"
# create an instance of KeywordRuleResponse from a JSON string
keyword_rule_response_instance = KeywordRuleResponse.from_json(json)
# print the JSON string representation of the object
print(KeywordRuleResponse.to_json())

# convert the object into a dict
keyword_rule_response_dict = keyword_rule_response_instance.to_dict()
# create an instance of KeywordRuleResponse from a dict
keyword_rule_response_from_dict = KeywordRuleResponse.from_dict(keyword_rule_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


