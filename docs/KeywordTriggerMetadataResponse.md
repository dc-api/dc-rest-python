# KeywordTriggerMetadataResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**keyword_filter** | **List[str]** |  | 
**regex_patterns** | **List[str]** |  | 
**allow_list** | **List[str]** |  | 

## Example

```python
from dc_rest.models.keyword_trigger_metadata_response import KeywordTriggerMetadataResponse

# TODO update the JSON string below
json = "{}"
# create an instance of KeywordTriggerMetadataResponse from a JSON string
keyword_trigger_metadata_response_instance = KeywordTriggerMetadataResponse.from_json(json)
# print the JSON string representation of the object
print(KeywordTriggerMetadataResponse.to_json())

# convert the object into a dict
keyword_trigger_metadata_response_dict = keyword_trigger_metadata_response_instance.to_dict()
# create an instance of KeywordTriggerMetadataResponse from a dict
keyword_trigger_metadata_response_from_dict = KeywordTriggerMetadataResponse.from_dict(keyword_trigger_metadata_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


