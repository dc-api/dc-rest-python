# DefaultKeywordListUpsertRequestActionsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **int** |  | 
**metadata** | [**UserCommunicationDisabledActionMetadata**](UserCommunicationDisabledActionMetadata.md) |  | 

## Example

```python
from dc_rest.models.default_keyword_list_upsert_request_actions_inner import DefaultKeywordListUpsertRequestActionsInner

# TODO update the JSON string below
json = "{}"
# create an instance of DefaultKeywordListUpsertRequestActionsInner from a JSON string
default_keyword_list_upsert_request_actions_inner_instance = DefaultKeywordListUpsertRequestActionsInner.from_json(json)
# print the JSON string representation of the object
print(DefaultKeywordListUpsertRequestActionsInner.to_json())

# convert the object into a dict
default_keyword_list_upsert_request_actions_inner_dict = default_keyword_list_upsert_request_actions_inner_instance.to_dict()
# create an instance of DefaultKeywordListUpsertRequestActionsInner from a dict
default_keyword_list_upsert_request_actions_inner_from_dict = DefaultKeywordListUpsertRequestActionsInner.from_dict(default_keyword_list_upsert_request_actions_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


