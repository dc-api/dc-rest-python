# DefaultKeywordListTriggerMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_list** | **List[str]** |  | [optional] 
**presets** | **List[int]** |  | [optional] 

## Example

```python
from dc_rest.models.default_keyword_list_trigger_metadata import DefaultKeywordListTriggerMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of DefaultKeywordListTriggerMetadata from a JSON string
default_keyword_list_trigger_metadata_instance = DefaultKeywordListTriggerMetadata.from_json(json)
# print the JSON string representation of the object
print(DefaultKeywordListTriggerMetadata.to_json())

# convert the object into a dict
default_keyword_list_trigger_metadata_dict = default_keyword_list_trigger_metadata_instance.to_dict()
# create an instance of DefaultKeywordListTriggerMetadata from a dict
default_keyword_list_trigger_metadata_from_dict = DefaultKeywordListTriggerMetadata.from_dict(default_keyword_list_trigger_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


