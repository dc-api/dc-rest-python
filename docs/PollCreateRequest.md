# PollCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**question** | [**PollMedia**](PollMedia.md) |  | 
**answers** | [**List[PollAnswerCreateRequest]**](PollAnswerCreateRequest.md) |  | 
**allow_multiselect** | **bool** |  | [optional] 
**layout_type** | **int** |  | [optional] 
**duration** | **int** |  | [optional] 

## Example

```python
from dc_rest.models.poll_create_request import PollCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PollCreateRequest from a JSON string
poll_create_request_instance = PollCreateRequest.from_json(json)
# print the JSON string representation of the object
print(PollCreateRequest.to_json())

# convert the object into a dict
poll_create_request_dict = poll_create_request_instance.to_dict()
# create an instance of PollCreateRequest from a dict
poll_create_request_from_dict = PollCreateRequest.from_dict(poll_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


