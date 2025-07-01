# ThreadsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**threads** | [**List[ThreadResponse]**](ThreadResponse.md) |  | 
**members** | [**List[ThreadMemberResponse]**](ThreadMemberResponse.md) |  | 
**has_more** | **bool** |  | [optional] 
**first_messages** | [**List[MessageResponse]**](MessageResponse.md) |  | [optional] 

## Example

```python
from dc_rest.models.threads_response import ThreadsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ThreadsResponse from a JSON string
threads_response_instance = ThreadsResponse.from_json(json)
# print the JSON string representation of the object
print(ThreadsResponse.to_json())

# convert the object into a dict
threads_response_dict = threads_response_instance.to_dict()
# create an instance of ThreadsResponse from a dict
threads_response_from_dict = ThreadsResponse.from_dict(threads_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


