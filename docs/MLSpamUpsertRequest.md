# MLSpamUpsertRequest


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
**trigger_metadata** | **object** |  | [optional] 

## Example

```python
from dc_rest.models.ml_spam_upsert_request import MLSpamUpsertRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MLSpamUpsertRequest from a JSON string
ml_spam_upsert_request_instance = MLSpamUpsertRequest.from_json(json)
# print the JSON string representation of the object
print(MLSpamUpsertRequest.to_json())

# convert the object into a dict
ml_spam_upsert_request_dict = ml_spam_upsert_request_instance.to_dict()
# create an instance of MLSpamUpsertRequest from a dict
ml_spam_upsert_request_from_dict = MLSpamUpsertRequest.from_dict(ml_spam_upsert_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


