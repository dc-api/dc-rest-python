# KeywordTriggerMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**keyword_filter** | **List[str]** |  | [optional] 
**regex_patterns** | **List[str]** |  | [optional] 
**allow_list** | **List[str]** |  | [optional] 

## Example

```python
from dc_rest.models.keyword_trigger_metadata import KeywordTriggerMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of KeywordTriggerMetadata from a JSON string
keyword_trigger_metadata_instance = KeywordTriggerMetadata.from_json(json)
# print the JSON string representation of the object
print(KeywordTriggerMetadata.to_json())

# convert the object into a dict
keyword_trigger_metadata_dict = keyword_trigger_metadata_instance.to_dict()
# create an instance of KeywordTriggerMetadata from a dict
keyword_trigger_metadata_from_dict = KeywordTriggerMetadata.from_dict(keyword_trigger_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


