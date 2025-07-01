# MentionSpamUpsertRequestPartial


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
from dc_rest.models.mention_spam_upsert_request_partial import MentionSpamUpsertRequestPartial

# TODO update the JSON string below
json = "{}"
# create an instance of MentionSpamUpsertRequestPartial from a JSON string
mention_spam_upsert_request_partial_instance = MentionSpamUpsertRequestPartial.from_json(json)
# print the JSON string representation of the object
print(MentionSpamUpsertRequestPartial.to_json())

# convert the object into a dict
mention_spam_upsert_request_partial_dict = mention_spam_upsert_request_partial_instance.to_dict()
# create an instance of MentionSpamUpsertRequestPartial from a dict
mention_spam_upsert_request_partial_from_dict = MentionSpamUpsertRequestPartial.from_dict(mention_spam_upsert_request_partial_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


