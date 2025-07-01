# DefaultKeywordListUpsertRequest


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
**trigger_metadata** | [**DefaultKeywordListTriggerMetadata**](DefaultKeywordListTriggerMetadata.md) |  | 

## Example

```python
from dc_rest.models.default_keyword_list_upsert_request import DefaultKeywordListUpsertRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DefaultKeywordListUpsertRequest from a JSON string
default_keyword_list_upsert_request_instance = DefaultKeywordListUpsertRequest.from_json(json)
# print the JSON string representation of the object
print(DefaultKeywordListUpsertRequest.to_json())

# convert the object into a dict
default_keyword_list_upsert_request_dict = default_keyword_list_upsert_request_instance.to_dict()
# create an instance of DefaultKeywordListUpsertRequest from a dict
default_keyword_list_upsert_request_from_dict = DefaultKeywordListUpsertRequest.from_dict(default_keyword_list_upsert_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


