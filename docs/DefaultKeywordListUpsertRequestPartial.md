# DefaultKeywordListUpsertRequestPartial


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
**trigger_metadata** | [**DefaultKeywordListTriggerMetadata**](DefaultKeywordListTriggerMetadata.md) |  | [optional] 

## Example

```python
from dc_rest.models.default_keyword_list_upsert_request_partial import DefaultKeywordListUpsertRequestPartial

# TODO update the JSON string below
json = "{}"
# create an instance of DefaultKeywordListUpsertRequestPartial from a JSON string
default_keyword_list_upsert_request_partial_instance = DefaultKeywordListUpsertRequestPartial.from_json(json)
# print the JSON string representation of the object
print(DefaultKeywordListUpsertRequestPartial.to_json())

# convert the object into a dict
default_keyword_list_upsert_request_partial_dict = default_keyword_list_upsert_request_partial_instance.to_dict()
# create an instance of DefaultKeywordListUpsertRequestPartial from a dict
default_keyword_list_upsert_request_partial_from_dict = DefaultKeywordListUpsertRequestPartial.from_dict(default_keyword_list_upsert_request_partial_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


