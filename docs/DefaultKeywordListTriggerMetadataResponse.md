# DefaultKeywordListTriggerMetadataResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_list** | **List[str]** |  | 
**presets** | **List[int]** |  | 

## Example

```python
from dc_rest.models.default_keyword_list_trigger_metadata_response import DefaultKeywordListTriggerMetadataResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DefaultKeywordListTriggerMetadataResponse from a JSON string
default_keyword_list_trigger_metadata_response_instance = DefaultKeywordListTriggerMetadataResponse.from_json(json)
# print the JSON string representation of the object
print(DefaultKeywordListTriggerMetadataResponse.to_json())

# convert the object into a dict
default_keyword_list_trigger_metadata_response_dict = default_keyword_list_trigger_metadata_response_instance.to_dict()
# create an instance of DefaultKeywordListTriggerMetadataResponse from a dict
default_keyword_list_trigger_metadata_response_from_dict = DefaultKeywordListTriggerMetadataResponse.from_dict(default_keyword_list_trigger_metadata_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


