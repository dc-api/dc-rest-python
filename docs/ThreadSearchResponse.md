# ThreadSearchResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**threads** | [**List[ThreadResponse]**](ThreadResponse.md) |  | 
**members** | [**List[ThreadMemberResponse]**](ThreadMemberResponse.md) |  | 
**has_more** | **bool** |  | [optional] 
**first_messages** | [**List[MessageResponse]**](MessageResponse.md) |  | [optional] 
**total_results** | **int** |  | [optional] 

## Example

```python
from dc_rest.models.thread_search_response import ThreadSearchResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ThreadSearchResponse from a JSON string
thread_search_response_instance = ThreadSearchResponse.from_json(json)
# print the JSON string representation of the object
print(ThreadSearchResponse.to_json())

# convert the object into a dict
thread_search_response_dict = thread_search_response_instance.to_dict()
# create an instance of ThreadSearchResponse from a dict
thread_search_response_from_dict = ThreadSearchResponse.from_dict(thread_search_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


