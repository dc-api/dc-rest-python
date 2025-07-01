# PollAnswerCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**poll_media** | [**PollMediaCreateRequest**](PollMediaCreateRequest.md) |  | 

## Example

```python
from dc_rest.models.poll_answer_create_request import PollAnswerCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PollAnswerCreateRequest from a JSON string
poll_answer_create_request_instance = PollAnswerCreateRequest.from_json(json)
# print the JSON string representation of the object
print(PollAnswerCreateRequest.to_json())

# convert the object into a dict
poll_answer_create_request_dict = poll_answer_create_request_instance.to_dict()
# create an instance of PollAnswerCreateRequest from a dict
poll_answer_create_request_from_dict = PollAnswerCreateRequest.from_dict(poll_answer_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


