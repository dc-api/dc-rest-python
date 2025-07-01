# PollResultsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**answer_counts** | [**List[PollResultsEntryResponse]**](PollResultsEntryResponse.md) |  | [optional] 
**is_finalized** | **bool** |  | 

## Example

```python
from dc_rest.models.poll_results_response import PollResultsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PollResultsResponse from a JSON string
poll_results_response_instance = PollResultsResponse.from_json(json)
# print the JSON string representation of the object
print(PollResultsResponse.to_json())

# convert the object into a dict
poll_results_response_dict = poll_results_response_instance.to_dict()
# create an instance of PollResultsResponse from a dict
poll_results_response_from_dict = PollResultsResponse.from_dict(poll_results_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


