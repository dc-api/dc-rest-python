# PollResultsEntryResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**count** | **int** |  | 
**me_voted** | **bool** |  | [optional] 

## Example

```python
from dc_rest.models.poll_results_entry_response import PollResultsEntryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PollResultsEntryResponse from a JSON string
poll_results_entry_response_instance = PollResultsEntryResponse.from_json(json)
# print the JSON string representation of the object
print(PollResultsEntryResponse.to_json())

# convert the object into a dict
poll_results_entry_response_dict = poll_results_entry_response_instance.to_dict()
# create an instance of PollResultsEntryResponse from a dict
poll_results_entry_response_from_dict = PollResultsEntryResponse.from_dict(poll_results_entry_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


