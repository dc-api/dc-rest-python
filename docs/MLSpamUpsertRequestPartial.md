# MLSpamUpsertRequestPartial


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
**trigger_metadata** | **object** |  | [optional] 

## Example

```python
from dc_rest.models.ml_spam_upsert_request_partial import MLSpamUpsertRequestPartial

# TODO update the JSON string below
json = "{}"
# create an instance of MLSpamUpsertRequestPartial from a JSON string
ml_spam_upsert_request_partial_instance = MLSpamUpsertRequestPartial.from_json(json)
# print the JSON string representation of the object
print(MLSpamUpsertRequestPartial.to_json())

# convert the object into a dict
ml_spam_upsert_request_partial_dict = ml_spam_upsert_request_partial_instance.to_dict()
# create an instance of MLSpamUpsertRequestPartial from a dict
ml_spam_upsert_request_partial_from_dict = MLSpamUpsertRequestPartial.from_dict(ml_spam_upsert_request_partial_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


