# DefaultKeywordRuleResponseActionsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **int** |  | 
**metadata** | [**UserCommunicationDisabledActionMetadataResponse**](UserCommunicationDisabledActionMetadataResponse.md) |  | 

## Example

```python
from dc_rest.models.default_keyword_rule_response_actions_inner import DefaultKeywordRuleResponseActionsInner

# TODO update the JSON string below
json = "{}"
# create an instance of DefaultKeywordRuleResponseActionsInner from a JSON string
default_keyword_rule_response_actions_inner_instance = DefaultKeywordRuleResponseActionsInner.from_json(json)
# print the JSON string representation of the object
print(DefaultKeywordRuleResponseActionsInner.to_json())

# convert the object into a dict
default_keyword_rule_response_actions_inner_dict = default_keyword_rule_response_actions_inner_instance.to_dict()
# create an instance of DefaultKeywordRuleResponseActionsInner from a dict
default_keyword_rule_response_actions_inner_from_dict = DefaultKeywordRuleResponseActionsInner.from_dict(default_keyword_rule_response_actions_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


