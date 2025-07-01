# KeywordUpsertRequestPartial


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
**trigger_metadata** | [**KeywordTriggerMetadata**](KeywordTriggerMetadata.md) |  | [optional] 

## Example

```python
from dc_rest.models.keyword_upsert_request_partial import KeywordUpsertRequestPartial

# TODO update the JSON string below
json = "{}"
# create an instance of KeywordUpsertRequestPartial from a JSON string
keyword_upsert_request_partial_instance = KeywordUpsertRequestPartial.from_json(json)
# print the JSON string representation of the object
print(KeywordUpsertRequestPartial.to_json())

# convert the object into a dict
keyword_upsert_request_partial_dict = keyword_upsert_request_partial_instance.to_dict()
# create an instance of KeywordUpsertRequestPartial from a dict
keyword_upsert_request_partial_from_dict = KeywordUpsertRequestPartial.from_dict(keyword_upsert_request_partial_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


