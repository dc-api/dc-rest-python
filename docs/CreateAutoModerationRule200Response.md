# CreateAutoModerationRule200Response


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
from dc_rest.models.create_auto_moderation_rule200_response import CreateAutoModerationRule200Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAutoModerationRule200Response from a JSON string
create_auto_moderation_rule200_response_instance = CreateAutoModerationRule200Response.from_json(json)
# print the JSON string representation of the object
print(CreateAutoModerationRule200Response.to_json())

# convert the object into a dict
create_auto_moderation_rule200_response_dict = create_auto_moderation_rule200_response_instance.to_dict()
# create an instance of CreateAutoModerationRule200Response from a dict
create_auto_moderation_rule200_response_from_dict = CreateAutoModerationRule200Response.from_dict(create_auto_moderation_rule200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


