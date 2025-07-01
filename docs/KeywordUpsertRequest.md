# KeywordUpsertRequest


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
**trigger_metadata** | [**KeywordTriggerMetadata**](KeywordTriggerMetadata.md) |  | [optional] 

## Example

```python
from dc_rest.models.keyword_upsert_request import KeywordUpsertRequest

# TODO update the JSON string below
json = "{}"
# create an instance of KeywordUpsertRequest from a JSON string
keyword_upsert_request_instance = KeywordUpsertRequest.from_json(json)
# print the JSON string representation of the object
print(KeywordUpsertRequest.to_json())

# convert the object into a dict
keyword_upsert_request_dict = keyword_upsert_request_instance.to_dict()
# create an instance of KeywordUpsertRequest from a dict
keyword_upsert_request_from_dict = KeywordUpsertRequest.from_dict(keyword_upsert_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


