# RatelimitedResponse

Ratelimit error object returned by the Discord API

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** | Discord internal error code. See error code reference | 
**message** | **str** | Human-readable error message | 
**retry_after** | **float** | The number of seconds to wait before retrying your request | 
**var_global** | **bool** | Whether you are being ratelimited by the global ratelimit or a per-endpoint ratelimit | 

## Example

```python
from dc_rest.models.ratelimited_response import RatelimitedResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RatelimitedResponse from a JSON string
ratelimited_response_instance = RatelimitedResponse.from_json(json)
# print the JSON string representation of the object
print(RatelimitedResponse.to_json())

# convert the object into a dict
ratelimited_response_dict = ratelimited_response_instance.to_dict()
# create an instance of RatelimitedResponse from a dict
ratelimited_response_from_dict = RatelimitedResponse.from_dict(ratelimited_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


