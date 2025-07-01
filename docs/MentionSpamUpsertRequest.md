# MentionSpamUpsertRequest


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
**trigger_metadata** | [**MentionSpamTriggerMetadata**](MentionSpamTriggerMetadata.md) |  | [optional] 

## Example

```python
from dc_rest.models.mention_spam_upsert_request import MentionSpamUpsertRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MentionSpamUpsertRequest from a JSON string
mention_spam_upsert_request_instance = MentionSpamUpsertRequest.from_json(json)
# print the JSON string representation of the object
print(MentionSpamUpsertRequest.to_json())

# convert the object into a dict
mention_spam_upsert_request_dict = mention_spam_upsert_request_instance.to_dict()
# create an instance of MentionSpamUpsertRequest from a dict
mention_spam_upsert_request_from_dict = MentionSpamUpsertRequest.from_dict(mention_spam_upsert_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


